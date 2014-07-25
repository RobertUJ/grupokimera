# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SlideHome.activo'
        db.add_column(u'home_slidehome', 'activo',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SlideHome.activo'
        db.delete_column(u'home_slidehome', 'activo')


    models = {
        u'home.slidehome': {
            'Meta': {'object_name': 'SlideHome'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'orden': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['home']