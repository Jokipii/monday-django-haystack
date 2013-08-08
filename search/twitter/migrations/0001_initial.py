# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'twitter', ['Author'])

        # Adding model 'Tweet'
        db.create_table('twitter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('retweet_count', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['twitter.Author'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'twitter', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('author')

        # Deleting model 'Tweet'
        db.delete_table('twitter')


    models = {
        u'twitter.author': {
            'Meta': {'object_name': 'Author', 'db_table': "'author'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'twitter.tweet': {
            'Meta': {'object_name': 'Tweet', 'db_table': "'twitter'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'retweet_count': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['twitter.Author']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['twitter']