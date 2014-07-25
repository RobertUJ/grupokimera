# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SlideHome'
        db.create_table(u'home_slidehome', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'home', ['SlideHome'])


    def backwards(self, orm):
        # Deleting model 'SlideHome'
        db.delete_table(u'home_slidehome')


    models = {
        u'home.slidehome': {
            'Meta': {'object_name': 'SlideHome'},
            'html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']