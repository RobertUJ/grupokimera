# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SlideHome.orden'
        db.add_column(u'home_slidehome', 'orden',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SlideHome.orden'
        db.delete_column(u'home_slidehome', 'orden')


    models = {
        u'home.slidehome': {
            'Meta': {'object_name': 'SlideHome'},
            'html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'orden': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['home']