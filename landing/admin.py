from landing.forms import SignUpChangeForm
from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    add_form = SignUpChangeForm
    list_display = ['email', 'first_name', 'last_name', 'phone_number']
    list_display_links = ['email']


# Register your models here.
admin.site.register(User, UserAdmin)
