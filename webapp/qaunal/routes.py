from qaunal.estructuras import SLL_Stack
from flask import jsonify, request, render_template, url_for, flash, redirect, abort
from qaunal import app, db, bcrypt
from qaunal.models import User, Pregunta, Comentario
from qaunal.forms import RegistrationForm, LoginForm, CreateQuestionForm, CreateCommentForm, BusquedaTag, BusquedaTexto
from flask_login import login_user, current_user, logout_user, login_required
from qaunal.estructuras import SLL_Stack, RabinKarpMatcher

@app.route('/')
def dashboardPrincipal():
    page =  request.args.get('page', default=1, type=int)
    preguntas = Pregunta.query.all()
    # Uso E.D
    stackPreguntas = SLL_Stack()
    for preg in preguntas:
        stackPreguntas.push(preg)
    # Tamaño del stack de preguntas
    current = stackPreguntas.getHead()
    size = 0
    while current:
        size += 1
        current = current.getNext()
    return render_template('home.html', titulo='Inicio', preguntas=stackPreguntas, size=size)


@app.route('/registrarse', methods=['GET', 'POST'])
def registroUsuario():
    if current_user.is_authenticated:
        return redirect(url_for('dashboardPrincipal'))

    forma = RegistrationForm()
    if forma.validate_on_submit():
        # Registro de un usuario nuevo
        hashed_password = bcrypt.generate_password_hash(
            forma.password.data).decode('utf-8')
        user = User(nombre=forma.nombre.data,
                    email=forma.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # Dar un mensaje al usuario
        flash('Bienvenido a QA UNAL, {}!. Inicia sesión!'.format(
            forma.nombre.data), 'success')
        return redirect(url_for('iniciarSesion'))
    return render_template('registroUsuario.html', forma=forma, titulo='Registro')


@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciarSesion():
    forma = LoginForm()
    if forma.validate_on_submit():
        user = User.query.filter_by(email=forma.email.data).first()
        if user and bcrypt.check_password_hash(user.password, forma.password.data):
            login_user(user, remember=forma.remember.data)
            next_page = request.args.get('next')
            flash('Bienvenido de vuelta!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboardPrincipal'))
        else:
            flash('Correo o contraseña errados. Revise los datos', 'danger')
    return render_template('iniciarSesion.html', forma=forma, titulo='Inicio Sesión')


@app.route('/preguntas/nueva', methods=['GET', 'POST'])
@login_required
def nuevaPregunta():
    forma = CreateQuestionForm()
    if forma.validate_on_submit():
        status = True if forma.estatus.data == 'Resuelta' else False
        pregunta = Pregunta(titulo=forma.titulo.data, contenido=forma.contenido.data, etiquetas=forma.tema.data, resuelta=status, likes=0, user_id=current_user.id)
        db.session.add(pregunta)
        db.session.commit()
        flash('Tu pregunta se ha creado!', 'success')
        return redirect(url_for('dashboardPrincipal'))
    return render_template('nuevaPregunta.html', forma=forma, titulo='Nueva Pregunta', legenda='¿Qué duda tienes?')


@app.route('/preguntas/<int:preg_id>', methods=['GET','POST'])
@login_required
def pregunta(preg_id):
    pregunta = Pregunta.query.get_or_404(preg_id)
    # Implementación E:D
    comentariosPregunta = SLL_Stack()
    for comentario in pregunta.comentarios:
        comentariosPregunta.push(comentario)

    # Tamaño del arreglo de comentarios
    size = 0
    current = comentariosPregunta.getHead()
    while current:
        current = current.getNext()
        size += 1
    return render_template('pregunta.html', titulo=Pregunta.titulo, pregunta=pregunta, comentarios=comentariosPregunta, size=size)


@app.route('/preguntas/<int:preg_id>/actualizar', methods=['GET', 'POST'])
@login_required
def actualizarPregunta(preg_id):
    pregunta = Pregunta.query.get_or_404(preg_id)
    if pregunta.autor != current_user:
        abort(403)
    forma = CreateQuestionForm()
    if forma.validate_on_submit():
        pregunta.titulo = forma.titulo.data
        pregunta.contenido = forma.contenido.data
        pregunta.etiquetas = forma.tema.data
        pregunta.resuelta = True if forma.estatus.data == 'Resuelta' else False
        db.session.commit()
        flash('Actualizamos tu pregunta', 'success')
        return redirect(url_for('pregunta', preg_id=pregunta.id))
    elif request.method == 'GET':
    # Llenar la forma con los datos actuales
        forma.titulo.data = pregunta.titulo
        forma.contenido.data =pregunta.contenido
        forma.tema.data = pregunta.etiquetas
        forma.estatus.data = pregunta.resuelta
        return render_template('nuevaPregunta.html', forma=forma, titulo='Acualizar Pregunta',
        legenda='Cambia tu pregunta')


@app.route('/preguntas/<int:preg_id>/eliminar', methods=['POST'])
@login_required
def eliminarPregunta(preg_id):
    pregunta = Pregunta.query.get_or_404(preg_id)
    if pregunta.autor != current_user:
        abort(403)
    db.session.delete(pregunta)
    db.session.commit()
    flash('Hemos eliminado tu pregunta!', 'success')
    return redirect(url_for('dashboardPrincipal'))


@ app.route('/like/pregunta/<int:preg_id>', methods=['GET', 'POST'])
def likePregunta(preg_id):
    pregunta = Pregunta.query.filter_by(id=preg_id).first()
    pregunta.likes = pregunta.likes + 1
    db.session.commit()
    return redirect(url_for('pregunta', preg_id=pregunta.id))

@app.route('/comentarios/<int:com_id>', methods=['GET', 'POST'])
@login_required
def comentario(com_id):
    comentario = Comentario.query.get_or_404(com_id)
    return render_template('comentario.html', titulo='Comentario', comentario=comentario)


@app.route('/comentarios/nuevo/<int:preg_id>', methods=['GET', 'POST'])
@login_required
def postComentario(preg_id):
    forma = CreateCommentForm() 
    if forma.validate_on_submit():
        comentario = Comentario(contenido=forma.contenido.data, likes=0, util=False, pregunta_id=preg_id, user_id=current_user.id)
        db.session.add(comentario)
        db.session.commit()
        flash('Tu comentario se ha creado!', 'success')
        return redirect(url_for('pregunta', preg_id=comentario.pregunta_id))
    return render_template('nuevoComentario.html', forma=forma, titulo='Nuevo Comentario')


@app.route('/comentarios/<int:com_id>/actualizar', methods=['GET','POST'])
@login_required
def actualizarComentario(com_id):
    comentario = Comentario.query.get_or_404(com_id)
    if comentario.autor != current_user:
        abort(403)
    forma = CreateCommentForm()
    if forma.validate_on_submit():
        comentario.contenido = forma.contenido.data
        db.session.commit()
        flash('Actualizamos tu comentario', 'success')
        return redirect(url_for('pregunta', preg_id=comentario.pregunta_id))
    elif request.method == 'GET':
        # Llenar la forma con los datos actuales
        forma.contenido.data = comentario.contenido
        return render_template('nuevoComentario.html', forma=forma, titulo='Acualizar comentario',
                               legenda='Cambia tu comentario')


@app.route('/comentarios/<int:com_id>/eliminar', methods=['GET', 'POST'])
@login_required
def eliminarComentario(com_id):
    comentario = Comentario.query.get_or_404(com_id)
    if comentario.autor != current_user:
        abort(403)
    db.session.delete(comentario)
    db.session.commit()
    flash('Hemos eliminado tu comentario!', 'success')
    return redirect(url_for('pregunta', preg_id=comentario.pregunta_id))


@ app.route('/like/comentario/<int:com_id>', methods=['GET','POST'])
def likeComentario(com_id):
    comentario = Comentario.query.filter_by(id=com_id).first()
    comentario.likes = comentario.likes + 1
    db.session.commit()
    return redirect(url_for('pregunta', preg_id=comentario.pregunta_id))

@app.route('/busqueda', methods=['GET', 'POST'])
def busqueda():
    formaTexto = BusquedaTexto()
    formaEtiqueta = BusquedaTag()
    # Busqueda por texto
    if formaTexto.validate_on_submit():
        query = formaTexto.textoBusqueda.data
        page = request.args.get('page', default=1, type=int)
        preguntas = Pregunta.query.filter(Pregunta.titulo.contains(
        query) | Pregunta.contenido.contains(query)).paginate(page=page, per_page=10)
        return render_template('resultados.html', titulo='Resultados Busqueda', preguntas=preguntas)
    # Verificacion etiquetas
    if formaEtiqueta.validate_on_submit():
        tags = ["Artes","Ciencias","Ciencias Agrarias","Ciencias Economicas","Ciencias Humanas","Derecho, Ciencias Políticas y Sociales","Enfermeria","Ingenieria","Medicina","Medicina Veterinaria y de Zootecnia","Odontologia"]
        if formaEtiqueta.textoEtiqueta.data not in tags:
            rabinKarpMatcher = RabinKarpMatcher()
            matches = rabinKarpMatcher.compareToTags(formaEtiqueta.textoEtiqueta.data)
            try:
                query = matches[0]
            except:
                return render_template('resultados.html', titulo='Resultados Busqueda', preguntas=None)

            page = request.args.get('page', default=1, type=int)
            preguntas = Pregunta.query.filter(Pregunta.etiquetas.contains(
                query)).paginate(page=page, per_page=10)
            return render_template('resultados.html', titulo='Resultados Busqueda', preguntas=preguntas)
        else:
            query = formaEtiqueta.textoEtiqueta.data
            page = request.args.get('page', default=1, type=int)
            preguntas = Pregunta.query.filter(Pregunta.etiquetas.contains(
                query)).paginate(page=page, per_page=10)
            return render_template('resultados.html', titulo='Resultados Busqueda', preguntas=preguntas)
        
    
    return render_template('buscar.html', titulo='Buscar', formaTexto=formaTexto, formaEtiqueta=formaEtiqueta)
    

@ app.route('/cerrar_sesion', methods=['GET', 'POST'])
def cerrarSesion():
    logout_user()       
    return redirect(url_for('iniciarSesion'))

@app.route('/usuario/preguntas')
def misPreguntas():
    page = request.args.get('page', default=1, type=int)
    user = User.query.filter_by(id=current_user.id).first_or_404()
    preguntas = Pregunta.query.filter_by(autor=user).paginate(page=page, per_page=10)
    print(preguntas)
    return render_template('userQuestions.html', titulo='Inicio', preguntas=preguntas)
