from datetime import date
from typing import Generic
from django.shortcuts import render
from django.views import generic
from package_registration.models import Package, Reservation, ReservationDives, ReservationEquipments, ReservationHotel
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class OrderView(LoginRequiredMixin, generic.TemplateView):
    template_name = "userapp/order_history.html"

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)

        reservation = Reservation.objects.filter(
            user=self.request.user).order_by("-pk")

        context.update({
            "reservations": reservation,
            "today": date.today()
        })
        return context


class OrderDetailsView(LoginRequiredMixin, generic.TemplateView):
    template_name = "userapp/order_details.html"

    def get_context_data(self, **kwargs):
        context = super(OrderDetailsView, self).get_context_data(**kwargs)
        total_price_dives = 0
        total_price_equipment = 0
        total_price_hotel = 0
        total_price = 0
        pk = self.kwargs["pk"]
        context = super(OrderDetailsView, self).get_context_data(**kwargs)
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
