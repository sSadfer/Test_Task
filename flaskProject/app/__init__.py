from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from elasticsearch import Elasticsearch

db = SQLAlchemy()
es = Elasticsearch(Config.Elasticsearch_URI)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


app = create_app()
from app import models, routes

app.app_context().push()  # Подтягивание зависимостей web_service
db.create_all()  # Создание недостающих таблиц
