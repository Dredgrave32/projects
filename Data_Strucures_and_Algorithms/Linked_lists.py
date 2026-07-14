"""
A Linked List is a linear DS where each element in a list is contained in node with a pointer
to the next with a Head being the begining and the Tail the end. Nodes are known as a self
Referential objects.

Single linked list only has thepointer tot eh next while a Doubl linked list has a previous
and next pointer
"""

class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        """
        This will allow us to represent data from a terminal to allow us to see the Node
        by using `%s` and the % to the self.data to replace teh % with the data we want
        to see.
        """
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        return the number of nodes in the list
        Take O(n) time aka Linear time
        """
        
        current = self.head
        count = 0
        
        while current:  #The same as a while current != None
            count += 1
            current = current.next_node
    
    def add(self, data):
        """
        Adds a new node containing data at the head of the lost
        Takes O(1) time aka Constant time
        """
        
        new_node = data
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time aka Linear Time
        """
        
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None   
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertions takes O(1) time but finding the node at insertion point takes O(n)
        
        Overall the runtime complexity takes O(n) or Linear Time
        """
        
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1
                
            prev = current
            next_node = current.next_node
            
            prev.next_node = new
            new.next_node = next_node
            
    def remove(self, key):
        """
        Removes Node containing data that matches the key.
        Returns the Node or None if key doewsn't exist
        Takes O(n) time, Linear Time
        """
        
        current = self.head
        previous = None
        found = False
            
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current
    
    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time aka Linear Time
        """
        nodes = []
        current = self.head
        
        while current:
            if current is self.head: #if the current node is the head node append data to head
                nodes.append("[Head: %s]" % current.data)
            elif current. next_node is None: #if current node is None append data to Tail node
                nodes.append("[Tail: %s]" % current.data)
            else: #append data to the current node
                nodes.append("[%s]" % current.data)
                
            current - current.next_node # moves to the next node
        return '-> '.join(nodes) #joins the nodes with the '-> ' inbetween each node