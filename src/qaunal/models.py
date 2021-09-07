from datetime import datetime
import enum
from qaunal import db, login_manager
from flask_login import UserMixin

# Obtener el id de usuario


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profilepic = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    preguntas = db.relationship(
        'Pregunta', backref='autor', lazy=True, cascade='all, delete')
    comentarios = db.relationship('Comentario', backref='autor', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f"id:{self.id}\nNombre:{self.nombre}\nEmail:{self.email}\nProfile Picture:{self.profilepic}"


class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    contenido = db.Column(db.Text, nullable=False)
    etiquetas = db.Column(db.String())
    resuelta = db.Column(db.Boolean(), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comentarios = db.relationship(
        'Comentario', backref='pregunta', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f"id:{self.id}\nTitulo:{self.titulo}\n"


class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    contenido = db.Column(db.Text, nullable=False)
    util = db.Column(db.Boolean(), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey(
        'pregunta.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"id:{self.id}\nContenido:{self.contenido}\n"
