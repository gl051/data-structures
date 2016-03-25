"""
	Author: Gianluca Biccari
	Description: Heap implementation
"""

class Heap(object):
	"""
		Heap can be easily implemented with an array, not using the first
		element helps managing the indexes to move between nodes:
	"""

	def __init__(self):
		self.array = [0]

	# We use the len of the array to have the position of the last element of the
	# heap, so that the count of the element is managed by the built in datatype
	@property
	def lastpos(self):
		# len - 1 because I want the index not the count
		return len(self.array) - 1

	def add(self, value):
		self.array.append(value)
		self.__perculate_up(self.lastpos)

	def minval(self):
		if self.lastpos == 0:
			return None
		else:
			return self.array[1]

	def pop(self):
		if self.lastpos == 0:
			return None
		else:
			if self.lastpos == 1:
				return self.array.pop()
			else:
				ret_val = self.array[1]
				# place the last element at the root
				self.array[1] = self.array.pop()
				self.__perculate_down(1)
				return ret_val

	def remove(self, value):
		if value in self.array:
			pos = self.array.index(value)
			self.array[pos] = self.array.pop()
			self.__perculate_down(pos)

	def __perculate_down(self, pos):
		if pos >= self.lastpos:
			return
		else:
			(left_pos, left_val) = self.__get_left_child(pos)
			(right_pos, right_val) = self.__get_right_child(pos)
			current_val = self.array[pos]
			# Get the min value and position of the min child
			# 2 childs
			if (left_val is not None) and (right_val is not None):
				min_val = min(left_val, right_val)
				min_pos = right_pos if min_val == right_val else left_pos
			elif left_pos is not None:
				# one child only (by heap definition can be only left one)
				min_val = left_val
				min_pos = left_pos
			else:
				# no childs
				return
			# Move the current node down if heap property not satisfied
			if current_val <= min_val:
				return
			else:
				self.array[pos], self.array[min_pos] =  min_val, current_val
				self.__perculate_down(min_pos)


	def __perculate_up(self, pos):
		if pos < 2:
			return
		child_value = self.array[pos]
		(parent_pos, parent_val) = self.__get_parent(pos)
		if child_value < parent_val:
			self.array[parent_pos], self.array[pos] = child_value, parent_val
			self.__perculate_up(parent_pos)

	def __get_parent(self, pos_child):
		# returns tuple (pos, val)
		if pos_child < 2:
			return (None, None)
		else:
			return (pos_child / 2 , self.array[pos_child / 2])

	def __get_left_child(self, pos_parent):
		# returns tuple (pos, val)
		idx = pos_parent * 2
		if idx <= self.lastpos:
			return (idx, self.array[idx])
		else:
			return (None, None)

	def __get_right_child(self, pos_parent):
		# returns tuple (pos, val)
		idx = pos_parent * 2 + 1
		if idx <= self.lastpos:
			return (idx, self.array[idx])
		else:
			return (None, None)

	# Some helper functions
	def __repr__(self):
		return str(self.array)

	def __len__(self):
		# the first element does not count
		return len(self.array) - 1
