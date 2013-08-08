Monday Tech - Django Haystack
=============================

This talk will cover Django Haystack + Elasticsearch.

The slides are located here: [http://goo.gl/CBIECi](http://goo.gl/CBIECi)

Dependency Setup
-----

This talk will use vagrant to setup a few requirements. You need a current version of Virtualbox and Vagrant. This box will setup:

 - JDK
 - Elasticsearch

Make sure its working:

```bash
$ vagrant up

$ curl localhost:9200/_cluster/nodes/_local

$ curl -XGET 'localhost:9200/test/_analyze?text=this+is+a+test'
```

Data Setup
----------

You need to setup some twitter api keys to get some random data. https://dev.twitter.com and setup an app to get some auth tokens.

```bash
$ export CONSUMER_KEY="your-consumer-key-here"
$ export CONSUMER_SECRET="you-consumer-secret-here"
$ export ACCESS_KEY="your-access-key-here"
$ export ACCESS_SECRET="your-access-secret-here"
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py load_tweets #run this for a few minutes and ctrl-c to stop
$ python manage.py runserver
```
