#!/usr/bin/env python

"""
    Author: Gianluca Biccari
    Description: Implementation of an Hash Table with string keys
"""


class HashTable(object):
    """
        Do-it by yourself implemenation in case you don't want to use the
        built in data structure dictionary.
    """

    def __init__(self):
        # number of slots per hast table
        self.size = 11
        self.__load_factor_threshold = 100
        # count the element stored in the hash table, to cotroll the load
        # factor and eventually you could resize the table size.
        self.count = 0
        # conflicts resolution with chaining, we use a list per each slot
        self.table = [[] for i in range(1, self.size + 1)]

    def hash_function(self, key):
        # raise an error if the key is not a string
        if not isinstance(key, str):
            raise KeyError('Key for hash table must be a string')
        # hash value is build usin the reminder operator. we sum up the ordinal
        # value of each char using position to weight the value to avoid
        # collision on a palindrome
        sum = 0
        for i, char in enumerate(key):
            sum = sum + ord(char) * (i+1)
        return sum % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        hash_list = self.table[hash_value]
        # we store in the hash table a tuple, including the original key. This
        # is necessary for implementing the remove method.
        hash_data = (key, value)
        hash_keys = [k for (k, v) in hash_list]
        if key in hash_keys:
            # we have already a value with that key, replace it
            index = hash_keys.index(key)
            hash_list[index] = hash_data
        else:
            # append the new value:
            hash_list.append(hash_data)
            self.count = self.count + 1
            if self.__load_factor() > self.__load_factor_threshold:
                print('Collision density warning - ', self.__load_factor())

    def get(self, key):
        hash_value = self.hash_function(key)
        hash_list = self.table[hash_value]
        hash_keys = [k for (k, v) in hash_list]
        if key in hash_keys:
            index = hash_keys.index(key)
            return hash_list[index][1]
        else:
            return None

    def remove(self, key):
        hash_value = self.hash_function(key)
        hash_list = self.table[hash_value]
        hash_keys = [k for (k, v) in hash_list]
        if key in hash_keys:
            index = hash_keys.index(key)
            hash_list.pop(index)
            self.count = self.count - 1
        else:
            return None

    def __load_factor(self):
        """
            __load_factor := (total input) / size
            To signal the level of collisions present in the table at the moment.
            Geometrically is the min(H) where Area = (H x Size) of the hash table
            rectangle.
        """
        return self.count / self.size

    # special class methods (to make it prettier)
    def __getitem__(self, value):
        return self.get(value)

    def __setitem__(self, key, item):
        return self.put(key, item)

    def __len__(self):
        return self.count

    def __delitem__(self, key):
        self.remove(key)

    def __repr__(self):
        return str(self.table)
