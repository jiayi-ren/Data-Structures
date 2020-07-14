"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   To enqueue and dequeue, it takes O(1) using linked list. For array, the worst case can be O(n)


Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)
#         else:
#             return None

### Linked List Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def add_to_tail(self, value):
        # 1. create the Node from the value 
        new_node = Node(value)
        # So, what do we do if tail is None? 
        # What's the rule we want to set to indicate that the linked
        # list is empty? 
        # Would it be better to check the head? 
        # Let's check them both: an empty linked list has an empty 
        # head and an empty tail 
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should head and tail 
            # be referring to? 
            # have both head and tail referring to the single node 
            self.head = new_node
            # set the new node to be the tail 
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring
            # to a Node 
            # 2. set the old tail's next to refer to the new Node 
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node 
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list 
        if self.head is None and self.tail is None:
            return
        # what if we only have a single elem in the linked list?
        # both head and tail are pointing at the same Node 
        if not self.head.get_next():
            head = self.head 
            # delete the linked list's head reference 
            self.head = None
            # also delete the linked list's tail reference 
            self.tail = None 
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head 
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an empty linked list 
        if self.head is None and self.tail is None:
            return
        # if we have a non-empty linked list 
        # we have to start at the head and move down the linked list 
        # until we get to the node right before the tail 
        # iterate over our linked list 
        current = self.head 

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()
        # at this point, `current` is the node right before the tail 
        # set the tail to be None
        val = self.tail.get_value() 
        # move self.tail to the Node right before
        self.tail = current
        self.tail.set_next(None)
        return val

    def contains(self, value):
        if not self.head:
            return False
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None