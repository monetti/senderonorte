# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ActivitieRegion'
        db.create_table('activities_activitieregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('activities', ['ActivitieRegion'])

        # Adding model 'Activitie'
        db.create_table('activities_activitie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.ActivitieRegion'])),
            ('duration', self.gf('django.db.models.fields.IntegerField')(max_length='10')),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('publish_newsletter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('activities', ['Activitie'])


    def backwards(self, orm):
        
        # Deleting model 'ActivitieRegion'
        db.delete_table('activities_activitieregion')

        # Deleting model 'Activitie'
        db.delete_table('activities_activitie')


    models = {
        'activities.activitie': {
            'Meta': {'ordering': "('region',)", 'object_name': 'Activitie'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {'max_length': "'10'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'publish_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activities.ActivitieRegion']"})
        },
        'activities.activitieregion': {
            'Meta': {'object_name': 'ActivitieRegion'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['activities']
