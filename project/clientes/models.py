from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre.capitalize()


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre.capitalize()} {self.apellido.capitalize()}'