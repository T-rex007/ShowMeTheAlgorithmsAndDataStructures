"""
Author:
Email: 
"""
class Node(object):
    """
    Class defintition of a node
    """
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.count = 0
    
    def getValue(self):
        return self.value
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

    def setValue(self, new_value):
        self.value = new_value
    
    def setLeftChild(self, child):
        self.leftChild = child
    
    def setRightChild(self, child):
        self.rightChild = child 
    
    def hasLeftChild(self):
        if(self.leftChild == None):
            return False
        else: 
            return True
    
    def hasRightChild(self):
        if(self.rightChild == None):
            return False
        else: 
            return True
    def __repr__(self):
        return f"Node({self.getValue()})"
    def __str__(self):
        return f"Node({self.getValue()})"

class Tree(object):
    def __init__(self, value = None):
        self.root = Node(value)


    def getRoot(self):
        return self.root

    def setRoot(self,new_root):
        self.root = new_root
    
class BSTree(Tree):
    def insert(self,new_node):
        current = self.root
        while(current != None):
            if(new_node.getValue()<current.getValue()):
                







def DFT_PreOrder(tree):
    stack = list()
    visited_order = []
    visited = set()
    current = tree.getRoot()
    # Add node to stack and mark visited 
    stack.insert(0,current)
    visited_order.append(current)
    visited.add(current)
    count = 0
    print(current)
    while(current and (count <7)):
        #print(current)
        #print(len(stack))
        count =+1
        if(current.hasLeftChild() and not(current.getLeftChild() in visited)):
            current = current.getLeftChild()
            stack.insert(0,current)
            visited_order.append(current)
            visited.add(current)
            print(current)
        elif(current.hasRightChild() and not(current.getRightChild() in visited)):
            current = current.getRightChild()
            stack.insert(0,current)
            visited_order.append(current)
            visited.add(current)
            print(current)
        else:
            stack.pop(0)
            if(len(stack) != 0):
                current = stack[0]
            else:
                current = None
    return visited_order

def DFT_PreOrderRecursion(tree):
    visited_order = []
    root = tree.getRoot()
    def traverse(parent):
        if(parent==None):
            return
        else:
            visited_order.append(parent)
            traverse(parent.getLeftChild())
            traverse(parent.getRightChild())
            
    traverse(root)
    return visited_order

def DFT_InOrderRecursion(tree):
    visited_order = []
    root = tree.getRoot()
    def traverse(parent):
        if(parent==None):
            return
        else:
            traverse(parent.getLeftChild())
            visited_order.append(parent)
            traverse(parent.getRightChild())
            
    traverse(root)
    return visited_order

def DFT_PostOrderRecursion(tree):
    visited_order = []
    root = tree.getRoot()
    def traverse(parent):
        if(parent==None):
            return
        else:
            traverse(parent.getLeftChild())
            traverse(parent.getRightChild())
            visited_order.append(parent)
    traverse(root)
    return visited_order

def BFS(tree):
    root = tree.getRoot()
    visit_order = []
    queue = []
    queue.insert(0,root)
    while(len(queue) != 0):
        current = queue.pop(-1)
        visit_order.append(current)
        if(current.hasLeftChild()):
            queue.insert(0,current.getLeftChild())
        if(current.hasRightChild()):
            queue.insert(0,current.getRightChild())
    return visit_order





 