# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Author.screen_name'
        db.delete_column('author', 'screen_name')

        # Adding field 'Author.twitter_id'
        db.add_column('author', 'twitter_id',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Author.screen_name'
        db.add_column('author', 'screen_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Deleting field 'Author.twitter_id'
        db.delete_column('author', 'twitter_id')


    models = {
        u'twitter.author': {
            'Meta': {'object_name': 'Author', 'db_table': "'author'"},
            'followers_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'friends_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'statuses_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'twitter_id': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'twitter.tweet': {
            'Meta': {'object_name': 'Tweet', 'db_table': "'twitter'"},
            'author': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['twitter.Author']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'retweet_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['twitter']