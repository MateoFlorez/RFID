# Generated by Django 4.1.1 on 2022-10-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_alter_ingreso_data_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingreso',
        ),
    ]
