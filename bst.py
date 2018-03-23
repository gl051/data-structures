#!/usr/bin/env python

"""
    Description: Implementation of a binary search tree
"""


from queue import Queue  # for breadth first traversal


class Node:
    """
        Node element of a tree
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # to support delete operation we add parent ref
        self.parent = None


class Tree:

    def __init__(self):
        # root node
        self.root = None
        self.count = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(value, self.root)

    def __insert(self, value, node):
        if value < node.value:
            # Go left
            if node.left is None:
                node.left = Node(value)
                node.left.parent = node
                self.count = self.count + 1
            else:
                self.__insert(value, node.left)
        else:
            # Go right
            if node.right is None:
                node.right = Node(value)
                node.right.parent = node
                self.count = self.count + 1
            else:
                self.__insert(value, node.right)

    # Find a node
    def search(self, value):
        if self.root is None:
            return None
        else:
            return self.__search(value, self.root)

    def __search(self, value, node):
        if value is node.value:
            return node
        else:
            if value < node.value and node.left is not None:
                return self.__search(value, node.left)
            elif node.right is not None:
                return self.__search(value, node.right)
            else:
                return None

    def show(self):
        self.inorder()

    # Delete a node
    # Trick: instead of deleting the node, we replace its value
    # with the right subsitute node depending on where the node
    # to delete is located. Then we drop the substitue node when
    # has been copied in position.
    def delete(self, value):
        if self.root is None:
            return None
        else:
            self.__delete(value, self.root)

    def __delete(self, value, node):
        if node.value is value:
            # found the node to delete
            # we can have situations of:
            # 0 child (leaf node)
            # 1 child
            # 2 child (most difficut)
            if node.left is None and node.right is None:
                node.parent.left = None
                node.parent.right = None
            elif node.left is not None and node.right is None:
                # 1 child only left
                # print '1 child left
                node.value = node.left.value
                node.right = node.left.right
                node.left = node.left.left
            elif node.right is not None and node.left is None:
                # 1 child only right
                # print '1 child right'
                node.value = node.right.value
                node.left = node.right.left
                node.right = node.right.right
            elif node.left is not None and node.right is not None:
                # 2 childs
                # print '2 childs'
                new_node = self.__min(node.right)
                node.value = new_node.value
                if node.right is new_node:
                    node.right = new_node.right
                    # node.left = new_node.left
                else:
                    if new_node.left is None and new_node.right is not None:
                        new_node.parent.left = new_node.right
                    else:
                        new_node.parent.left = None
            # detach the current node
            # node = None
            self.count = self.count - 1
        else:
            if value < node.value:
                if node.left:
                    self.__delete(value, node.left)
            else:
                if node.right:
                    self.__delete(value, node.right)

    # Get the min node (min val)
    def min(self):
        if self.root is None:
            return None
        else:
            return self.__min(self.root)

    def __min(self, node):
        if node.left is None:
            return node
        else:
            return self.__min(node.left)

    # Deepth First Traversal:
    # - inorder: left, parent, right
    # - preorder: parent, left, right
    # - postorder: left, right, parent
    # Complexity: O(n)

    def inorder(self):
        if self.root is None:
            print('Empty tree')
        else:
            self.__inorder(self.root)

    def __inorder(self, node):
        if node is not None:
            self.__inorder(node.left)
            print(str(node.value))
            self.__inorder(node.right)

    def preorder(self):
        if self.root is None:
            print('Empty tree')
        else:
            self.__preorder(self.root)

    def __preorder(self, node):
        if node is not None:
            print(str(node.value))
            self.__preorder(node.left)
            self.__preorder(node.right)

    def postorder(self):
        if self.root is None:
            print('Empty tree')
        else:
            self.__postorder(self.root)

    def __postorder(self, node):
        if node is not None:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(str(node.value))

    # Breadth First Traversal:
    # Implementation using a Queue, first the node is printed then its child nodes
    # are put into a FIFO. You iterate until no nodes are left in the queue.
    def breadth(self):
        if self.root is None:
            print('Empty tree')
        else:
            q = Queue()
            q.put(self.root)
            while (q.empty() is not True):
                node = q.get()
                print(node.value),
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
