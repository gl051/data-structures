"""
    Author: Gianluca Biccari
    Description: Implementation of a Queue
"""

class Queue(object):
    def __init__(self):
        self.qlist = []

    def push(self, value):
        self.qlist.append(value)

    def pop(self):
        val = None
        if len(self.qlist) == 1:
            val = l.pop()
        else:
            val = self.qlist[0]
            self.qlist = self.qlist[1:]
        return val

    # Special class methods (to make it prettier)

    def __len__(self):
        return len(self.qlist)

    def __repr__(self):
        return str(self.qlist)
