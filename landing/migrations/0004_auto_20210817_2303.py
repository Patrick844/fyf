# Generated by Django 3.2.5 on 2021-08-17 20:03

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_remove_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='diving_level',
            field=models.CharField(choices=[('None', 'None'), ('Scuba Diver', 'Scuba Diver'), ('Advance Scuba Diver', 'Advance Scuba Diver'), ('Technincal Diver', 'Technincal Diver'), ('Rescue Diver', 'Rescue Diver'), ('Instructor', 'Instructor')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='user',
            name='specialty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
