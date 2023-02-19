from django.db import models

class Estacion(models.Model):
    id_estacion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    espacios_vacios = models.IntegerField()
    def __str__(self):
        return self.nombre
