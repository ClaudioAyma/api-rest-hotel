# Generated by Django 3.2.5 on 2021-07-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_hotel', '0004_auto_20210721_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='capacidad',
            field=models.IntegerField(default=0),
        ),
    ]
