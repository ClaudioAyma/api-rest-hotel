# Generated by Django 3.2.5 on 2021-07-21 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_hotel', '0002_auto_20210721_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estadia_final',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estadia_inicio',
            field=models.DateTimeField(),
        ),
    ]