class Comentario:
    #Clase que describe los comentarios y sus atributos para el proyecto Q&A UNAL
    def __init__(self, ide,texto,fechaHora,idUsuario,likes,utilidad,idPregunta):
        self.__idComentario=ide
        self.__textoComentario=texto
        self.__fechaHoraComentario=fechaHora
        self.__idUsuarioComentario=idUsuario
        self.__likesComentario=likes
        self.__utilidadComentario=utilidad
        self.__idPreguntaComentario=idPregunta

    def setId(self,ide):
        self.__idComentario = ide
        
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

    def setLikesComentario(self,likes):
        self.__likesComentario = likes

    def getLikesComentario(self):
        return self.__likesComentario

    def setIdPreguntaComentario(self, idPregunta):
        self.__idPreguntaComentario = idPregunta
        
    def getIdPreguntaComentario(self):
        return self.__idPreguntaComentario

    def __str__(self):
        return 'com_id:{}\ntexto:{}\nfecha:{}\nutil:{}\nlikes:{}\nuserid:{}\npreg_id:{}\n'.format(self.__idComentario, self.__textoComentario, self.__fechaHoraComentario, self.__utilidadComentario, self.__likesComentario, self.__idUsuarioComentario, self.__idPreguntaComentario)
        

    def toJSON(self):
        jsonrep = {
            "com_id": self.__idComentario,
            "texto": self.__textoComentario,
            "date": str(self.__fechaHoraComentario),
            "likes": self.__likesComentario,
            "util": self.__utilidadComentario,
            "userid": self.__idUsuarioComentario,
            "preg_id": self.__idPreguntaComentario
        }
        return jsonrep
