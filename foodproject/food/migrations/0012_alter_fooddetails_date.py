# Generated by Django 4.0.6 on 2022-07-15 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_fooddetails_date_fooddetails_fexpiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetails',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
