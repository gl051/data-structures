#!/usr/bin/env python

"""
    Author: Gianluca Biccari
    Description: Implementation of a Stack
"""


class Stack(object):
    """
        We implement the stack using the internal data type list, but we could
        also have used a double linked list to have more control of the implementation
    """

    def __init__(self):
        self.klist = []

    def push(self, value):
        self.klist.append(value)

    def pop(self):
        return self.klist.pop()

    # Special class methods (to make it prettier)

    def __len__(self):
        return len(self.klist)

    def __repr__(self):
        return str(self.klist)
