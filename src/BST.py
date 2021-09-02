class Node():
    def __init__(self, key=None, parent=None,item=None):
        self.key = key
        self.item=item
        self.com=[]
        self.left = None 
        self.right = None
        self.parent = parent
    def getItem(self):
        return self.com

class BST:
    def __init__(self, key=None, parent=None):
        self.node = None

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
    
    def rangeSearch(self, x, y,vals):
        root = self.node
        if root is None:
            return
        if x < root.key :
            root.left.rangeSearch(x, y, vals)
        if x <= root.key and y >= root.key:
            items=root.getItem()
            for i in items:
                vals.append(i)
        if y > root.key:
            root.right.rangeSearch(x,y, vals)
        return vals

    def insert(self, key,item):
        tree = self.node
        
        newnode = Node(key, self.node,item)
        
        if not self.node:
            self.node = newnode 
            self.node.left = BST() 
            self.node.right = BST()
            self.node.com.append(item)

        elif key < tree.key:
            self.node.left.insert(key,item)

        elif key > tree.key:
            self.node.right.insert(key,item)
        elif key==tree.key:
            self.node.com.append(item)
            

    def get_min(self):
        current = self.node
        while current is not None:
            prev_node = current.left.node
            if not prev_node:
                break
            else:
                current = prev_node
        return current.key

    def get_max(self):
        current = self.node
        while current is not None:
            next_node = current.right.node
            if not next_node:
                break
            else:
                current = next_node
        return current.key
#Hay N nodos de preguntas correspondientes a cada fecha, pero cada no puede contener M preguntas realizadas al tiempo

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

    def successor(self, node): 
        node = node.right.node  
        if node:  
            while node.left:
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

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
                    if replacement: # sanity check 
                        self.node.key = replacement.key 
                         
                        self.node.right.delete(replacement.key)
                    
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
        else: 
            return 

'''a = BST()
inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
for i in inlist:
    a.insert(i)
print(a.rangeSearch(3,7,[]))'''
