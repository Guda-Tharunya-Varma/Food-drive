# Generated by Django 4.0.6 on 2022-07-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fooddetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nameofdonor', models.CharField(max_length=100, verbose_name='Enter name')),
                ('Itemname', models.CharField(max_length=100, verbose_name='Enter food item name')),
                ('Itype', models.CharField(max_length=100, verbose_name='enter Item type')),
                ('Location', models.TextField()),
            ],
        ),
    ]
