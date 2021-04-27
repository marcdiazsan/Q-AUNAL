from Preguntas import *
from Comentarios import *
from DoubleLinkedList import DLL_Stack
from Arrays import Array_Stack
from LinkedList import SLL_Stack
import json
from datetime import datetime
arrays = False


class Stack(DLL_Stack):

    def __init__(self, size=None):
        # crea la estructura que se quiera o necesite

        if arrays:
            super().__init__(size)
        else:
            super().__init__()

    def creacion(self, dic):
        for i in dic.keys():
            item = Pregunta(dic[i]['preg_id'], dic[i]['titulo'], dic[i]['texto'], dic[i]['date'], dic[i]
                            ['tema'], dic[i]['userid'], dic[i]['likes'], dic[i]['comments'], dic[i]['estatus'])
            super().push(item)

    def insercion(self, item, comment=False, idPregunta=None):
        addition = False

        if not comment:
            if arrays:
                if super().full():
                    tmp = super().getArray()
                    newArray = [None] * (super().getSize() + 1)
                    newArray[:len(tmp)] = tmp
                    super.setArray(newArray)
            super().push(item)
            addition = True

        else:
            pregunta = self.buscarId(idPregunta)

            if arrays:
                if pregunta.getComentariosPregunta().full():
                    tmp = pregunta.getComentariosPregunta().getArray()
                    newArray = [None] * \
                        (pregunta.getComentariosPregunta().getSize() + 1)
                    newArray[:len(tmp)] = tmp
                    pregunta.getComentariosPregunta().setArray(newArray)
            # Crea el comentario
            id_com = str(idPregunta) + "." + \
                str(pregunta.getComentariosPregunta().count()+1)
            nuevoComentario = Comentario(ide=id_com, texto=item['texto'], fechaHora=datetime.now(), idUsuario=item['userid'],
                                         likes=0, utilidad=False, idPregunta=idPregunta)
            pregunta.getComentariosPregunta().push(nuevoComentario)
            addition = True

        return addition

    def buscarId(self, key):
        encontrado = None
        #tmp = DLL_Stack()
        item = super().getTop()
        while item != None:
            # print(item.getData().getId())
            # tmp.push(item)
            if item.getData().getId() == key:
                encontrado = item.getData()
                break
            item = item.getNext()
        '''
        while tmp.count() != 0:
            item = tmp.pop()
            super().push(item)
        '''
        return encontrado

    def eliminar(self, key, comment=False, idPregunta=None):
        deleted = False
        temp = DLL_Stack()
        if not comment:
            if super().getTop() == None:
                return None
            else:
                deleted = super().erase(key)
                '''
                while super().count() != 0:
                    if super().getTop().getData().getId() == key:
                        super().pop()
                        deleted=True
                        break
                    else:
                        a=super().pop()
                        temp.push(a)
                for j in range(0,temp.count()):
                    a=temp.pop()
                    super().push(a)
                '''
        else:
            pregunta = self.buscarId(idPregunta)
            # deleted=pregunta.getComentariosPregunta().erase(key)
            # print(pregunta.getComentariosPregunta().count())
            # deleted=pregunta.getComentariosPregunta().erase(key)
            # print(key)

            while pregunta.getComentariosPregunta().count() != 0:
                item = pregunta.getComentariosPregunta().pop()
                temp.push(item)
            while temp.count() != 0:
                item = temp.pop()
                if item.getId() == key:
                    deleted = True
                    pass
                else:
                    pregunta.getComentariosPregunta().push(item)

        return deleted

    def buscar(self, termino):
        '''

        encontrado = None
        #tmp = DLL_Stack()
        item = super().getTop()
        while self.count() != 0:
            # print(item.getData().getId())
            # tmp.push(item)
            if item.getData().getId() == key:
                encontrado = item.getData()
                break
            item = item.getNext()
        '''

        encontrado = None

        tmp = DLL_Stack()

        elementos = DLL_Stack()
        item = super().getTop()

        while item != None:
            #item = super().pop()
            # tmp.push(item)
            if termino.lower() in item.getData().getTituloPregunta().lower() or termino.lower() in item.getData().getTemaPregunta().lower():
                encontrado = item
                elementos.push(item)
            item = item.getNext()
       # while tmp.count() != 0:
        #    item = tmp.pop()
         #   super().push(item)

        return elementos

# La entrada cambios es tipo diccionario
    def actualizar(self, id, cambios, idPregunta=None, titulo=False, texto=True, tema=False, utilidad=False,
                   likes=False, comentario=False):
        tmp = DLL_Stack()

        actualizado = False
        if not comentario:
            pregunta = self.buscarId(id)

            if cambios['titulo']:
                pregunta.setTituloPregunta(cambios['titulo'])
                actualizado = True
            if cambios['texto']:
                pregunta.setTextoPregunta(cambios['texto'])
                actualizado = True
            if cambios['tema']:
                pregunta.setTemaPregunta(cambios['tema'])
                actualizado = True

            if cambios['likes']:
                numero = pregunta.getLikesPregunta()
                pregunta.setLikesPregunta(numero + 1)
                actualizado = True

        else:
            pregunta = self.buscarId(idPregunta)
            while pregunta.getComentariosPregunta().count() != 0:
                item = pregunta.getComentariosPregunta().pop()
                tmp.push(item)
            while tmp.count() != 0:
                item = tmp.pop()
                if item.getId() == id:
                    if texto:
                        item.setTextoComentario(cambios['texto'])
                        actualizado = True
                    if utilidad:
                        item.setUtilidadComentario(cambios['utilidad'])
                        actualizado = True
                    if likes:
                        numero = pregunta.getLikesComentario()
                        item.setLikesComentario(numero + 1)
                        actualizado = True

                pregunta.getComentariosPregunta().push(item)
        return actualizado

    def consultaTotal(self):
        tmp = DLL_Stack()

        data = {}
        while super().count() != 0:
            item = super().pop()
            data[item.getId()] = item.toJSON()
            tmp.push(item)

        while tmp.count() != 0:
            item = tmp.pop()
            super().push(item)

        return data

    def almacenamiento(self, fileName):
        #tmp = DLL_Stack()
        item = super().getTop()
        data = {}
        while item != None:
         #   item = super().pop()
            data[item.getData().getId()] = item.getData().toJSON()
            item = item.getNext()
            # tmp.push(item)

        # while tmp.count() != 0:
         #   item = tmp.pop()
          #  super().push(item)

        JSONData = open(fileName, 'w')
        JSONData.write(json.dumps(data))
        JSONData.close()

        return True
