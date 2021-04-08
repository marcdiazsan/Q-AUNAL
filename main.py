from flask import Flask, jsonify, request
from dataScrambler import DataCreator
import json
from Pregunta import Pregunta
from Comentario import Comentario

app = Flask(__name__)

data = open("JSONData.json", "r")
preguntas = data.readlines()
data.close()

@app.route('/preguntas')
def getPreguntas():
    if request.method == 'GET':
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json') as data:
            apiData = json.loads(data.read())

        return jsonify(apiData)

# Obtener una pregunta por su identificador (Uso colas-pilas)
@app.route('/preguntas/<int:preg_id>', methods=['GET', 'POST'])
def getPregunta(preg_id):
    if request.method == 'GET':
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json') as data:
            apiData = json.load(data)
        # Itera sobre los datos que se trajeron (Eventualmente los datos se guardan en colas)
        for pregunta_id in apiData:
            pregunta = apiData[pregunta_id]
            # Si encuentra el identificador devuelve el contenido de esa pregunta
            if pregunta['preg_id'] == preg_id:
                return jsonify(pregunta)
        # Si no lo encuentra le informa al usuario que no lo halló
        return jsonify("No se encontró el item solicitado")


# Si el request es de tipo POST
@app.route('/preguntas/nueva', methods=['GET', 'POST'])    
def nuevaPregunta():
    if request.method == 'POST':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Crea un objeto de pregunta a partir de esos datos
        newPregunta = Pregunta(preg_id=requestData['preg_id'], titulo=requestData['titulo'], contenido=requestData['texto'], tema=requestData['tema'], userid=requestData['user_id'])
        with open("JSONData.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            data.update(newPregunta.toJSON())
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()
        # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Created object in DB with \n{}".format(newPregunta.toJSON())
    else:
        return "Sitio para crear pregunta"

# Si se quiere actualizar una pregunta
@app.route('/preguntas/actualizar/<int:preg_id>', methods=['POST', 'PUT'])
def actualizarPregunta(preg_id):
    # Por ahora busca la pregunta en el archivo
    if request.method == 'POST' or request.method == 'PUT':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json') as data:
            apiData = json.load(data)
        # Itera sobre los datos que se trajeron (Eventualmente los datos se guardan en colas)
        for pregunta_id in apiData:
            pregunta = apiData[pregunta_id]
            # Si encuentra el identificador devuelve el contenido de esa pregunta
            if pregunta['preg_id'] == preg_id:  
                # Crea un objeto de pregunta a partir de esos datos
                newPregunta = Pregunta(preg_id=preg_id, titulo=requestData['titulo'], contenido=requestData['texto'], tema=requestData['tema'], userid=requestData['user_id'], comments=pregunta['comments'])
                # Actualiza los datos en la base de datos o en el JSON (?)
                with open("JSONData.json", "r+") as jsonFile:
                    data = json.load(jsonFile)
                    data[preg_id] = newPregunta.toJSON()
                    jsonFile.seek(0)  # rewind
                    json.dump(data, jsonFile)
                    jsonFile.truncate()
                # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
                return "Created object in DB with \n{}".format(newPregunta.toJSON())
    else:
        return "Sitio para crear pregunta"

# Si se quiere actualizar una pregunta
@app.route('/preguntas/eliminar/<int:preg_id>', methods=['GET', 'DELETE'])
def eliminarPregunta(preg_id):
    # Por ahora busca la pregunta en el archivo
    if request.method == 'GET' or request.method == 'DELETE':
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json') as data:
            apiData = json.load(data)
        # Itera sobre los datos que se trajeron (Eventualmente los datos se guardan en colas)
        for pregunta_id in apiData:
            pregunta = apiData[pregunta_id]
            print(pregunta)
            print()
            # Si encuentra el identificador devuelve el contenido de esa pregunta
            if pregunta['preg_id'] == preg_id:  
                with open("JSONData.json", "r+") as jsonFile:
                    data = json.load(jsonFile)
                    data.pop(str(preg_id))
                    jsonFile.seek(0)  # rewind
                    json.dump(data, jsonFile)
                    jsonFile.truncate()
                # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Objeto con ID {} Eliminado".format(preg_id)
    else:
        return "Eliminando Pregunta"
        
# Obtener todos los comentarios disponibles
@app.route('/comentarios')
def getComentarios():
    if request.method == 'GET':
        renderDict = {}
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json') as data:
            apiData = json.loads(data.read())
        # Para cada identificador obtiene los comentarios y los guarda en un diccionario
        for pregunta_id in apiData:
            pregunta = apiData[pregunta_id]
            comentarios = pregunta['comments']
            renderDict[pregunta_id] = comentarios
        return jsonify(renderDict)

# Obtener un comentario por su id
@app.route('/comentarios/<int:com_id>')
def getComentario(com_id):
    if request.method == 'GET':
        renderDict = {}
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json') as data:
            apiData = json.loads(data.read())
        # Para cada identificador obtiene los comentarios y los guarda en un diccionario
        for pregunta_id in apiData:
            pregunta = apiData[pregunta_id]
            comentarios = pregunta['comments']
            for comentario in comentarios:
                print(comentario)
                print('\n')
                if comentario['com_id'] == str(com_id):
                    renderDict[com_id] = comentario
        return jsonify(renderDict)

# Enviar un nuevo comentario
@app.route('/comentarios/nuevo/<int:preg_id>', methods=['GET', 'POST'])
def postComentario(preg_id):
    if request.method == 'POST':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        print(requestData)
        # Se busca la pregunta para añadir el comentario a los comentarios
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json', "r+") as data:
            apiData = json.load(data)
            # Itera sobre los datos que se trajeron (Eventualmente los datos se guardan en colas)
            for pregunta_id in apiData:
                pregunta = apiData[pregunta_id]
                # Si encuentra el identificador devuelve el contenido de esa pregunta
                if pregunta['preg_id'] == preg_id:
                    # Crea un objeto de pregunta a partir de esos datos
                    newComentario = Comentario(preg_id=requestData['preg_id'], texto=requestData['texto'], user_id=requestData['user_id'], com_id=str(preg_id) + str(len(pregunta['comments']+1)))
                    # La añade a las preguntas
                    pregunta['comments'].append(newComentario.toJSON())
                    # Lo escribe al archivo (Eventualmente una base de datos)
                    data.seek(0)  # rewind
                    json.dump(apiData, data)
                    data.truncate()
                    break
        # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
        return "Created object in DB with \n{}".format(newComentario.toJSON())

    return "No se pudo crear el objeto, revise sus parametros."


# Si se quiere Actualizar/Borrar una pregunta
@app.route('/comentarios/actualizar/<int:preg_id>/<int:com_id>', methods=['POST', 'PUT', 'DELETE'])
def actualizarComentario(preg_id, com_id):
    # Por ahora busca la pregunta en el archivo
    if request.method == 'POST' or request.method == 'PUT':
        # Solicita los datos del request (Eventualmente van a venir de una forma)
        requestData = request.get_json()
        # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
        with open('JSONData.json', "r+") as data:
            apiData = json.load(data)
            # Itera sobre los datos que se trajeron (Eventualmente los datos se guardan en colas)
            for pregunta_id in apiData:
                pregunta = apiData[pregunta_id]
                # Si encuentra el identificador devuelve el contenido de esa pregunta
                if pregunta['preg_id'] == preg_id:  
                    for comentario in pregunta['comments']:
                        if str(comentario['com_id']) == str(com_id):
                            # Crea un objeto de pregunta a partir de esos datos
                            updateComentario = Comentario(preg_id=preg_id, texto=requestData['texto'], user_id=comentario['userid'], com_id=com_id, numlikes=comentario['likes'])
                            # Remueve el comentario previo
                            pregunta['comments'].remove(comentario)
                            # La añade a las preguntas
                            pregunta['comments'].append(updateComentario.toJSON())
                            # Lo escribe al archivo (Eventualmente una base de datos)
                            data.seek(0)  
                            json.dump(apiData, data)
                            data.truncate()
                            # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
                            return "Created object in DB with \n{}".format(updateComentario.toJSON())
                            break
        return "Unable to Create Object"
    elif request.method=='DELETE':
        # Por ahora busca la pregunta en el archivo
        if request.method == 'POST' or request.method == 'DELETE':
            # Solicita los datos del request (Eventualmente van a venir de una forma)
            requestData = request.get_json()
            # Abre el archivo de los datos (Eventualmente esto va a leer de una base de datos)
            with open('JSONData.json', "r+") as data:
                apiData = json.load(data)
                # Itera sobre los datos que se trajeron (Eventualmente los datos se guardan en colas)
                for pregunta_id in apiData:
                    pregunta = apiData[pregunta_id]
                    # Si encuentra el identificador devuelve el contenido de esa pregunta
                    if pregunta['preg_id'] == preg_id:  
                        for comentario in pregunta['comments']:
                            if str(comentario['com_id']) == str(com_id):
                                # Remueve el comentario previo
                                pregunta['comments'].remove(comentario)
                                data.seek(0)  
                                json.dump(apiData, data)
                                data.truncate()
                                # Muestra el objeto creado. Eventualmente, el objeto se añade a una cola de preguntas
                                return "Clear 200"
                                break
            return "Unable to Delte Object"
    else:
        return abort(404)
        


if __name__=='__main__':
    app.run(debug=True)
