from django.contrib import admin
from .models import Accomodation, DiveType, Equipement, Package, Reservation, ReservationDives, ReservationEquipments, ReservationHotel, Room


class DiveTypeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "price", "level"]
    list_display_links = ["pk"]
    list_editable = ["name", "price", "level"]


class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_display_links = ["name"]
    list_editable = ["price"]


class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_display_links = ["name"]
    list_editable = ["price"]


class EquipementAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "type"]
    list_display_links = ["name"]
    list_editable = ["price", "type"]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price",
                    "date_reservation", "arrival_date", "arrival_time", "pk"]
    list_display_links = ["user"]
    readonly_fields = ('date_reservation',)


class ReservationDiveAdmin(admin.ModelAdmin):
    list_display = ["dives_name", "price", "reservation"]
    list_display_links = ["dives_name"]
    readonly_fields = ('reservation',)


class ReserverationEquipmentAdmin(admin.ModelAdmin):
    list_display = ["equipment_name", "reservation"]
    list_display_links = ["equipment_name"]
    readonly_fields = ('reservation',)


class ReservationHotelAdmin(admin.ModelAdmin):
    list_display = ["hotel", "room", "hotel_name",
                    "hotel_website", "reservation"]
    list_display_links = ["hotel"]
    readonly_fields = ('reservation',)


class PackageAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk"]


# Register your s here.
admin.site.register(Accomodation, HotelAdmin)
admin.site.register(DiveType, DiveTypeAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationDives, ReservationDiveAdmin)
admin.site.register(ReservationEquipments, ReserverationEquipmentAdmin)
admin.site.register(ReservationHotel, ReservationHotelAdmin)
