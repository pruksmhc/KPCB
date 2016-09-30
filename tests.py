import unittest
from HashMap import HashMap
import random
import numbers
import string


class TestHashMap(unittest.TestCase):

    def setUp(self):
		self.size = random.randrange(1, 200)
		self.hash_map = HashMap(self.size)

    def test_initial_state(self):
    	'''
    	    Test initial state after object creation
    	    Expected behavior: any "get" function calls return None
    	    Number of items in map is 0
    	    Load is 0
    	'''
        self.assertTrue(self.hash_map.get_num_items() == 0)
        load = self.hash_map.load()
        self.assertTrue(isinstance(load, numbers.Real))
        self.assertTrue(load == float(0))
        self.assertTrue(self.hash_map.get('null_case') is None)
        self.assertTrue(self.hash_map.delete('null_case') is None)

	def test_insert_invalid(self):
		'''
    	    Test inserting an invalid number. 
    	    Set should return False
    	'''
    	self.assertFalse(self.hash_map.set(None, None))
    	self.assertFalse(self.hash_map.set(100, 100))

    def test_insert_valid(self):
    	'''
    	    Test inserting a valid key. 
    	    Expected behavior: set function returns true and 
    	    load is still < 1
    	'''
    	chars = string.ascii_uppercase + string.digits
    	key = ''.join(random.choice(chars) for _ in range(self.size))
    	saved_key = key
    	value = 1000
    	prev_size = self.hash_map.get_num_items()
    	self.assertTrue(self.hash_map.set(key, value))
    	self.assertTrue((self.hash_map.get_num_items() - prev_size) == 1 )
    	self.assertTrue(self.hash_map.load() <= 1.0)

    def test_delete_invalid(self):
    	'''
    	    Test deleting an invalid key and a key that 
    	    doesn't exist
    	'''
    	self.assertTrue(self.hash_map.delete(None) is None)
    	self.assertTrue(self.hash_map.delete('') is None)

    def test_delete_valid(self):

    	''' 
    		Test deleting a valid value. Number of items should decrease back to 0
    		and the delete function should return the value
    		Load should stay less than 1.0
    	'''

    	curr_size = self.hash_map.get_num_items()
    	chars = string.ascii_uppercase + string.digits
       	key = ''.join(random.choice(chars) for _ in range(self.size))
       	self.hash_map.set(key, 10000)
       	prev_size = self.hash_map.get_num_items()
       	self.assertTrue(self.hash_map.delete(key) == 10000)
       	self.assertTrue(self.hash_map.load() < 1.0)
       	self.assertTrue((prev_size - self.hash_map.get_num_items()) == 1)

    def test_linear_probing(self):

    	''' 
    		First test the case where there is an open slot in the hash map. 
    		Then test the case wehre there are no more slots. 
    		Expected behavior: Return index (here 0) for first case and 
    		-1 for second
    	'''

       	self.hash_map = HashMap(1)
       	self.assertTrue(self.hash_map.find_index('hello') == 0)
       	self.hash_map.set('hello', 10)
       	self.assertTrue(self.hash_map.find_index('bye') == -1)




if __name__ == '__main__':
	unittest.main()