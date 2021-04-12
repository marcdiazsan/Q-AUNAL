class Pregunta:
    #Clase que describe una preguntas y sus atributos para el proyecto Q&A UNAL
    def __init__(self, identificador, titulo,texto,fechaHora, tema, idUsuario, estatus, likes):
        self.__id=identificador
        self.__tituloPregunta=titulo
        self.__textoPregunta=texto
        self.__fechaHoraPregunta=fechaHora
        self.__temaPregunta=tema
        self.__idUsuarioPregunta=idUsuario
        self.__estatusPregunta=estatus
        self.__likesPregunta=likes

    def setId(self,identificador):
        self.__idPregunta = identificador
        
    def getId(self):
        return self.__idPregunta

    def setTituloPregunta(self,titulo):
        self.__tituloPregunta = titulo

    def getTituloPregunta(self):
        return self.__tituloPregunta

    def setTextoPregunta(self,texto):
        self.__textoPregunta = texto

    def getTextoPregunta(self):
        return self.__textoPregunta

    def setFechaHoraPregunta(self,fechaHora):
        self.__fechaHoraPregunta = fechaHora

    def getFechaHoraPregunta(self):
        return self.__fechaHoraPregunta

    def setTemaPregunta(self,tema):
        self.__temaPregunta = tema

    def getTemaPregunta(self):
        return self.__temaPregunta

    def setIdUsuarioPregunta(self,idUsuario):
        self.__idUsuarioPregunta = idUsuario

    def getIdUsuarioPregunta(self):
        return self.__idUsuarioPregunta

    def setEstatusPregunta(self,estatus):
        self.__estatusPregunta = estatus

    def getEstatusPregunta(self):
        return self.__estatusPregunta

    def setLikesPregunta(self,likes):
        self.__likesPregunta = likes

    def getLikesPregunta(self):
        return self.__likesPregunta

    
a = Pregunta(1, 'Prueba','Prueba2','10/04/2021','Prueeba3','marcdiazsan',False,25)

print(str(a.getIdUsuarioPregunta()))
