import json
from FunctionalQueue import FunctionalQueue
from Stack import Stack


class Encolador():
    def __init__(self):
        pass

    def encolar(self):
        es = FunctionalQueue()
        with open('JSON10MILData.json', 'r+') as data:
            apiData = json.loads(data.read())
        es.creacion(apiData)
        return es

    def enpilar(self):
        es = Stack()
        with open('JSON1MILLONData.json', 'r+') as data:
            apiData = json.loads(data.read())
        es.creacion(apiData)
        return es
