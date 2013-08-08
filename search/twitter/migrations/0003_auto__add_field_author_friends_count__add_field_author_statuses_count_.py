# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.friends_count'
        db.add_column('author', 'friends_count',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Author.statuses_count'
        db.add_column('author', 'statuses_count',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Author.followers_count'
        db.add_column('author', 'followers_count',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Author.screen_name'
        db.add_column('author', 'screen_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Author.friends_count'
        db.delete_column('author', 'friends_count')

        # Deleting field 'Author.statuses_count'
        db.delete_column('author', 'statuses_count')

        # Deleting field 'Author.followers_count'
        db.delete_column('author', 'followers_count')

        # Deleting field 'Author.screen_name'
        db.delete_column('author', 'screen_name')


    models = {
        u'twitter.author': {
            'Meta': {'object_name': 'Author', 'db_table': "'author'"},
            'followers_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'friends_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'statuses_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'})
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