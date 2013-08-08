# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tweet.location_name'
        db.add_column('twitter', 'location_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Tweet.country'
        db.add_column('twitter', 'country',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tweet.location_name'
        db.delete_column('twitter', 'location_name')

        # Deleting field 'Tweet.country'
        db.delete_column('twitter', 'country')


    models = {
        u'twitter.author': {
            'Meta': {'object_name': 'Author', 'db_table': "'author'"},
            'followers_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'friends_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile_image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'statuses_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'twitter_id': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'twitter.tweet': {
            'Meta': {'object_name': 'Tweet', 'db_table': "'twitter'"},
            'author': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['twitter.Author']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'retweet_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['twitter']