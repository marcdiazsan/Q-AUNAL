class Comentario:
    #Clase que describe los comentarios y sus atributos para el proyecto Q&A UNAL
    def __init__(self, id,texto,fechaHora,idUsuario,likes,utilidad,idPregunta):
        self.__idComentario=id
        self.__textoComentario=texto
        self.__fechaHoraComentario=fechaHora
        self.__idUsuarioComentario=idUsuario
        self.__likesComentario=likes
        self.__utilidadComentario=utilidad
        self.__idPreguntaComentario=idPregunta

    def setId(self,id):
        self.__idComentario = id
        
    def getId(self):
        return self.__idComentario

    def setTextoComentario(self,texto):
        self.__textoComentario = texto

    def getTextoPregunta(self):
        return self.__textoPregunta

    def setFechaHoraComentario(self,fechaHora):
        self.__fechaHoraComentario = fechaHora

    def getFechaHoraComentario(self):
        return self.__fechaHoraComentario

    def setIdUsuarioComentario(self,idUsuario):
        self.__idUsuarioComentario = idUsuario

    def getIdUsuarioComentario(self):
        return self.__idUsuarioComentario

    def setUtilidadComentario(self,utilidad):
        self.__utilidadComentario = utilidad

    def getUtilidadComentario(self):
        return self.__utilidadComentario

    def setLikesPregunta(self,likes):
        self.__likesPregunta = likes

    def getLikesPregunta(self):
        return self.__likesPregunta

    def setIdPreguntaComentario(self, idPregunta):
        self.__idPreguntaComentario = idPregunta
        
    def getIdPreguntaComentario(self):
        return self.__idPreguntaComentario
