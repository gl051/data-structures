"""
    Implement a circular buffer of size N. 
    Allow to append, remove and list the content of the buffer
    New items are appended to the end, when the number of elements in the buffer exceeds the defined size, 
    the older elements are overwritten
"""

class CircularBuffer():
    def __init__(self, size):
        self.__size = size
        self.__list = [None for i in range(size)]
        self.__index = -1

    def __increment_index(self):
        self.__index = (self.__index + 1) % (self.__size)

    def __decrement_index(self):
        self.__index = (self.__index - 1) % (self.__size)

    def add(self, value):
        self.__increment_index()
        self.__list[self.__index] = value

    def get(self):
        return self.__list[self.__index]
        self.__decrement_index()

    def __str__(self):
        return str(self.__list)

