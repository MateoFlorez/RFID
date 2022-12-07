from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.

# Modelo de los registros RFID (Campos en la base de datos)
class Registro(models.Model):
    codigoRFID = models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cc = models.PositiveIntegerField()

    def __str__(self):
        texto = "{0} {1} ({2}) {3} - "
        return texto.format(self.nombre, self.apellido, self.codigoRFID, self.cc)

class Oficina(models.Model):
    idoficina = models.IntegerField(primary_key=True,default=1)
    oficina = models.CharField(max_length=50)
    registros = models.ManyToManyField(Registro, through='RegistroOficina')
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.oficina, self.idoficina)

class RegistroOficina(models.Model):
    codigoRFID = models.ForeignKey(Registro, on_delete=models.CASCADE)
    idoficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.codigoRFID, self.idoficina)
    
class Ingreso(models.Model):
    data_time = models.DateTimeField(auto_now_add=True)
    codigoRFID = models.CharField(max_length=20)
    idoficina = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
