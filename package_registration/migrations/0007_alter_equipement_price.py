# Generated by Django 3.2.5 on 2021-08-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_registration', '0006_divetype_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Price in $'),
        ),
    ]
