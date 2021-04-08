from datetime import datetime
class Comentario():
    def __init__(self, com_id,texto, user_id, preg_id, numlikes=0, comentarioútil=False, fecha=datetime.now()):
        self.com_id = com_id
        self.texto=texto
        self.fecha = fecha
        self.user_id=user_id
        self.numlikes = numlikes
        self.comentarioutil = comentarioútil
        self.preg_id=preg_id

    def toJSON(self):
        jsonrep = {
            "com_id": self.com_id,
            "texto": self.texto,
            "date": str(self.fecha),
            "likes": self.numlikes,
            "util": self.comentarioutil,
            "userid": self.user_id,
            "preg_id": self.preg_id
        }
        return jsonrep