# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Excurtion.activitie'
        db.add_column('excurtion_excurtion', 'activitie', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['activities.Activitie']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Excurtion.activitie'
        db.delete_column('excurtion_excurtion', 'activitie_id')


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
        },
        'excurtion.excurtion': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Excurtion'},
            'activitie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['activities.Activitie']"}),
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
