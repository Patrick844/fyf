from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class User(AbstractUser):
    DIVING_LEVELS = [
        ("None", "None"),
        ("Scuba Diver", "Scuba Diver"),
        ("Advance Scuba Diver", "Advance Scuba Diver"),
        ("Technincal Diver", "Technincal Diver"),
        ("Rescue Diver", "Rescue Diver"),
        ("Instructor", "Instructor"),
        ("Others", "Others"),
    ]

    username = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    phone_number = PhoneNumberField(
        blank=True, null=True)
    diving_level = models.CharField(
        blank=True, null=True, max_length=20, choices=DIVING_LEVELS)

    speciality = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(
        blank=True, null=True, upload_to="profile_pictures")
    pass

    def __str__(self):
        return self.email
