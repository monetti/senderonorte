# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Cimbling'
        db.create_table('cimblings_cimbling', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cimbling_type', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('cimblings', ['Cimbling'])


    def backwards(self, orm):
        
        # Deleting model 'Cimbling'
        db.delete_table('cimblings_cimbling')


    models = {
        'cimblings.cimbling': {
            'Meta': {'ordering': "('cimbling_type',)", 'object_name': 'Cimbling'},
            'cimbling_type': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['cimblings']
