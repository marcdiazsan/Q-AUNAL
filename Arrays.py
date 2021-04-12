class Array_Stack():

    def __init__(self, size):
        self.__top = 0
        self.__sarray = [None]*size

    def empty(self):
        return self.__top <= 0

    def full(self):
        return self.__top >= len(self.__sarray)

    def pop(self):
        if self.empty():
            print('La lista esta vacia')
            return

        else:
            self.__top-=1
            return self.__sarray[self.__top]

    def push(self, item):
        if self.full():
            print('La pila esta llena')

        else:
            self.__sarray[self.__top]=item
            top+=1

    def getTop(self):
        if not self.empty():
            return self.__sarray[self.__top - 1]
        else:
            return None
        
    def count(self):
        return self.getTop()
                
class Array_Queue:

    def __init__(self, size):

        self.__front = 0
        self.__rear = 0
        self.__count = 0
        self.__qarray = [None]*size

    def empty(self):
        return self.__count <= 0

    def full(self):
        return self.__count >= len(self.__qarray)

    def count():
        return self.__count

    def enqueue(self, item):
        
        if self.full():
            print('La cola esta llena')

        else:
            self.__qarray[self.__rear] = item
            self.__rear = (self.__rear +1) % len(self.__qarray)
            count += 1

    def dequeue(self):

        item = None
        if self.empty():
            print('La cola esta vacia')

        else:
            item  = self.__qarray[self.__front]
            self._front = (self.__front + 1) % len(self.__qarray)
            self.__count -= 1

        return item

    def getFront(self):
        return self.__qarray[self.__front]

    def getRear(self):
        return self.__qarray[self.__rear]


        
        
    
   
         
         
                

        


    
        

    
    
    
