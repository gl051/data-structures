"""
    Author: Gianluca Biccari
    Description: Linked List Implementation
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.count = self.count + 1
        else:
            self.__insert(self.head, value)

    def __insert(self, node, value):
        if node.next is None:
            node.next = Node(value)
            self.count = self.count + 1
        else:
            self.__insert(node.next, value)

    def delete(self, value):
        if self.head is None:
            return
        else:
            # need to check if the head is my value first
            if self.head.value == value:
                self.head = self.head.next
            else:
                # check next nodes
                self.__delete(self.head, value)

    def __delete(self, node, value):
        # delete needs to stay one node behind to adjust the link
        if node.next == None:
            return
        else:
            if node.next.value == value:
                node.next = node.next.next
                self.count = self.count - 1
            else:
                self.__delete(node.next, value)

    def search(self, value):
        if self.head is None:
            return
        else:
            self.__search(self.head, value)

    def __search(self, node, value):
        if (node == None) or (node.value == value):
            return node.value
        else:
            self.__search(node.next, value)

    # Special methods implementation
    def __len__(self):
        return self.count

    def __repr__(self):
        # I could traverse the list with recursion but just for the sake
        # of changing style I use iteration this time
        string = ""
        if self.head is None:
            return ""
        else:
            string = str(self.head.value)
            node = self.head
            while node != None:
                string = string + " " + str(node.value)
                node = node.next
            return string
