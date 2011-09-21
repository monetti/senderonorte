# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EducationTravel'
        db.create_table('educationtravels_educationtravel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('educationtravels', ['EducationTravel'])


    def backwards(self, orm):
        
        # Deleting model 'EducationTravel'
        db.delete_table('educationtravels_educationtravel')


    models = {
        'educationtravels.educationtravel': {
            'Meta': {'ordering': "('name',)", 'object_name': 'EducationTravel'},
            'duration': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['educationtravels']
