from django.db import models
from django.core.urlresolvers import reverse
import datetime


class Cliente(models.Model):
    name = models.CharField(max_length=200)
    identificacion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha_creacion = models.CharField(max_length=200, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})


class Animal(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    fecha_nacim = models.CharField(max_length=200)
    id_cliente = models.IntegerField()
    fecha_creacion = models.CharField(max_length=200, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})


class Cita(models.Model):
    id_animal = models.IntegerField()
    name = models.CharField(max_length=500)
    fecha_cita = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today() + datetime.timedelta(days=1))
    descripcion = models.CharField(max_length=500)
    fecha_creacion = models.CharField(max_length=200, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})

class Historia(models.Model):
    id_historia = models.IntegerField()
    id_animal = models.IntegerField()
    name = models.CharField(max_length=500, default='name')
    descripcion = models.CharField(max_length=500)
    fecha_creacion = models.CharField(max_length=200, default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})