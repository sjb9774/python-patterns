class TestClass(object):
    
    def __init__(self, data):
        self.data = data
    
# just for reference purposes, all the testing is based on the more complex singletonizer
class SimpleSingleton(object):
    
    _instance = None
    
    class HiddenClass(object):
        
        def __init__(self, *args, **kwargs):
            pass
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls.HiddenClass(*args, **kwargs)
        return cls._instance
        


    

import functools
import types
def singletonizer(scls, scope=None):
    """ Takes a class and optional scope of existing instances and returns a new class
    that can only be instantiated one time. Further calls to instatiate the class will
    simply return the original, first instance """
    instances = scope if scope else {}
    def class_wrapper(scls):
        
        class NewType(scls):
            def __init__(self, *args, **kwargs):
                pass
            def __new__(cls, *args, **kwargs):
                if not instances.get(scls):
                    instances[scls] = scls(*args, **kwargs)
                scls.__init__(instances.get(scls), *args, **kwargs)
                return instances[scls]
        
        NewType.__name__ = "Singleton_{cls}".format(cls=scls.__name__)
        return NewType
    return class_wrapper(scls)

Singleton = singletonizer(TestClass)    