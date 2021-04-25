from flask import Flask, jsonify, request
import json
import time
from Preguntas import *
from Comentarios import *
from FunctionalQueue import FunctionalQueue
from Encolador import Encolador
from datetime import datetime
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
        estructura = encolador.enpilar()
        # Detiene el contador
        e = time.time()
        print("10k datos enpiladoss en {}s".format(e-s))
        # Inicia el contador / Cuanto toma mostrarlos
        s = time.time()
        renderDict = estructura.consultaTotal()
        e = time.time()
        # Detiene el contador
        print("10k datos desenpiladoss en {}s".format(e-s))
    return jsonify(renderDict)


# Obtener una pregunta por su identificador (Uso colas-pilas)
@app.route('/preguntas/<string:preg_text>', methods=['GET'])
def getPregunta(preg_text):
    if request.method == 'GET':
        renderDict = {}
        s = time.time()
        estructura = encolador.enpilar()
        e = time.time()
        print("10k datos enpiladoss en {}s".format(e-s))
        # Buscar el elementos
        s = time.time()
        pregunta = estructura.buscar(preg_text)
        e = time.time()
        if pregunta != None:
            print("Objeto encontrado en {}s".format(e-s))
            for i in range(pregunta.count()):
                tmp = pregunta.pop()
                renderDict[tmp.getData().getId()] = tmp.getData().toJSON()
            return jsonify(renderDict)
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
        estructura = encolador.enpilar()
        # Solicita la creación de la pregunta en la cola
        # Inicia el temporizador
        s = time.time()
        item = Pregunta(estructura.count()+1, requestData['titulo'], requestData['texto'], str(datetime.now()), requestData
                        ['tema'], requestData['userid'], 0, [], "Abierto")
        estructura.insercion(item)
        e = time.time()
        # Informa el tiempo
        print("Objeto creado en {} segundos".format(e-s))
        # Guarda al archivo
        estructura.almacenamiento('JSON10MILData.json')
        # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Pregunta creada y guardada"
    else:
        return "Sitio para crear pregunta"

# Si se quiere actualizar una pregunta


@app.route('/preguntas/actualizar/<int:preg_id>', methods=['PUT', 'DELETE'])
def actualizarPregunta(preg_id):
    # Encola los datos
    estructura = encolador.enpilar()
    # Por ahora busca la pregunta en el archivo
    if request.method == 'PUT':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        print(requestData, type(requestData))
        # Inicia el diccionario de cambios
        cambios = {
            'titulo': requestData.get('titulo', None),
            'texto': requestData.get('texto', None),
            'tema': requestData.get('tema', None),
            'likes': requestData.get('likes', None)
        }
        s = time.time()
        estructura.actualizar(id=preg_id,
                              cambios=cambios)
        e = time.time()
        print(f"Valor actualizado en {e-s}s")
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f'Valor guardado en {e-s}s')
        return "Valor actualizado"

    elif request.method == 'DELETE':
        # Inicia el contador
        s = time.time()
        # Elimina el objeto
        estructura.eliminar(key=preg_id)
        # Detiene el contador
        e = time.time()
        print(f"Valor eliminado en {e-s}s")
        # Guarda los datos
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f'Valor guardado en {e-s}s')
        return 'Valor eliminado'

    else:
        return "Sitio para crear pregunta"


# Obtener todos los comentarios disponibles
@ app.route('/comentarios')
def getComentarios():
    if request.method == 'GET':
        # Crea un diccionario para mostrar los datos
        renderDict = {}
        # Instancia la estructura a usar
        estructura = encolador.enpilar()
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
        print("Datos enpiladoss en {}s".format(e-s))

        # Desencola los comentarios
        s = time.time()
        for i in range(estructura_com.count()):
            SLL_Comentarios = estructura_com.pop()
            for j in range(SLL_Comentarios.count()):
                comentario = SLL_Comentarios.pop()
                renderDict[comentario.getId()] = comentario.toJSON()
        # Detiene el contador
        e = time.time()
        print("10k datos desenpiladoss en {}s".format(e-s))
    return jsonify(renderDict)


# Obtener un comentario por su id
@ app.route('/comentarios/<string:com_id>')
def getComentario(com_id):
    if request.method == 'GET':
        # Instancia la estructura a usar
        estructura = encolador.enpilar()
        # Instancia una cola para los comentarios
        estructura_com = FunctionalQueue()
        # Encola todos los comentarios
        # Inicia el contador
        s = time.time()
        for i in range(estructura.count()):
            pregunta = estructura.pop()
            if pregunta.getId() == int(com_id.split('.')[0]):
                questionComments = pregunta.getComentariosPregunta()
                for j in range(questionComments.count()):
                    comentario = questionComments.pop()
                    print(str(comentario.getId()).split('.')[1])
                    if int(str(comentario.getId()).split('.')[1]) == int(com_id.split('.')[1]):
                        busqueda = comentario
        # Detiene el contador
        e = time.time()
        print("Datos enpiladoss en {}s".format(e-s))

        # Busca el comentario
        s = time.time()

        # busqueda = estructura_com.buscarId(com_id)
        # Detiene el contador
        e = time.time()
        if busqueda != None:
            print("Objeto encontrado en {}s".format(e-s))
            return jsonify(busqueda.toJSON())
        else:
            print("Objeto no encontrado en {}s".format(e-s))
            return "No encontrado"

    return ""

# Enviar un nuevo comentario


@ app.route('/comentarios/nuevo/<int:preg_id>', methods=['GET', 'POST'])
def postComentario(preg_id):
    if request.method == 'POST':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Encola los datos
        estructura = encolador.enpilar()
        # Solicita la creación de un nuevo comentario
        # Inicia el temporizador
        s = time.time()
        estructura.insercion(requestData, comment=True, idPregunta=preg_id)
        e = time.time()
        print(f'Valor añadido en {e-s}s')
        # Guarda al archivo
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f'Valor guardado en {e-s}s')
        # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Objeto creado"
    else:
        return "Sitio para crear pregunta"


# Si se quiere Actualizar/Borrar una pregunta
@ app.route('/comentarios/actualizar/<int:preg_id>/<string:com_id>', methods=['POST', 'PUT', 'DELETE'])
def actualizarComentario(preg_id, com_id):
    # Encola los datos
    estructura = encolador.enpilar()
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
        print('Valor actualizado en {}s'.format(e-s))
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print('Valor guardado en {}s'.format(e-s))
        return "Valor actualizado!"

    elif request.method == 'DELETE':
        # Inicia el contador
        s = time.time()
        # Elimina el objeto
        estructura.eliminar(idPregunta=preg_id, key=com_id, comment=True)
        # Detiene el contador
        e = time.time()
        print(f"Valor eliminado en {e-s}")
        # Guarda los datos
        s = time.time()
        estructura.almacenamiento('JSON10MILData.json')
        e = time.time()
        print(f"Valor guardado en {e-s}s")
        return "Valor eliminado"


if __name__ == '__main__':
    app.run(debug=True)
