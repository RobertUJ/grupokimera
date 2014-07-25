# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SlideHome.name'
        db.delete_column(u'home_slidehome', 'name')

        # Deleting field 'SlideHome.image'
        db.delete_column(u'home_slidehome', 'image')

        # Adding field 'SlideHome.nombre'
        db.add_column(u'home_slidehome', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'SlideHome.imagen'
        db.add_column(u'home_slidehome', 'imagen',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SlideHome.name'
        db.add_column(u'home_slidehome', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'SlideHome.image'
        db.add_column(u'home_slidehome', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'SlideHome.nombre'
        db.delete_column(u'home_slidehome', 'nombre')

        # Deleting field 'SlideHome.imagen'
        db.delete_column(u'home_slidehome', 'imagen')


    models = {
        u'home.slidehome': {
            'Meta': {'object_name': 'SlideHome'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'orden': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['home']