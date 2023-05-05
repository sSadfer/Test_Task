from flask import request
from app import app, db, es
from app.models import Texts
from sqlalchemy.exc import IntegrityError
import datetime


@app.route('/', methods=['GET'])
def search():
    return


@app.route('/add_texts', methods=['POST'])
def add_texts():  # Добавление нового теста
    request_data = request.get_json()
    Request_Type = request_data.get('Message_Type', None)

    if Request_Type == 'Add_texts':
        print(Request_Type)
    else:
        return 'Bad Request'
    request_data = request_data.get('Body', None)
    print(request_data)
    for element in request_data:
        try:
            e = Texts(rubrics=element['rubrics'],
                      text=element['text'],
                      created_date=datetime.datetime.strptime(element['created_date'], "%d.%m.%Y  %H:%M:%S").strftime(
                          "%Y-%m-%d %H:%M:%S"))  # форматирование в iso

            db.session.add(e)
            db.session.commit()
            doc1 = {'text': e.text}
            es.index(index='test_task_index', id=e.id, body=doc1)
        except IntegrityError:
            db.session.rollback()
            return 'SQL ERROR'
    return 'Запрос принят'


@app.route('/delete_text', methods=['POST'])
def delete_text():  # Добавление нового теста
    request_data = request.get_json()
    Request_Type = request_data.get('Message_Type', None)

    if Request_Type == 'Delete_text':
        print(Request_Type)
    else:
        return 'Bad Request'
    request_data = request_data.get('Body', None)
    print(request_data)
    try:
        Texts.query.filter_by(id=request_data['id']).delete()
        db.session.commit()
        es.delete(index='test_task_index', id=request_data['id'])
    except IntegrityError:
        db.session.rollback()
        return 'SQL ERROR'
    return 'Запрос принят'


@app.route('/test', methods=['get'])  # Тестовый запрос
def test():
    return '200'


@app.route('/healthcheck', methods=['GET'])  # Проверка состояния
def healthcheck():
    return '200 OK'
