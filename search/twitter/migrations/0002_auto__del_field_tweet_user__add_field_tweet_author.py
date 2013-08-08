# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tweet.user'
        db.delete_column('twitter', 'user_id')

        # Adding field 'Tweet.author'
        db.add_column('twitter', 'author',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['twitter.Author'], unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Tweet.user'
        db.add_column('twitter', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['twitter.Author'], unique=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Tweet.author'
        db.delete_column('twitter', 'author_id')


    models = {
        u'twitter.author': {
            'Meta': {'object_name': 'Author', 'db_table': "'author'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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