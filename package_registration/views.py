from package_registration.forms import dummy
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from package_registration.models import Accomodation, DiveType, Equipement, Package, Reservation, ReservationDives, ReservationEquipments, ReservationHotel, Room
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings


# Create your views here. package_registration/package_registration.html"


def BookRegistration(request, pk):

    accomodations = Accomodation.objects.all().order_by("name")
    rooms = Room.objects.all()

    entry_level = DiveType.objects.filter(level="Entry-Level")
    specialty_level = DiveType.objects.filter(level="Specialty")
    leadership_level = DiveType.objects.filter(level="Leadership")
    technical_level = DiveType.objects.filter(level="Technical Diver")
    freediving_level = DiveType.objects.filter(level="Freediving")
    aid_level = DiveType.objects.filter(level="First Aid")
    education_level = DiveType.objects.filter(level="Continuing Education")
    instructor_level = DiveType.objects.filter(level="Instructor Specialty")
    support_level = DiveType.objects.filter(level="Support Course")
    recognition_level = DiveType.objects.filter(level="Recognition")
    supervised_level = DiveType.objects.filter(level="Supervised Diver")
    public_level = DiveType.objects.filter(level="Public Safety Diving")

    equipements = Equipement.objects.all()
    personals = equipements.filter(type="Full equipment")
    essentials = equipements.filter(type="Normal")
    no_equipment = equipements.get(type="No equipment")

    context = {
        "accomodations": accomodations,
        "rooms": rooms,


        "divers_level": entry_level,
        "specialty_levels": specialty_level,
        "leadership_levels": leadership_level,
        "technical_levels": technical_level,
        "leadership_levels": leadership_level,
        "freediving_levels": freediving_level,
        "aid_levels": aid_level,
        "education_levels": education_level,
        "instructor_levels": instructor_level,
        "support_levels": support_level,
        "recognition_levels": recognition_level,
        "supervised_levels": supervised_level,
        "public_levels": public_level,






        "personals": personals,
        "essentials": essentials,
        "no_equipment": no_equipment,
        "pk": pk,

    }
    if request.method == "POST":
        print(request.POST)

        hotel = request.POST.get('accomodations', "None")
        room = request.POST.get('rooms', "None")
        dives = request.POST.getlist("dives", [])
        equipment = request.POST.getlist("equipments", [])
        date_arrival = request.POST.get('date_arrival')
        time_arrival = request.POST.get('time_arrival')
        print(room)

        reservation = Reservation()
        package = Package.objects.get(id=pk)

        reservation.package = package
        reservation.arrival_date = date_arrival
        reservation.arrival_time = time_arrival
        reservation.save()

        if dives:
            for dive in dives:
                dive_type = DiveType.objects.get(name=dive)
                res_dive = ReservationDives()
                res_dive.dives_name = dive_type
                res_dive.reservation = reservation
                res_dive.price = dive_type.price
                res_dive.save()

        if equipment:
            for eq in equipment:
                equipment_name = Equipement.objects.get(name=eq)
                res_equipment = ReservationEquipments()
                res_equipment.equipment_name = equipment_name
                res_equipment.reservation = reservation
                res_equipment.price = dive_type.price
                res_equipment.save()

        hotel_type = Accomodation.objects.get(name=hotel)
        room_type = Room.objects.get(name=room)
        res_hotel = ReservationHotel()
        res_hotel.hotel = hotel_type
        res_hotel.room = room_type
        res_hotel.price_hotel = hotel_type.price
        res_hotel.price_room = room_type.price
        res_hotel.reservation = reservation
        res_hotel.save()

        package = Package.objects.get(id=pk)

        return redirect(reverse('packages:registration-summary', kwargs={'pk': reservation.pk}))

    return render(request, "package_registration/package_registration.html", context)


class SummaryView(LoginRequiredMixin, generic.FormView):
    template_name = "package_registration/purchase_summary.html"
    form_class = dummy

    def get_context_data(self, **kwargs):
        total_price_dives = 0
        total_price_equipment = 0
        total_price_hotel = 0
        total_price = 0
        pk = self.kwargs["pk"]
        context = super(SummaryView, self).get_context_data(**kwargs)
        dives = ReservationDives.objects.filter(reservation=pk)
        equipments = ReservationEquipments.objects.filter(reservation=pk)
        hotel = ReservationHotel.objects.get(reservation=pk)
        reservation = Reservation.objects.get(pk=pk)
        package = Package.objects.get(name=reservation.package)

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
            "total_price": total_price

        })

        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        reservation = Reservation.objects.get(pk=pk)
        total_price = request.POST.get("price")

        reservation.user = self.request.user
        reservation.total_price = total_price
        reservation.save()

        return redirect(reverse('packages:registration-payment', kwargs={'pk': pk}))


class PaymentView(generic.FormView):
    template_name = "package_registration/payment.html"
    form_class = dummy

    def post(self, request, *args, **kwargs):
        total_price = 0
        pk = self.kwargs["pk"]
        context = super(PaymentView, self).get_context_data(**kwargs)
        dives = ReservationDives.objects.filter(reservation=pk)
        equipments = ReservationEquipments.objects.filter(reservation=pk)
        hotel = ReservationHotel.objects.get(reservation=pk)
        reservation = Reservation.objects.get(pk=pk)
        package = Package.objects.get(name=reservation.package)

        plaintext = get_template(
            'package_registration/confirmation_email.txt').render()
        htmly = get_template(
            'package_registration/confirmation_email.html').render()

        subject, from_email, to = 'Your Purchase Information', settings.EMAIL_HOST_USER, self.request.user

        msg = EmailMultiAlternatives(subject, plaintext, from_email, [to])
        msg.attach_alternative(htmly, "text/html")
        msg.send()
        return redirect(reverse('landing:home'))
