from app import db


class Texts(db.Model):
    __tablename__ = 'texts'
    id = db.Column(db.Integer, primary_key=True)            # id для каждого документа;
    rubrics = db.Column(db.String(200), nullable=False)     # Массив рубрик;
    text = db.Column(db.Text(), nullable=False)             # Текст документа;
    created_date = db.Column(db.DateTime())                 # Дата и время создания документа.
