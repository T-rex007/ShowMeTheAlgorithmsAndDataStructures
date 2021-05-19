
class Node(object):
    def __init__(self,key, value):
        self.value = value
        self.key =key
        self.next = None
        self.prev= None
        

class LinkedList(object):
    head = None
    def __init(self, head = None,size = 0):
        self.head = head
        self.tail = None
        self.size = size

    def addTop(self, new_node):
        """
        Add Items to the top
        """
        
        new_node.next = self.head
        if(self.head!=None): # Not first Item
            self.head.prev = new_node
        else: # First item on list
            self.tail = new_node
        self.head = new_node

    def pop(self):
        """
        Returns the last element from the list
        """
        tmp = self.tail.prev
        tmp.next = None
        self.tail.prev = None
        tail = self.tail
        self.tail  = tmp
        return tail 

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
 

            
            
    def printLast(self):
        print(self.head.value)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity 
        self.numItems = 0
        self.cache = dict()
        self.cachedData = LinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if(key in cache.keys()):
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if(key  not in self.cache.keys()):
            print("True")
            if(self.numItems<self.capacity):
                self.cache[key] = Node(key,value)
                self.cachedData.addTop(self.cache[key])
                self.numItems +=1
            else:
                # Remove least used node (the tail)
                tmp = self.cachedData.pop()
                del cache[tmp[key]]
                del tmp
                # Add node to the top of the list
                self.cache[key] = Node(key,value)
                self.cachedData.addTop(self.cache[key])

    def printCache(self):
        print()
        print(">> Cache")
        print("-"*80)
        for key,value in self.cache.items():
            print("Key: {}\t Value: {}".format(key, value.value))
        print("-"*80)

if(__name__ == "__main__"):
    cache = LRU_Cache(5)
    cache.printCache()
    cache.set("Tyrel", "is A Boss")
    cache.printCache()

