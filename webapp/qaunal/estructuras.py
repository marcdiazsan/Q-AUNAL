class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def getData(self):
        return self.__data

    def setNext(self, node):
        self.__next = node

    def getNext(self):
        return self.__next

# definicion de la clase pilas con listas simplemente enlazadas


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def getHead(self):
        return self.__head

    def setHead(self, item):
        self.__head = item

    # agregar al inicio de la lista
    def pushFront(self, item):
        newNode = Node(item)
        newNode.setNext(self.__head)
        self.__head = newNode

    # agregar al final de la lista
    def pushBack(self, item):
        newNode = Node(item)
        if self.__head == None:
            self.__head = newNode

        else:
            tmpNode = self.__head
            while tmpNode.getNext() != None:
                tmpNode = tmpNode.getNext()
            tmpNode.setNext(newNode)

    # eliminar elemento al inicio de la lista y lo devuelve
    def popFront(self):

        if self.__head == None:
            print('No hay elementos para eliminar')
            return
        else:
            popNode = self.__head
            self.__head = self.__head.getNext()
            popNode.setNext(None)

        return popNode.getData()

    def erase(self, key):

        deleted = False
        # no hay elementos en la lista
        if self.__head == None:
            print('La lista no tiene elementos para eliminar')
            return deleted
        # el elemento que se quiere eliminar es la cabeza
        if self.__head.getData().getId() == key:
            self.__head = self.__head.getNext()
            deleted = True
            return deleted

        # se busca el elemento

        tmpNode = self.__head

        while tmpNode.getNext() != None:
            if tmpNode.getNext().getData().getId() == key:
                break  # si encuentra el elemento se rompe el ciclo
            tmpNode = tmpNode.getNext()

        # Imprime un mensaje si no se encontro coincidencia en los id de los elementos guardados
        if tmpNode.getNext() == None:
            print('Item no encontrado')
        else:
            tmpNode.setNext(tmpNode.getNext().getNext())
            deleted = True

        return deleted

    # cuenta el numero de elementos en la lista
    def count(self):
        tmpNode = self.__head
        count = 0
        while tmpNode != None:
            count = count + 1
            tmpNode = tmpNode.getNext()

        return count

    def find(self, key):

        if self.__head == None:
            print('La lista no tiene elementos')
            return

        tmpNode = self.__head

        while tmpNode != None:
            if tmpNode.getData().getId() == key:
                return tmpNode.getData()
            tmpNode = tmpNode.getNext()

    def findWord(self, word):
        data = {}
        if self.__head == None:
            print('La lista no tiene elementos')
            return

        tmpNode = self.__head

        while tmpNode != None:
            if word in tmpNode.getData().getTituloPregunta() or word in tmpNode.getData().getTemaPregunta():

                data[tmpNode.getData().getId()] = tmpNode.getData().toJSON()
            tmpNode = tmpNode.getNext()
        return data

    def empty(self):
        return self.__head == None


class SLL_Stack(SinglyLinkedList):

    def __init__(self):
        super().__init__()

    def getTop(self):
        return super().getHead()

    def push(self, item):
        super().pushFront(item)

    def pop(self):
        super().popFront()


class SLL_Queue(SinglyLinkedList):

    def __init__(self):
        super().__init__()
        self.__rear = None

    def getFront(self):
        return super().getHead()

    def getRear(self):
        return self.__rear

    def dequeue(self):

        element = super().popFront()
        if super().getHead() == None:
            self.__rear = None

        return element

    def enqueue(self, item):

        newNode = Node(item)

        if self.__rear == None:
            self.__rear = newNode
            super().setHead(newNode)
            return

        self.__rear.setNext(newNode)
        self.__rear = newNode


class RabinKarpMatcher():
    def __init__(self):
        self.d = 256
        self.tags = {1: "Artes",
                     2: "Ciencias",
                     3: "Ciencias Agrarias",
                     4: "Ciencias Economicas",
                     5: "Ciencias Humanas",
                     6: "Derecho, Ciencias Políticas y Sociales",
                     7: "Enfermeria",
                     8: "Ingenieria",
                     9: "Medicina",
                     10: "Medicina Veterinaria y de Zootecnia",
                     11: "Odontologia"}
        self.primeFactor = 101
        pass

    def polyHash(self, key, x, primeFactor=31):
        initHash = 0
        for i in range(len(key)-1):
            initHash = (initHash*x + ord(key[i])) % primeFactor
        return initHash

    def search(self, pattern, baseText, primeFactor=31):
        M = len(pattern)
        N = len(baseText)
        pHashVal = 0
        tHashVal = 0
        primeFactor = primeFactor
        x = 34
        pHashVal = self.polyHash(pattern, x, primeFactor)

        for j in range(N-M):
            chunk = baseText[j:j+M]
            tHashVal = self.polyHash(chunk, x, primeFactor)

            if pHashVal != tHashVal:
                continue

            if pattern == chunk:
                return True

        return False

    def compareToTags(self, query):
        similarTags = []
        for (key, value) in self.tags.items():
            tagExists = self.search(
                query.lower(), value.lower(), self.primeFactor)
            if tagExists == True:
                similarTags.append(value)

        return similarTags
