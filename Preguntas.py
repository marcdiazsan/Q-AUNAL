from LinkedList import SLL_Queue, SLL_Stack
from DoubleLinkedList import DLL_Stack, DLL_Queue
from Arrays import Array_Queue, Array_Stack
from Comentarios import *

arrays = False


class Pregunta:
    # Clase que describe una preguntas y sus atributos para el proyecto Q&A UNAL
    def __init__(self, identificador, titulo, texto, fechaHora, tema, idUsuario, likes, comentarios, estatus=False):
        self.__id = identificador
        self.__tituloPregunta = titulo
        self.__textoPregunta = texto
        self.__fechaHoraPregunta = fechaHora
        self.__temaPregunta = tema
        self.__idUsuarioPregunta = idUsuario
        self.__estatusPregunta = estatus
        self.__likesPregunta = likes

        # se crea la estructura de los comentarios (se cambia cuando se necesite)
        if arrays:
            coments = Array_Stack(len(comentarios))
        else:
            coments = SLL_Queue()

        for com in comentarios:

            comentario = Comentario(com['com_id'], com['texto'], com['date'], com['userid'], com['likes'], com['util'],
                                    com['preg_id'])

            # Para colas enqueue y para pilas push
            coments.enqueue(comentario)
        self.__comentarios = coments

    def setId(self, identificador):
        self.__id = identificador

    def getId(self):
        return self.__id

    def setTituloPregunta(self, titulo):
        self.__tituloPregunta = titulo

    def getTituloPregunta(self):
        return self.__tituloPregunta

    def setTextoPregunta(self, texto):
        self.__textoPregunta = texto

    def getTextoPregunta(self):
        return self.__textoPregunta

    def setFechaHoraPregunta(self, fechaHora):
        self.__fechaHoraPregunta = fechaHora

    def getFechaHoraPregunta(self):
        return self.__fechaHoraPregunta

    def setTemaPregunta(self, tema):
        self.__temaPregunta = tema

    def getTemaPregunta(self):
        return self.__temaPregunta

    def setIdUsuarioPregunta(self, idUsuario):
        self.__idUsuarioPregunta = idUsuario

    def getIdUsuarioPregunta(self):
        return self.__idUsuarioPregunta

    def setEstatusPregunta(self, estatus):
        self.__estatusPregunta = estatus

    def getEstatusPregunta(self):
        return self.__estatusPregunta

    def setLikesPregunta(self, likes):
        self.__likesPregunta = likes

    def getLikesPregunta(self):
        return self.__likesPregunta

    def setComentariosPregunta(self, comentarios):
        self.__comentarios = comentarios

    def getComentariosPregunta(self):
        return self.__comentarios

    # Cuando se cambie de pilas a colas toca invertit cúal bloque está comentado para los métosos __str__ y toJSON
    '''
    def __str__(self):

        listaComentarios = []
        tmp = DLL_Stack()

        while self.__comentarios.count() != 0:
            # Para pilas pop y para colas dequeue
            item = self.__comentarios.pop()
            listaComentarios.append(str(item))
            tmp.push(item)
        while tmp.count() != 0:
            item = tmp.pop()
            self.__comentarios.push(item)

        return 'preg_id:{}\ntitulo:{}\ntexto:{}\nfecha:{}\ntema:{}\nuserid:{}\nstatus:{}\nlikes:{}\ncomments:{}'.format(
            self.__id, self.__tituloPregunta, self.__textoPregunta, self.__fechaHoraPregunta, self.__temaPregunta,
            self.__idUsuarioPregunta, self.__estatusPregunta, self.__likesPregunta, listaComentarios)

    def toJSON(self):
        listaComentarios = []
        tmp = DLL_Stack()

        while self.__comentarios.count() != 0:
            item = self.__comentarios.pop()
            listaComentarios.append(item.toJSON())
            tmp.push(item)
        while tmp.count() != 0:
            item = tmp.pop()
            self.__comentarios.push(item)

        jsondata = {
            "date": str(self.__fechaHoraPregunta),
            "estatus": self.__estatusPregunta,
            "preg_id": self.__id,
            "tema": self.__temaPregunta,
            "texto": self.__textoPregunta,
            "titulo": self.__tituloPregunta,
            "userid": self.__idUsuarioPregunta,
            "likes": self.__likesPregunta,
            "comments": listaComentarios
        }

        return jsondata

    '''

    def __str__(self):

        listaComentarios = []
        tmp = SLL_Queue()

        while self.__comentarios.count() != 0:
            item = self.__comentarios.dequeue()
            listaComentarios.append(str(item))
            tmp.enqueue(item)
        while tmp.count() != 0:
            item = tmp.dequeue()
            self.__comentarios.enqueue(item)

            return 'preg_id:{}\ntitulo:{}\ntexto:{}\nfecha:{}\ntema:{}\nuserid:{}\nstatus:{}\nlikes:{}\ncomments:{}'.format(self.__id, self.__tituloPregunta, self.__textoPregunta, self.__fechaHoraPregunta, self.__temaPregunta, self.__idUsuarioPregunta, self.__estatusPregunta, self.__likesPregunta, listaComentarios)

    def toJSON(self):
        listaComentarios = []
        tmp = SLL_Queue()

        while self.__comentarios.count() != 0:
            item = self.__comentarios.dequeue()
            listaComentarios.append(item.toJSON())
            tmp.enqueue(item)
        while tmp.count() != 0:
            item = tmp.dequeue()
            self.__comentarios.enqueue(item)

        jsondata = {
            "date": str(self.__fechaHoraPregunta),
            "estatus": self.__estatusPregunta,
            "preg_id": self.__id,
            "tema": self.__temaPregunta,
            "texto": self.__textoPregunta,
            "titulo": self.__tituloPregunta,
            "userid": self.__idUsuarioPregunta,
            "likes": self.__likesPregunta,
            "comments": listaComentarios
        }

        return jsondata
