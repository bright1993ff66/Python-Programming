# Date: 2018-03-07
# Title: Data Structure
# Author: Haoliang Chang

#*****************************************************************

# 1. Stack: Last in, First out

class Stack(object):
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def values(self):
        return self.items

# 2. Queue: First in, First Out

class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        return self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# 3. Deque: Double-ended queue

class Deque():
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def add_rear(self, item):
        return self.items.insert(0, item)
    
    def add_front(self, item):
        return self.items.append(item)
    
    def size(self):
        return len(self.items)
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def remove_front(self):
        return self.items.pop()

# 4. Unordered list

class Node(object):
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next

from __main__ import Node

class UnorderedList(object):
    
    def __init__(self):
        self.head = None
        self.end = None

    def is_empty(self):
        return self.head == None
               
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
            
        return found
    
    def remove(self, item):
        current = self.head
        previous  = None
        found = False
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
        if previous == None:
            self.head = current.get_next() # when the first item in the linked list is the item 
                                           # we want to remove
        else:
            previous.set_next(current.get_next()) # when we cannot find the item, noting is removed
    
    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        
        while current != None:
            previous = current
            current = current.get_next()
            
        previous.set_next(temp)
        
    def insert(self, index, item):
        current = self.head
        count = 0
        
        if index == 0:
            temp = Node(item)
            temp.set_next(self.head)
            self.head = temp
        elif index >= self.size():
            raise Exception("Index out of range")
        else:
            temp = Node(item)
            previous = None
            while current != None:
                count += 1
                previous = current
                current = current.get_next()
                if count == index-1:
                    temp.set_next(current)
                    previous.set_next(temp)
                    
    def index(self, item):
        current = self.head
        count = 0
        found = False
        
        if current.get_data() == item:
            return count
        elif self.search(item) == False:
            return 'Item is not in this unordered list.'
        else:
            while current != None and not found:
                count += 1
                current = current.get_next()
                if current.get_data() == item:
                    found = True
                else:
                    pass
        
    def pop(self, index):
        current = self.head
        count = 0
        previous = None
        
        if index == 0:
            self.head = current.get_next()
        else:
            while current != None:
                count += 1
                previous = current
                current = current.get_next()
                if count == index:
                    previous.set_next(current.get_next())

# 5. Ordered list

class OrderedList(object):
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
    
    def remove(self, item):
        current = self.head
        previous  = None
        found = False
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
        if previous == None:
            self.head = current.get_next() # when the first item in the linked list is the item 
                                           # we want to remove
        else:
            previous.set_next(current.get_next()) # when we cannot find the item, noting is removed
            
    def remove(self, item):
        current = self.head
        found = False
        stop = False
        
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
                    
        return found
    
    def add(self, item):
        current = self.head
        temp = Node(item)
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
