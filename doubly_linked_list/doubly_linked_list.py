"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        # empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # empty node
        if self.head is None and self.tail is None:
            return None
        # single node in the list
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # multiple node
        value = self.head.value
        self.next.prev = None
        self.head = self.head.next
        self.length -= 1
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        # empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # empty list
        if self.head is None and self.tail is None:
            return None
        # single node in the list
        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # multiple nodes
        current = self.head

        while current.next is not self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #  empty node
        if not node:
            return None
        # self is empty
        if self.head is None and self.tail is None:
            return None
        # single node in the list
        if not self.head.next and not self.tail.prev:
            return self.head.value
        # multiple nodes
        if self.tail == node: # node is the tail
            self.tail = self.tail.prev
            self.tail.next = None
        if self.head == node: # node is the head
            return self.head.value
        # node in the middle of list
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
        value = self.head.value
        return value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # empty node
        if not node:
            return None
        # empty list
        if self.head is None and self.tail is None:
            return None
        # single node
        if self.head == self.tail:
            return self.head.value
        # multiple nodes
        if self.tail == node: # node is the tail
            return self.tail.value
        if self.head == node: # node is the head
            self.head = self.head.next
            self.head.prev = None
        # node in the middle of list
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        value = self.tail.value
        return value

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # empty list
        if self.head is None and self.tail is None:
            return None
        # single node in list
        if not self.head.next and not self.tail.prev:
            value = node.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # multiple node in list
        if node.prev:
            node.prev.next = node.next
        else:
            node.next.prev = None
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            node.prev.next = None
            self.tail = node.prev
        self.length -= 1
        print(self.length)
        value = node.value
        return value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # empty list
        if not self.head:
            return None
        # iterate through list and find the max 
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value