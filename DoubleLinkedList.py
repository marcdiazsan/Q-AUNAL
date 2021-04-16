from Preguntas import *
from Comentarios import *

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def getData(self):
        return self.__data

    def setNext(self, node):
        self.__next = node

    def getNext(self):
        return self.__next

    def setPrev(self, node):
        self.__prev = node

    def getPrev(self):
        return self.__prev

# definicion de la clase pilas con listas simplemente enlazadas

class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def getTail(self):
        return self.__tail

    def setTail(self, item):
        self.__tail = item

    def getHead(self):
        return self.__head

    def setHead(self, item):
        self.__head = item

    # agregar al inicio de la lista
    def pushFront(self, item):
        newNode = Node(item)
        if self.__head == None:
            self.__head = newNode
            self.__tail = self.__head
        else:
            newNode.setNext(self.__head)
            self.__head.setPrev(newNode)
            self.__head = newNode

    # agregar al final de la lista
    def pushBack(self, item):
        newNode = Node(item)
        if (self.__tail==None):
            self.__tail=newNode
            self.__head=newNode
        else:
            newNode.setPrev(self.__tail)
            self.__tail.setNext(newNode)
            self.__tail = newNode

    # eliminar elemento al inicio de la lista y lo devuelve
    def popFront(self):

        if self.__head == None:
            print('No hay elementos para eliminar')
            popNode = Node(None)
        else:
            if (self.__tail==self.__head):
                self.__tail=None
            popNode = self.__head
            self.__head = self.__head.getNext()
            popNode.next = None
            if (self.__head!=None):
                self.__head.setPrev(None)

        return popNode.getData()

    #Remueve el último elemento
    def popBack(self):
        if self.__tail == None:
            print('No hay elementos para eliminar')
            popNode = Node(None)
        elif(self.__tail==self.__head):
            popNode=self.__tail
            self.__tail=None
            self.__head=None
        else:
            popNode=self.__tail
            self.__tail=self.__tail.getPrev()
            popNode.prev=None
            self.__tail.setNext(None)

        return popNode.getData()

    #Remueve un elemento específico por su ID
    def erase(self, key):
        if self.__head == None:
            print('La lista no tiene elementos para eliminar')
        # el elemento que se quiere eliminar es la cabeza
        if self.__head.getData() == key:
            self.__head = self.__head.getNext()
            if (self.__head!=None):
                self.__head.setPrev(None)

        # se busca el elemento

        tmpNode = self.__head

        while tmpNode.getNext() != None:
            if tmpNode.getNext().getData() == key:
                break  # si encuentra el elemento se rompe el ciclo
            tmpNode = tmpNode.getNext()

        # Imprime un mensaje si no se encontro coincidencia en los id de los elementos guardados
        if tmpNode.getNext() == None:
            print('Item no encontrado')
        else:
            tmpNode.setNext(tmpNode.getNext().getNext())
            tmpNode.getNext().setPrev(tmpNode)

    # cuenta el numero de elementos en la lista
    def count(self):
        tmpNode = self.__head
        count = 0
        while tmpNode != None:
            count = count + 1
            tmpNode = tmpNode.getNext()

        return count

    def printList(self):
        temp=self.__head
        while(temp):
            print(temp.getData())
            temp=temp.getNext()

    def find(self, key):

        if self.__head == None:
            print('La lista no tiene elementos')
            return

        tmpNode = self.__head

        while tmpNode != None:
            if tmpNode.getData().getId() == key:
                print('test', tmpNode.getData().getId())
            tmpNode = tmpNode.getNext()

    def empty(self):
        return self.__head == None


class DLL_Stack(DoublyLinkedList):

    def __init__(self):
        super().__init__()

    def getTop(self):
        return super().getHead()

    def push(self, item):
        super().pushFront(item)

    def pop(self):
        element = super().popFront()
        return element

class DLL_Queue(DoublyLinkedList):

    def __init__(self):
        super().__init__()
        self.__rear = None

    def getFront(self):
        return super().getHead()

    def getRear(self):
        return super().getTail()

    def dequeue(self):
        super().popFront()


    def enqueue(self, item):
        super().pushBack(item)

#a=[1,2,3,4,5,6,7,8]
#k= Stack()
#for i in a:
#    k.addElement(i)
#print(k.count())
#k.remove(7)
#k.remove(1)
#k.remove(8)
#temp= Stack()
#temp.addElement(k.getFirst())
#temp.printList()
#print(k.count())
#print(k.getHead().getNext().getData())