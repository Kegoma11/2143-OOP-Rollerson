"""
Keona Rollerson
"""
import random
import time

class BalancedSearchTree(object):
    def __init__(self,size):
        self.tree = [-1 for x in range(size)]
        self.size = size
        self.root = 1
        self.items = 0
        self.subtree = []

    """
    @Name: insert
    @Description:
    -Recieves an int and inserts into binary tree
    @Params:
    val(int) - value inserted into tree
    """
    def insert(self,val):
        if self.tree[self.root] == -1:
            self.tree[self.root] = val
        else:
            i = self.root
            loop = True
            while loop:
                if val > self.tree[i]:
                    i = self.rightChild(i)
                else:
                    i = self.leftChild(i)
                if i >= self.size:
                    self.extend()
                if self.tree[i] == -1:
                    self.tree[i] = val
                    self.item += 1
                    loop = False

    def extend(self,temp):
        self.temp = temp
        temp = [-1 for x in range(self.size)] 
        self.tree.extend(temp) 
        self.size *= 2 
        print(self.items) 

    """
    @Name: insertList
    @Description:
    recieves a list of unordered ints and insets into binary tree so that tree is balanced
    """
    def insertList(self,value):
        value.sort()
        self._recursiveInsert(value)

    def leftChild(self,i):
        return 2 + i

    def rightChild(self,i):
        return 2 * i + 1

    def find(self,key): 
      
         self.comparisons = 1 
 
 
         if key == self.tree[self.root]: 
             return True 
         else: 
             i = self.root 
             while True: 
                 if key < self.tree[i]: 
                     i = self.leftChild(i) 
                 else: 
                     i = self.rightChild(i) 
                      
                 if i >= self.size: 
                     return False 
                  
                 if self.tree[i] == -1: 
                     return False    
                      
                 if self.tree[i] == key: 
                     return True 
                      
                 self.comparisons += 1 

    def  _recursiveInsertList(self, values): 
        self.insert(values[len(values) // 2])    #Inserting middle element of values 
        if len(values) > 1: 
            values_left = values[:len(values) // 2]    
            self._recursiveInsertList(values_left)    #Using recursion  
        if len(values) > 2: 
            values_right = values[len(values) // 2 + 1:]   
            self._recursiveInsertList(values_right)   #recursion 

    def randomList(self):
        unique = []
        random.seed(250)
        num = int(input("Enter number between 1 and 100000"))
        for i in range(0,num):
            r = random.randint(0,100000)

            if r not in unique:
                unique.append(r)

        unique.sort()
        for i in unique:
            BalancedSearchTree.insert(self,i)

if __name__=='__main__': 
    user_input = int(input("Number to insert: (1-100000) ")) 
    list_to_insert = randomList(user_input) 
    random_tree = BalancedSearch() 
    random_tree.insertList(list_to_insert) 
