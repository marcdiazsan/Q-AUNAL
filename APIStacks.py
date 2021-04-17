from flask import Flask, jsonify, request
import json
import time
from Preguntas import *
from Comentarios import *
from FunctionalQueue import FunctionalQueue
from Encolador import Encolador
from Stack import Stack


app = Flask(__name__)


# Encolar todos los datos una vez se inicie la app
encolador = Encolador()


@app.route('/preguntas', methods=['GET'])
def getPreguntas():
    if request.method == 'GET':
        # Crea un diccionario para mostrar los datos
        renderDict = {}
        # Inicia el contador
        s = time.time()
        # Instancia la estructura a usar
        estructura = encolador.enpilar(10000)
        # Detiene el contador
        e = time.time()
        print("10k datos enpilados en {}s".format(e-s))
        # Inicia el contador / Cuanto toma mostrarlos
        s = time.time()
        for i in range(estructura.count()):
            pregunta = estructura.pop()
            renderDict[pregunta.getId()] = pregunta.toJSON()
        e = time.time()
        # Detiene el contador
        print("10k datos renderizados en {}s".format(e-s))
    return jsonify(renderDict)


# Obtener una pregunta por su identificador (Uso colas-pilas)
@app.route('/preguntas/<string:preg_text>', methods=['GET'])
def getPregunta(preg_text):
    if request.method == 'GET':
        s = time.time()
        estructura = encolador.enpilar(10000)
        e = time.time()
        print("10k datos enpilados en {}s".format(e-s))
        # Buscar el elementos
        s = time.time()
        pregunta = estructura.buscar(preg_text)
        e = time.time()
        if pregunta != None:
            print("Objeto encontrado en {}s".format(e-s))
            return jsonify(pregunta.toJSON())
        else:
            print("La pregunta con texto: {}, no existe".format(preg_text))
            return jsonify("No se encontró el item solicitado")


# Si el request es de tipo POST
@app.route('/preguntas/nueva', methods=['GET', 'POST'])
def nuevaPregunta():
    if request.method == 'POST':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Encola los datos
        estructura = encolador.enpilar(10000)
        # Solicita la creación de la pregunta en la cola
        # Inicia el temporizador
        s = time.time()
        estructura.creacion(requestData)
        e = time.time()
        # Informa el tiempo
        print("Objeto creado en {} segundos".format(e-s))
        # Guarda al archivo
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print("Archivo JSON escrito en {}".format(e-s))
        # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Pregunta creada y guardada"
    else:
        return "Sitio para crear pregunta"

# Si se quiere actualizar una pregunta


@app.route('/preguntas/actualizar/<int:preg_id>', methods=['PUT', 'DELETE'])
def actualizarPregunta(preg_id):
    # Encola los datos
    estructura = encolador.enpilar(10000)
    # Por ahora busca la pregunta en el archivo
    if request.method == 'PUT':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Inicia el diccionario de cambios
        cambios = {
            'titulo': requestData.get('titulo', None),
            'texto': requestData.get('texto', None),
            'tema': requestData.get('tema', None),
            'likes': requestData.get('likes', None)
        }
        s = time.time()
        estructura.actualizar(id=preg_id, cambios=cambios)
        e = time.time()
        print("Valor actualizado en {}s".format(e-s))
        e = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        s = time.time()
        print("Actualización a JSON en {}".format(e-s))
        return "Valor actualizado en {}s".format(e-s)

    elif request.method == 'DELETE':
        # Inicia el contador
        s = time.time()
        # Elimina el objeto
        estructura.eliminar(idPregunta=preg_id, key=preg_id)
        # Detiene el contador
        e = time.time()
        # Guarda los datos
        estructura.almacenamiento('JSON10MILData.json')
        return 'Valor {} eliminado en {}s'.format(preg_id, e-s)

    else:
        return "Sitio para crear pregunta"


# Obtener todos los comentarios disponibles
@ app.route('/comentarios')
def getComentarios():
    if request.method == 'GET':
        # Crea un diccionario para mostrar los datos
        renderDict = {}
        # Instancia la estructura a usar
        estructura = encolador.enpilar(10000)
        # Instancia una cola para los comentarios
        estructura_com = Stack()
        # Encola todos los comentarios
        # Inicia el contador
        s = time.time()
        for i in range(estructura.count()):
            pregunta = estructura.pop()
            estructura_com.push(pregunta.getComentariosPregunta())
        # Detiene el contador
        e = time.time()
        print("Datos enpilados en {}s".format(e-s))

        # Desencola los comentarios
        s = time.time()
        for i in range(estructura_com.count()):
            SLL_Comentarios = estructura_com.pop()
            for j in range(SLL_Comentarios.count()):
                comentario = SLL_Comentarios.pop()
                renderDict[comentario.getId()] = comentario.toJSON()
        # Detiene el contador
        e = time.time()
        print("10k datos enpilados en {}s".format(e-s))
    return jsonify(renderDict)


# Obtener un comentario por su id
@ app.route('/comentarios/<int:com_id>')
def getComentario(com_id):
    if request.method == 'GET':
        # Instancia la estructura a usar
        estructura = encolador.enpilar(10000)
        # Instancia una cola para los comentarios
        estructura_com = Stack()
        # Encola todos los comentarios
        # Inicia el contador
        s = time.time()
        for i in range(estructura.count()):
            pregunta = estructura.pop()
            questionComments = pregunta.getComentariosPregunta()
            for j in range(questionComments.count()):
                comentario = questionComments.pop()
                estructura_com.push(comentario)
        # Detiene el contador
        e = time.time()
        print("Datos enpilados en {}s".format(e-s))

        # Busca el comentario
        s = time.time()

        busqueda = estructura_com.buscarId(com_id)
        # Detiene el contador
        e = time.time()
        if busqueda != None:
            print("Objeto encontrado en {}s".format(e-s))
            return jsonify(busqueda.toJSON())
        else:
            return jsonify("Objeto no encontrado")

    return ""

# Enviar un nuevo comentario


@ app.route('/comentarios/nuevo/<int:preg_id>', methods=['GET', 'POST'])
def postComentario(preg_id):
    if request.method == 'POST':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Encola los datos
        estructura = encolador.enpilar(10000)
        # Solicita la creación de un nuevo comentario
        # Inicia el temporizador
        s = time.time()
        estructura.insercion(requestData, comment=True, idPregunta=preg_id)
        e = time.time()
        print(f"Objeto insertado en {e-s}")
        # Guarda al archivo
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f'Objeto guardado en {e-s}')
        # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Hemos guardado tu comentario"
    else:
        return "Sitio para crear pregunta"


# Si se quiere Actualizar/Borrar una pregunta
@ app.route('/comentarios/actualizar/<int:preg_id>/<int:com_id>', methods=['POST', 'PUT', 'DELETE'])
def actualizarComentario(preg_id, com_id):
    # Encola los datos
    estructura = encolador.enpilar(10000)
    # Por ahora busca la pregunta en el archivo
    if request.method == 'PUT':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Inicia el diccionario de cambios
        cambios = {
            'texto': requestData.get('texto', None),
            'likes': requestData.get('likes', None),
            'utilidad': requestData.get('utilidad', None)
        }
        s = time.time()
        estructura.actualizar(id=com_id,
                              cambios=cambios, idPregunta=preg_id, comentario=True)

        e = time.time()
        print(f"Comentario actualizado en {e-s}")
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f'Datos guardados en {e-s}')
        return 'Valor actualizado'

    elif request.method == 'DELETE':
        # Inicia el contador
        s = time.time()
        # Elimina el objeto
        estructura.eliminar(idPregunta=preg_id, key=int(
            str(preg_id)+str(com_id)), comment=True)
        # Detiene el contador
        e = time.time()
        print(f"Valor {com_id} eliminado en {e-s}s")
        # Guarda los datos
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f'Valor guardado en {e-s}s')
        return "Dato Eliminado"


if __name__ == '__main__':
    app.run(debug=True)
