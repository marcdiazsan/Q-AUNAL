from faker import Faker
import json
import random
from random import randint
from datetime import datetime


class DataCreator():
    def __init__(self):
        pass
    def createData(self, preguntas, comentarios):
        # Write to file 
        fake = Faker("en_US")
        data = {}
        for i in range(1, preguntas):
            pregunta = {"preg_id": i, "titulo": "Titulo {}".format(i), "texto":fake.text(), "date":str(datetime.now()), "tema":"Ingenieria", "userid": randint(1,200), "estatus": "Success", "comments":[]} 
            for j in range(1, comentarios):
                comentario = {"com_id": str(i) + str(j), "texto":fake.text(), "date":str(datetime.now()), "userid": randint(1,200), "likes": randint(0, 100), "util": "True", "preg_id":i} 
                pregunta["comments"].append(comentario)
            data[i]= pregunta
        JSONData = open('JSONData.json', 'w')
        JSONData.write(json.dumps(data))
        JSONData.close()
        return True
            
            

            
