from qaunal import app, db, bcrypt
import json
from datetime import datetime
from qaunal.models import User, Pregunta, Comentario

def creacion(dic):
    for key in dic.keys():
        item = Pregunta(titulo=dic[key]['titulo'], 
                        contenido=dic[key]['texto'], 
                        date_created=datetime.strptime(
                            dic[key]['date'], '%Y-%m-%d %H:%M:%S.%f')                        ,
                        etiquetas=dic[key]['tema'], 
                        likes=dic[key]['likes'],
                        resuelta=True if dic[key]['estatus'] == 'Resuelta' else False,
                        user_id = dic[key]['userid'])

        comentarios = dic[key]['comments']

        for com in comentarios:
            comPreg = Comentario(date_created=datetime.strptime(
                com['date'], '%Y-%m-%d %H:%M:%S.%f'),
                            contenido=com['texto'],
                util=True if dic[key]['estatus'] == 'True' else False,
                            likes=com['likes'],
                            pregunta_id=com['preg_id'],
                            user_id=com['userid'])
            db.session.add(comPreg)
            db.session.commit()
        db.session.add(item)
        db.session.commit()
        


with open('JSON10MILData.json', 'r+') as data:
        apiData = json.loads(data.read())
        creacion(apiData)
