from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField
from django.forms import widgets
from django.forms.fields import CharField
from .models import User
from django.core.exceptions import ValidationError
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_bootstrap5.bootstrap5 import FloatingField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.validators import validate_international_phonenumber


class SignUpForm(UserCreationForm):

    profile_picture = forms.ImageField(
        label="Profile picture (optional)", required=False)
    speciality = forms.CharField(
        max_length=100, label="Speciality (If applicable)", required=False)
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'class': "form-control float-start dropdown-toogle mb-4 w-50"}))
    phone_number.error_messages['invalid'] = "Please enter a valid phone number"

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'diving_level', 'speciality', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        data = self.cleaned_data["email"]
        users = User.objects.all()
        for user in users:
            if user.email == data:
                raise ValidationError("email already exists")
        return data


class SignUpChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'diving_level', 'speciality']
