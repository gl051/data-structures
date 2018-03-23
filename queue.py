#!/usr/bin/env python

"""
    Author: Gianluca Biccari
    Description: Implementation of a Queue
"""


class Queue(object):
    """
        Implement the queue using a single list
    """
    def __init__(self):
        self.qlist = []

    def push(self, value):
        self.qlist.append(value)

    def pop(self):
        val = None
        if len(self.qlist) == 1:
            val = self.qlist.pop()
        else:
            val = self.qlist[0]
            self.qlist = self.qlist[1:]
        return val

    # Special class methods (to make it prettier)

    def __len__(self):
        return len(self.qlist)

    def __repr__(self):
        return str(self.qlist)


 class Queue2():
     """
        Implementing the Queue using two list/stack
     """

     def __init__(self):
        self.__listin = []
        self.__listout = []
   
    def push(self, value):
        self.__listin.append(value)
  
    def pop(self):
        if len(self.__listout) > 0:
            return self.__listout.pop()
        else:
            for val in range(len(self.__listin)):
                pv = self.__listin.pop()
                self.__listout.append(pv)
                return self.__listout.pop()
