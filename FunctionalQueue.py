from Arrays import Array_Queue
from LinkedList import SLL_Queue
from Preguntas import Pregunta
from Comentarios import Comentario
import json

from DoubleLinkedList import DLL_Queue


#al cambiar por colas con array Array_Queue o listas doblemente enlazada, se cambia todo lo que tiene SLL_queue
class FunctionalQueue(SLL_Queue):
    
    def __init__(self):
        #crea la estructura que se quiera o necesite
        super().__init__()

    #creacion y llenado de la estructura de datos
    def creacion(self, dic):
        
        for key in dic.keys():
            item = Pregunta(dic[key]['preg_id'],dic[key]['titulo'],dic[key]['texto'],dic[key]['date'],dic[key]['tema'],dic[key]['userid'],dic[key]['likes'],dic[key]['comments'],dic[key]['estatus'])
            
            super().enqueue(item)
            
    #adicion de una pregunta o comentario a la estructura correspondiente      
    def insercion(self, item, comment = False, idPregunta = None):
        inserted = False

        if not comment:
            super().enqueue(item)
            inserted = True

        else:
            pregunta = self.buscarId(idPregunta)
            pregunta.getComentariosPregunta().enqueue(item)
            inserted = True

        return inserted
    
    #busqueda de preguntas por medio del Id          
    def buscarId(self, key):
        encontrado = None 
        tmp = SLL_Queue()
        while self.count() != 0:
            item = self.dequeue()
            tmp.enqueue(item)
            if item.getId() == key:
                encontrado = item
        while tmp.count() != 0:
            item = tmp.dequeue()
            super().enqueue(item)
        return encontrado

    #eliminacion de una pregunta o comentario de la estructura
    def eliminar(self, key, comment = False, idPregunta = None):
        deleted = False

        tmp = SLL_Queue()
        if not comment:
            while super().count() != 0:
                item = super().dequeue()
                if item.getId() != key:
                    tmp.enqueue(item)
            while tmp.count() != 0:
                item = tmp.dequeue()
                super().enqueue(item)


        else:
            pregunta = self.buscarId(idPregunta)
            while pregunta.getComentariosPregunta().count() != 0:
                item = pregunta.getComentariosPregunta().dequeue()
                tmp.enqueue(item)
            while tmp.count() != 0:
                item = tmp.dequeue()
                if int(item.getId()) == key:
                    deleted = True
                    pass
                else:
                    pregunta.getComentariosPregunta().enqueue(item)

        return deleted 
                
    #buscar una palabra dentro del titulo o tema     
    def buscar(self, word):
        encontrado = None

        tmp = SLL_Queue()

        elementos = SLL_Queue()
        #data={}
         
        while super().count() != 0:
            item = super().dequeue()
            tmp.enqueue(item)
            if word.lower() in item.getTituloPregunta().lower() or word.lower() in item.getTemaPregunta().lower():
                encontrado=item
                elementos.enqueue(item)
                #data[item.getId()] = item.toJSON()
        while tmp.count() != 0:
            item = tmp.dequeue()
            super().enqueue(item)

        return elementos

     
    #actualizacion de una pregunta o comentario   
    def actualizar(self, identificacion, cambios, idPregunta=None, titulo = False, texto = True, tema = False, utilidad = False, likes = False, comentario = False):
        tmp = SLL_Queue()
         
        actualizado = False
        if not comentario:
            pregunta = self.buscarId(identificacion)
            
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
                pregunta.setLikesPregunta(numero+1)
                actualizado = True

        else:
            pregunta = self.buscarId(idPregunta)
            while pregunta.getComentariosPregunta().count() != 0:
                item = pregunta.getComentariosPregunta().dequeue()
                tmp.enqueue(item)
            while tmp.count() != 0:
                item = tmp.dequeue()
                if int(item.getId()) == identificacion:
                    if texto:
                        item.setTextoComentario(cambios['texto'])
                        actualizado = True
                    if utilidad:
                        item.setUtilidadComentario(cambios['utilidad'])
                        actualizado=True
                    if likes:
                        numero = pregunta.getLikesComentario() 
                        item.setLikesComentario(numero+1)
                        actualizado = True
                         
                pregunta.getComentariosPregunta().enqueue(item)
        return actualizado

    #consulta total de las preguntas
    def consultaTotal(self):
        tmp = SLL_Queue()
         
        data={}
        while super().count() !=0:
            item = super().dequeue()
            data[item.getId()] = item.toJSON()
            tmp.enqueue(item)
             
        while tmp.count() !=0:
            item = tmp.dequeue()
            super().enqueue(item)


        return data

    #guarda en un archivo externo la estructura
    def almacenamiento(self):
        tmp = SLL_Queue()
         
        data={}
        while super().count() !=0:
            item = super().dequeue()
            data[item.getId()] = item.toJSON()
            tmp.enqueue(item)
             
        while tmp.count() !=0:
            item = tmp.dequeue()
            super().enqueue(item)

        JSONData = open('JSONDataTotal.json', 'w')
        JSONData.write(json.dumps(data))
        JSONData.close()

        return True
         
             
         
q=FunctionalQueue()

with open('JSONData.json') as data:
    apiData = json.loads(data.read())

q.creacion(apiData)
print(q.buscar('artes'))
c={'texto':'Test Update'}
q.eliminar(998)
print(q.buscar('artes'))
#print(q.actualizar(998,c, texto= True))

           
             

         
         
            
             
         

     

     
                     
         
         
         

        
        
        
