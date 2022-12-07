# Generated by Django 4.1.1 on 2022-10-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0006_delete_ingreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('codigoRFID', models.CharField(max_length=20)),
                ('idoficina', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]