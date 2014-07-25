# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class SlideHome(models.Model):
	# TODO: Define fields here
	nombre = models.CharField(verbose_name='Nombre', max_length=50)
	imagen = models.ImageField(upload_to='slides',verbose_name='Imagen del Slide')
	html = models.TextField(verbose_name='Ingresa aquí el html del slide.')
	orden = models.PositiveSmallIntegerField(verbose_name='Orden')
	activo = models.BooleanField(default=True,verbose_name='Activo')

	class Meta:
		verbose_name = 'Slide Home'
		verbose_name_plural = 'Slides en Inicio'

	def __unicode__(self):
		return "%s | %s" % (self.nombre, self.orden)

	# def save(self):
	# 	pass

	# @models.permalink
	# def get_absolute_url(self):
	# 	return ('')

    # TODO: Defne custom methods here

