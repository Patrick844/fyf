# Generated by Django 3.2.5 on 2021-08-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='DiveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RenameModel(
            old_name='PackageModel',
            new_name='Package',
        ),
        migrations.DeleteModel(
            name='AccomodationModel',
        ),
        migrations.DeleteModel(
            name='DiveTypeModel',
        ),
        migrations.DeleteModel(
            name='EquipementModel',
        ),
    ]
