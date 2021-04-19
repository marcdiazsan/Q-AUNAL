from faker import Faker
import json
import random
from random import randint
from datetime import datetime, timedelta


class DataCreator():
    def __init__(self):
        pass

    def createData(self, preguntas, comentarios):
        # Write to file
        fake = Faker("en_US")
        temas = ["Ingenieria", "Artes", "Ciencias", "Ciencias Agrarias", "Ciencias Economicas", "Ciencias Humanas", "Derecho, Ciencias Politicas y Sociales", "Enfermeria", "Medicina", "Medicina Veterinaria y de Zootecnia", "Odontologia"]
        estatus = ["Activo", "Cerrado"]
        fecha = datetime.now() - timedelta(468)
        duracion = preguntas//468
        data = {}
        for i in range(1, preguntas):
            if (i % 468) == 0 and i >= 0:
                fecha += timedelta(1)
            pregunta = {"preg_id": i, "titulo": "Titulo {}".format(i), "texto": fake.sentence(), "date": str(fecha), "tema": random.choice(temas), "userid": randint(1, 200), "likes": randint(0, 100), "estatus": random.choice(estatus), "comments": []}
            for j in range(1, comentarios):
                comentario = {"com_id": str(i) + "."+str(j), "texto": fake.sentence(), "date": str(fecha), "userid": randint(1, 200), "likes": randint(0, 100), "util": "True", "preg_id": i}
                pregunta["comments"].append(comentario)
            data[i] = pregunta
        JSONData = open('JSON10MILLONESData.json', 'w')
        JSONData.write(json.dumps(data))
        JSONData.close()
        return True
