import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://anime:1234@postgreSQL:5432/Test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    Elasticsearch_URI = 'http://elasticsearch:9200/'
    host_for_flask = '0.0.0.0'
    port_for_flask = 5000
