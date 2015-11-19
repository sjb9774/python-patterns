import unittest
from proxy import Proxy

class TestProxy(unittest.TestCase):
    
    def test_list_proxy(self):
        l = ["list", "elements", "could", "cause", "issues"]
        p = Proxy(l)
        self.assertEqual(p[0], "list")
        self.assertEqual(p[-2], "cause")
        self.assertEqual(p, l)
        self.assertEqual(len(p), len(l))
        self.assertNotEqual(id(p), id(l))
        
    def test_dict_proxy(self):
        d = {"key1": "val1", "key2": "val2"}
        p = Proxy(d)
        self.assertEqual(p["key1"], "val1")
        self.assertEqual(len(p.keys()), len(d.keys()))
        self.assertEqual(p, d)
        self.assertTrue(p == d)
        self.assertNotEqual(id(p), id(d))
        del p["key1"]

    def test_object_proxy(self):
        o = type("TestClass", (object,), {"prop1": [1,2,3], "prop2": "a string"})()
        pr = Proxy(o)
        self.assertEqual(pr.prop1, o.prop1)
        self.assertEqual(pr.prop2, o.prop2)
        
        # My philosophy is that a proxy should be known to be a proxy, it should provide
        # a middleman for accessing an object, and make it easy to access that object 
        # through itself, but it should not pretend to *be* that object.
        self.assertTrue(o == pr._obj)
        self.assertNotEqual(id(pr), id(o))