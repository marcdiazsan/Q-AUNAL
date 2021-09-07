from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.fields.core import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from qaunal.models import User
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='Este campo es obligatorio'), Length(
        min=10, message="El nombre es demasiado corto")])
    email = StringField('Email', validators=[DataRequired(
        message='Este campo es obligatorio'), Email(message='Dirección de correo no válida')])
    password = PasswordField('Contraseña', validators=[
                             DataRequired(message='Este campo es obligatorio')])
    password_confirmation = PasswordField(
        'Confirmar Contraseña', validators=[DataRequired(message='Este campo es obligatorio'), EqualTo('password', message='Las contraseñas no coinciden')])
    submit = SubmitField('Registrarse')

    # Validar que el correo no exista ya en la base de usuarios
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "El correo ya está registrado. Intente iniciando sesión")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(
        message='Este campo es obligatorio'), Email(message='Dirección de correo invalida')])
    password = PasswordField('Contraseña', validators=[
                             DataRequired(message='Este campo es obligatorio')])
    remember = BooleanField('Recuerdame')
    submit = SubmitField('Iniciar Sesion')


class CreateQuestionForm(FlaskForm):
    opcionesEstatus = [('Resuelta', 'Resuelta'),
                       ('No Resuelta', 'No Resuelta')]
    etiquetasTema = [('Artes', 'Artes'), 
                     ('Ingenieria', 'Ingenieria'), 
                     ('Ciencias', 'Ciencias'),
                     ('Ciencias Economicas', 'Ciencias Economicas'),
                     ('Medicina', 'Medicina'),
                     ('Medicina Veterinaria y de Zootecnia',
                      'Medicina Veterinaria y de Zootecnia'),
                     ('Ciencias Agrarias', 'Ciencias Agrarias'),
                     ('Ciencias Humanas', 'Ciencias Humanas'), 
                     ('Derecho, Ciencias Políticas y Sociales', 'Derecho, Ciencias Políticas y Sociales'), 
                     ('Enfermeria', 'Enfermeria'),
                     ('Odontologia', 'Odontologia')]
    titulo = StringField('Titulo', validators=[
                         DataRequired()])
    contenido = TextAreaField('Contenido', validators=[
        DataRequired(message='Este campo es obligatorio')])
    tema = SelectField('Tema', choices=etiquetasTema)
    estatus = SelectField('Estatus', choices=opcionesEstatus)
    submit = SubmitField('Crear Pregunta')


class CreateCommentForm(FlaskForm):
    contenido = TextAreaField('Contenido', validators=[DataRequired(
        message='Este campo es obligatorio'), Length(min=2)])
    submit = SubmitField('Añadir Comentario')

class BusquedaTexto(FlaskForm):
    textoBusqueda = StringField('Busqueda', validators=[Length(min=1)])
    submit = SubmitField('Buscar')

class BusquedaTag(FlaskForm):
    textoEtiqueta = StringField('Busqueda', validators=[Length(min=1)])
    submit = SubmitField('Filtrar')

class FiltroFechas(FlaskForm):
    fechaInicio = DateField('Inicio', format='%Y-%m-%d')
    fechaFin = DateField('Fin', format='%Y-%m-%d')
    submit = SubmitField('Filtrar')
