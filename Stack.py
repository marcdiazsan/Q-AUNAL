from Preguntas import *
from Comentarios import *
from DoubleLinkedList import DLL_Stack
from Arrays import Array_Stack
from LinkedList import SLL_Stack
import json

class Stack(DLL_Stack):
    def __init__(self):
        super().__init__()

    def creacion(self,dic):
        for i in dic.keys():
            item=Pregunta(dic[i]['preg_id'],dic[i]['titulo'],dic[i]['texto'],dic[i]['date'],dic[i]['tema'],dic[i]['userid'],dic[i]['likes'],dic[i]['comments'],dic[i]['estatus'])
            super().push(item)

    def insercion(self,item,comment = False, idPregunta = None):
        addition = False

        if not comment:
            super().push(item)
            addition = True

        else:
            pregunta = self.buscarId(idPregunta)
            pregunta.getComentariosPregunta().push(item)
            addition = True

        return addition

    def buscarId(self, key):
        encontrado = None
        tmp = DLL_Stack()
        while self.count() != 0:
            item = self.pop()
            tmp.push(item)
            if item.getId() == key:
                encontrado = item
        while tmp.count() != 0:
            item = tmp.pop()
            super().push(item)
        return encontrado

    def eliminar(self, key, comment = False, idPregunta = None):
        deleted = False
        temp = DLL_Stack()
        if not comment:
            if super().getTop()==None:
                return None
            else:
                while super().count() != 0:
                    if super().getTop().getData().getId() == key:
                        super().pop()
                        break
                    else:
                        a=super().pop()
                        temp.push(a)
                for j in range(0,temp.count()):
                    a=temp.pop()
                    super().push(a)
        else:
            pregunta=self.buscarId(idPregunta)
            while pregunta.getComentariosPregunta().count() != 0:
                if pregunta.getComentariosPregunta().getTop().getData().getId() == key:
                    pregunta.getComentariosPregunta().pop()
                    deleted = True
                    break
                else:
                    a=pregunta.getComentariosPregunta().pop()
                    temp.push(a)
                for i in range(0,temp.count()):
                    a=temp.pop()
                    super().push(a)
        return deleted


    def buscar(self,termino):
        encontrado = None

        tmp = DLL_Stack()

        elementos = DLL_Stack()

        while super().count() != 0:
            item = super().pop()
            tmp.push(item)
            if termino.lower() in item.getTituloPregunta().lower() or termino.lower() in item.getTemaPregunta().lower():
                encontrado = item
                elementos.push(item)
        while tmp.count() != 0:
            item = tmp.pop()
            super().push(item)

        return encontrado

#La entrada cambios es tipo diccionario
    def actualizar(self, id, cambios, idPregunta=None, titulo=False, texto=True, tema=False, utilidad=False,
                   likes=False, comentario=False):
        tmp = DLL_Stack()

        actualizado = False
        if not comentario:
            pregunta = self.buscarId(id)

            if titulo:
                pregunta.setTituloPregunta(cambios['titulo'])
                actualizado = True
            if texto:
                pregunta.setTextoPregunta(cambios['texto'])
                actualizado = True
            if tema:
                pregunta.setTemaPregunta(cambios['tema'])
                actualizado = True

            if likes:
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

    def almacenamiento(self):
        tmp = DLL_Stack()

        data = {}
        while super().count() != 0:
            item = super().pop()
            data[item.getId()] = item.toJSON()
            tmp.push(item)

        while tmp.count() != 0:
            item = tmp.pop()
            super().push(item)

        JSONData = open('JSONDataTotal.json', 'w')
        JSONData.write(json.dumps(data))
        JSONData.close()

        return True

q=Stack()

with open('JSON10MILData.json') as data:
    apiData = json.loads(data.read())

q.creacion(apiData)
print(q.buscar('artes'))
c={'texto':'Test Update'}
q.eliminar(998)
print(q.actualizar(3,c, texto= True))
q.almacenamiento()
print(q.consultaTotal())

'''
print("hola")
a=[1,2,3,4,5,6,7,8]
k= Stack()
for i in a:
    k.insercion(i)
#print(k.count())
k.printList()
print("hola")
k.remove(7)
k.remove(1)
k.remove(8)
#temp= Stack()
#temp.insercion(k.getFirst())
k.printList()
#print(k.count())
#print(k.getHead().getNext().getData())
'''