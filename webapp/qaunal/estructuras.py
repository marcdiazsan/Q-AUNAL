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


class AVLNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def search(self, key):

        tree = self.node
        if tree == None:
            return
        if tree.key == key:
            return self
        elif tree.key < key:
            return self.node.right.search(key)
        elif tree.key > key:
            if self.node.left:
                return self.node.left.search(key)
            else:
                return

    def rangeSearch(self, x, y, vals):
        root = self.node
        if root is None:
            return
        if x < root.key.date_created:
            root.left.rangeSearch(x, y, vals)
        if x <= root.key.date_created and y >= root.key.date_created:
            vals.append(root.key)
        if y > root.key.date_created:
            root.right.rangeSearch(x, y, vals)
        return vals

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        tree = self.node

        newnode = AVLNode(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key.date_created < tree.key.date_created:
            self.node.left.insert(key)

        elif key.date_created > tree.key.date_created:
            self.node.right.insert(key)

        self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_heights()
                    self.update_balances()
                self.right_rotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_heights()
                    self.update_balances()
                self.left_rotate()
                self.update_heights()
                self.update_balances()

    def right_rotate(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def left_rotate(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        if self.node != None:
            if self.node.key == key:
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                else:
                    successor = self.successor(self.node)
                    if successor:
                        self.node.key = successor.key

                        self.node.right.delete(successor.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def predecessor(self, node):
        node = node.left.node
        if node:
            while node.right:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def successor(self, node):
        node = node.right.node
        if node:
            while node.left:
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder(self, vals):
        if not self.node:
            return
        if self.node.left is not None:
            self.node.left.inorder(vals)
        if self.node.key is not None:
            vals.append(self.node.key)
        if self.node.right is not None:
            self.node.right.inorder(vals)
        return vals

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')
