# Generated by Django 4.0.6 on 2022-07-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_fooddetails_date_fooddetails_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetails',
            name='Date',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='fooddetails',
            name='Fexpiry',
            field=models.TimeField(default=0),
        ),
    ]
