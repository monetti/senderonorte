# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Region'
        db.create_table('excurtion_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('excurtion', ['Region'])

        # Adding model 'Excurtion'
        db.create_table('excurtion_excurtion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['excurtion.Region'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('place', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('time', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('publish_last_exc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('intro_last_exc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('publish_newsletter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('excurtion', ['Excurtion'])

        # Adding model 'PhotoPostExcurtion'
        db.create_table('excurtion_photopostexcurtion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('excurtion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['excurtion.Excurtion'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('excurtion', ['PhotoPostExcurtion'])


    def backwards(self, orm):
        
        # Deleting model 'Region'
        db.delete_table('excurtion_region')

        # Deleting model 'Excurtion'
        db.delete_table('excurtion_excurtion')

        # Deleting model 'PhotoPostExcurtion'
        db.delete_table('excurtion_photopostexcurtion')


    models = {
        'excurtion.excurtion': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Excurtion'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_last_exc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'publish_last_exc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['excurtion.Region']"}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': "'200'"})
        },
        'excurtion.photopostexcurtion': {
            'Meta': {'ordering': "('excurtion',)", 'object_name': 'PhotoPostExcurtion'},
            'excurtion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['excurtion.Excurtion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'excurtion.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['excurtion']
