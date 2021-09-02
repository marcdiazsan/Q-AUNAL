from BST import *
from AVL import *
import datetime
from Preguntas import *
from Comentarios import *
import json
import time
import datetime

class Trees(BST):
    def __init__(self):
            super().__init__()
    def creacion(self,dic):
        a=0
        for i in dic.keys():
            item = Pregunta(dic[i]['preg_id'], dic[i]['titulo'], dic[i]['texto'], dic[i]['date'], dic[i]['tema'],
                            dic[i]['userid'], dic[i]['likes'], dic[i]['comments'], dic[i]['estatus'])
            super().insert(dic[i]['date'],dic[i])
            a=a+1
            #print(a)
    def busqueda(self,x,y):
        return super().rangeSearch(x,y,[])


with open('C:/Users/ersan/OneDrive - Universidad Nacional de Colombia/Documentos/Proyecto estructuras/Q-AUNAL/src/JSON100MILLONData.json') as data:
    apiData = json.loads(data.read())

print(len(apiData))
s=time.time()
q=Trees()
q.creacion(apiData)
e=time.time()
print(f"Árboles creados en {e-s}s")
s=time.time()
f=q.busqueda("2020-01-01","2020-12-31")
#print(f)
print(f"Elementos encontrados: {len(f)}")
e=time.time()
print(f"RangeSearch find in {e-s}s")