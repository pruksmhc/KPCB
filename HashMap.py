__author__ = 'Yada Pruksachatkun'

'''
	Assumptions: 
	1) By fixed-size, I am assuming this means the hashmap can store a 
	certain number of string to arbitrary data object references.
	2) I am not allowed to use external libraries such as divison
	This is coded up in Python 2.7
'''



class HashMap:

    delete_value = "deleted"

    def __init__(self, size):
        # I used a none to None to be able to check what the string is. 
        # Hash may hash to the same index, but check what the key is.
    	self.table = [(None, None)] * size 
        self._limit = size
        self.num_items = 0

    def map_hash(self, prev_hash):
    	return (prev_hash + 1)%self._limit

    def find_first_free(self, key): 
        if type(key) is not str:
            return -1
        index = key.__hash__() % self._limit
        if ((self.table[index][0] is None) or (self.table[index][0]  == self.delete_value)):
            return index
        else:
            next_index = self.map_hash(index)
            while (self.table[next_index][0] is not None and 
                   self.table[next_index][0] != self.delete_value and
                   next_index != index): # hERE THE NEXT_INDEX HASNT LOOPED AROUDN TO THE first index. 
                next_index = self.map_hash(next_index)
            if self.table[next_index][0] is None or self.table[next_index][0] == self.delete_value:
                return next_index
            else:
                return -1 


    def find_index(self, key): 

        """
        This function searches if the key is in the table
        :params: key (string) 
        :return: index of the next free space, or sapce that is 
        already given to the key using linear probing
        """

        if (type(key) is not str):
        	return -1
        index = key.__hash__() % self._limit
        if self.table[index][0] is None or self.table[index][0] == key:
            return index
        else:
            next_index = self.map_hash(index)
            while (self.table[next_index][0] is not None and 
            	   self.table[next_index][0] != key and
                   next_index != index): 
                next_index = self.map_hash(next_index)
            if self.table[next_index][0] is None or self.table[next_index][0] == key:
                return next_index
            else:
                return -1

    def set(self, key, value):

        """
        :params: key (string), and value (any data type)
        :return: True on success, False otherwise
        """

    	index = self.find_index(key)

    	if self.num_items > (self._limit - 1):
            return False
        if (index == -1):
            index = self.find_first_free(key)
        if (index == -1):
            return False
        else:
    		if (self.table[index][0] is None):
	    		self.num_items = self.num_items + 1
	    	self.table[index] = (key, value)
	    	return True
	    		
    def get(self, key):

    	"""
        :params: key (string)
        :return: Value associated with key, None othersie
        """

    	index = self.find_index(key)
    	if (index is not -1):
    		return self.table[index][1]
    	else:
    		return None

    def delete(self, key):

    	"""
        :params: key (string)
        :return: None if key is not in hashmap, value if otherwise (could be None)
        """

    	index = self.find_index(key)
    	value = None
    	if (index is not -1):
    		value = self.table[index][1]
    		self.table[index] =  (self.delete_value, None)
    		self.num_items = self.num_items - 1
    	return value

    def load(self):
  
    	"""
        :params: none
        :return: Ratio of number of items and size limit
        """

        return (float(0) if self.num_items is 0 
   				else float(self.num_items)/float(self._limit))


