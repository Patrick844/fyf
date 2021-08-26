from datetime import date
from typing import Generic
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.views import generic
from package_registration.models import Package, Reservation, ReservationDives, ReservationEquipments, ReservationHotel
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from package_registration.forms import dummy
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.conf import settings
from django.contrib import messages

User = get_user_model()

# Create your views here.


class OperatorView(LoginRequiredMixin, generic.TemplateView):
    template_name = "adminop/reservations.html"

    def get_context_data(self, **kwargs):
        context = super(OperatorView, self).get_context_data(**kwargs)

        hotel = ReservationHotel.objects.filter(
            Q(hotel_name__isnull=True) | Q(hotel_website__isnull=True)).values_list("reservation", flat=True)
        print(hotel)

        reservation = Reservation.objects.filter(
            arrival_date__gte=date.today()).order_by("-pk")
        for res in reservation:
            print(res.pk)
        reservation_prev = Reservation.objects.filter(
            arrival_date__lt=date.today()).order_by("-pk")

        context.update({
            "reservations": reservation,
            "reservations_prev": reservation_prev,
            "hotels": hotel,
            "today": date.today()
        })
        return context


class OperatorDetailsView(LoginRequiredMixin, generic.FormView):
    template_name = "adminop/reservation_details.html"
    form_class = dummy

    def get_context_data(self, **kwargs):
        context = super(OperatorDetailsView, self).get_context_data(**kwargs)
        total_price_dives = 0
        total_price_equipment = 0
        total_price_hotel = 0
        total_price = 0
        pk = self.kwargs["pk"]

        dives = ReservationDives.objects.filter(reservation=pk)
        equipments = ReservationEquipments.objects.filter(reservation=pk)
        hotel = ReservationHotel.objects.get(reservation=pk)
        reservation = Reservation.objects.get(pk=pk)
        package = Package.objects.get(name=reservation.package)
        user = User.objects.get(email=reservation.user)
        package_price = package.price

        for dive in dives:
            total_price_dives += dive.price

        for eq in equipments:
            total_price_equipment += eq.price

        total_price_hotel = hotel.price_hotel+hotel.price_room

        total_price = total_price_dives+total_price_equipment + \
            total_price_hotel+package_price

        context.update({
            "dives": dives,
            "equipments": equipments,
            "hotel": hotel,
            "reservation": reservation,
            "package_price": package_price,
            "price_hotel": total_price_hotel,
            "price_equipment": total_price_equipment,
            "price_dives": total_price_dives,
            "total_price": total_price,
            'user': user

        })

        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        hotel = ReservationHotel.objects.get(reservation=pk)
        reservation = Reservation.objects.get(pk=pk)
        user = User.objects.get(email=reservation.user)
        hotel_name = request.POST.get("hotel_name")
        hotel_website = request.POST.get("hotel_website")
        hotel.hotel_name = hotel_name
        hotel.hotel_website = hotel_website
        hotel.save()
        context = ({'firstname': user.first_name,
                    "lastname": user.last_name,
                   "pk": pk,
                    "hotel_name": hotel_name,
                    "website": hotel_website}
                   )
        plaintext = render_to_string('adminop/booking.txt', context)

        htmly = render_to_string('adminop/booking.html', context)

        subject, from_email, to = 'Hotel Booking Confirmed', settings.EMAIL_HOST_USER, reservation.user

        msg = EmailMultiAlternatives(subject, plaintext, from_email, [to])
        msg.attach_alternative(htmly, "text/html")
        msg.send()

        messages.add_message(request, messages.SUCCESS, 'Email sent.')

        return redirect(reverse("operator:reservations"))
