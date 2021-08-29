class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
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

    def rangeSearch(self, x, y,vals):
        root = self.node
        if root is None:
            return
        if x < root.key :
            root.left.rangeSearch(x, y, vals)
        if x <= root.key and y >= root.key:
            vals.append(root.key)
        if y > root.key:
            root.right.rangeSearch(x,y, vals)
        return vals
    
    def is_leaf(self):
        return self.height == 0 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
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
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')
a = AVLTree()
inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
for i in inlist:
    a.insert(i)
print(a.rangeSearch(2,9,[]))
