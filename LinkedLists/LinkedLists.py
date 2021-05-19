class Element:
    def __init__(self, value):
        self.value =value
        self.next = None
        self.prev = None


class LinkedList:
    head = None
    tail = None
    size = 0

    def addToBack(self, new_element):
        """
        
        """
        current = self.head 
        if(current == None):
            self.head = new_element
            self.tail = new_element
            self.size = self.size + 1
        else:
            new_element.prev = self.tail
            self.tail.next = new_element 
            self.tail = new_element
            self.size = self.size + 1
        
    def addToFront(self,new_element ):
        """
        
        """
        current = self.head
        if(current ==None):
            self.head = new_element
            self.tail = new_element
            self.size = self.size + 1
        else: 
            new_element.next =self.head
            self.head.prev = new_element
            self.head = new_element
            self.size = self.size + 1


        
    def printList(self):
        """
        Prints the linked List from head to tail
        """
        current = self.head
        if(current == None):
            print(None)
        else:
            print(current.value)
            while(current.next != None):
                current = current.next 
                print(current.value)
        
    def printRevList(self):
        """
        
        """
        current = self.tail
        if(current == None):
            print(None)
        else:
            print(current.value)
            while(current.prev != None):
                current = current.prev 
                print(current.value)
    def loopDetection(self):
        """
        Return whetheror not this link list has a loop
        """
        hash_table = set()
        current =self.head
        while(current.next != None):
            if(current in hash_table):
                return True
            had_table.add(current)
            current = current.next
        return False

            
            
    def printLast(self):
        print(self.head.value)
            

if(__name__ =='__main__'):

    lst = LinkedList()
    for i in range(10):
        e1 = Element(i)
        lst.addToBack(e1)
    print("Reverse List:")
    lst.printRevList()
    print()
    print("List")
    lst.printList()
    print()
    lst.printLast()

    lst = LinkedList()