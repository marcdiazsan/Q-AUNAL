from datetime import datetime
import json

class Pregunta():
    def __init__(self, preg_id, titulo, contenido, tema, userid, comments=[],status=False, fecha=datetime.now()):
        self.preg_id=preg_id
        self.titulo=titulo
        self.texto=contenido
        self.fecha=fecha
        self.tema=tema
        self.userid=userid
        self.status=status
        self.comments=comments

    def toString(self):
        return 'preg_id:{}\ntitulo:{}\ntexto:{}\nfecha:{}\ntema:{}\nuserid:{}\nstatus:{}\ncomments:{}'.format(self.preg_id, self.titulo, self.texto, self.fecha, self.tema, self.userid, self.status, self.comments)

    def toJSON(self):
        jsondata = {
            "date": str(self.fecha),
            "estatus": self.status,
            "preg_id": self.preg_id,
            "tema": self.tema,
            "texto": self.texto,
            "titulo": self.titulo,
            "userid": self.userid,
            "comments": self.comments
        }
        return jsondata