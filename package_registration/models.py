from django.db import models
from landing.models import User

# Create your models here.

DIVING_TYPES = [
    ("Entry-Level", "Entry-Level"),
    ("Specialty", "Specialty"),
    ("Leadership", "Leadership"),
    ("Technical Diver", "Technical Diver"),
    ("Continuing Education", "Continuing Education"),
    ("First Aid", "First Aid"),
    ("Support Course", "Support Course"),
    ("Instructor Specialty", "Instructor Specialty"),
    ("Recognition", "Recognition"),
    ("Supervised Diver", "Supervised Diver"),
    ("Public Safety Diving", "Public Safety Diving"),
    ("Freediving", "Freediving"),


]


EQUIPMENT = [
    ("Full equipment", "Full equipment"),
    ("Normal", "Normal"),
    ("No equipment", "No equipment")
]


class Package(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField("Price in $",
                                max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Accomodation(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField("Price in $",
                                max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Equipement(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(
        "Price in $", max_digits=6, decimal_places=2, null=True, blank=True)
    type = models.CharField(max_length=120, null=True,
                            blank=True, choices=EQUIPMENT)

    def __str__(self) -> str:
        return self.name


class DiveType(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField("Price in $",
                                max_digits=6, decimal_places=2, null=True, blank=True)
    level = models.CharField(max_length=120, null=True,
                             blank=True, choices=DIVING_TYPES)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField("Price in $",
                                max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    total_price = models.DecimalField("Total price in $",
                                      max_digits=6, decimal_places=2, null=True, blank=True)
    date_reservation = models.DateTimeField(auto_now_add=True, editable=True)
    package = models.ForeignKey(
        Package, blank=True, null=True, on_delete=models.CASCADE)
    arrival_date = models.DateField(null=True, blank=True, editable=True)

    arrival_time = models.TimeField(blank=True, null=True)

    status = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.pk)


class ReservationDives(models.Model):
    dives_name = models.ForeignKey(
        DiveType, blank=True, null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(
        Reservation, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField("Price in $",
                                max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.dives_name.name


class ReservationEquipments(models.Model):
    equipment_name = models.ForeignKey(
        Equipement, blank=True, null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(
        Reservation, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField("Price in $",
                                max_digits=6, decimal_places=2, null=True, blank=True)


class ReservationHotel(models.Model):
    hotel = models.ForeignKey(
        Accomodation, blank=True, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, blank=True, null=True, on_delete=models.CASCADE)
    price_hotel = models.DecimalField("Price in $",
                                      max_digits=6, decimal_places=2, null=True, blank=True)
    price_room = models.DecimalField("Price in $",
                                     max_digits=6, decimal_places=2, null=True, blank=True)
    hotel_name = models.CharField(max_length=120, blank=True, null=True)
    hotel_website = models.URLField(max_length=200, blank=True, null=True)
    reservation = models.ForeignKey(
        Reservation, null=True, blank=True, on_delete=models.CASCADE)
