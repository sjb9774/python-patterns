import unittest
from singleton import Singleton

class TestSingleton(unittest.TestCase):
    
    def setUp(self):
        self.singleton_1 = Singleton(10)
        self.singleton_2 = Singleton(50)
    
    def test_singleton_data_does_not_change(self):
        self.assertEqual(self.singleton_1.data, 10)
        self.assertEqual(self.singleton_2.data, 10)
        
    def test_singleton_is_singleton(self):
        self.assertEqual(self.singleton_1.data, self.singleton_2.data)
        self.assertEqual(id(self.singleton_1), id(self.singleton_2))