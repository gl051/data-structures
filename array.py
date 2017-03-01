#!/usr/bin/env python

"""
    Author: Gianluca Biccari
    Description: Implementation of an Array data structure
"""


class Array(object):
    """
        Python has already `list` that acts as an arrya, but  we are going
        to implement an array which is slightly different, it requires elements
        of the same data type and also a fixed lenght for the array itself.
        In this example:
        - data type is a string
        - fixed size limit
        - we access/add/remove elements by indexing (to consider for big O notation)
    """

    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(0, self.size)]

    def put(self, index, value):
        """
            If the array slot is taken we replace the value, we could handle
            this in other ways but this is the more similar to real scenarios
            using array.
        """
        self.__check_index(index)
        self.__check_value(value)
        # Not using the built in index control of the list because I want to
        # have control of the error message.
        if index < self.size:
            self.array[index] = value
        else:
            raise IndexError('Index goes over the size of the array')

    def get(self, index):
        self.__check_index(index)
        # Not using the built in index control of the list because I want to
        # have control of the error message.
        if index < self.size:
            return self.array[index]
        else:
            raise IndexError('Index goes over the size of the array')

    def delete(self, index):
        self.__check_index(index)
        if index < self.size:
            self.put(index, None)
        else:
            raise IndexError('Index goes over the size of the array')

    def __check_index(self, index):
        if not isinstance(index, int):
            raise IndexError('Index for array must be an integer')

    def __check_value(self, value):
        if not isinstance(value, str):
            raise TypeError('Value for array must be a string')

    # Special methods Implementation

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        return self.put(index, value)

    def __len__(self):
        return self.size

    def __delitem__(self, key):
        self.remove(key)

    def __repr__(self):
        return str(self.array)

    def __iter__(self):
        i = 0
        while i < self.size:
            yield self.array[i]
            i = i + 1
