import types

""" Python doesn't act the way you would expect when looking up magic methods on objects.
It expects to find spaces for these definitions at the C-level , meaning that they can't all
be defined on an object at runtime. My solution, without succumbing to manually writing in
every method, is to use this metaclass to generate the proxy class, it will add these methods
to that class so they are defined on the class before the object is created. """
class MetaProxy(type):
    
    magic_methods = ("len", "str", "eq", "ne", "gt", "lt", "ne", "gte", "lte",
                     "getitem", "setitem", "dir", "delitem", "cmp", "le", "ge", "index",
                     "contains", "iter")
    
        
    def __init__(meta, name, bases, properties):
        super(MetaProxy, meta).__init__(name, bases, properties)
        meta.__setup_magic__()
        
    def __setup_magic__(meta):
        def magic(name):
            def wrapper(self, *args):
                fn = getattr(self._obj, name)
                return fn(*args)
            return wrapper
            
        for method in meta.magic_methods:
            name = "__{}__".format(method)
            setattr(meta, name, magic(name))
                
class Proxy(object):
    
    __metaclass__ = MetaProxy
    
    def __init__(self, obj):
        self._obj = obj
        self.accesses = 0
        
    def on_access(self, *args, **kwargs):
        self.accesses += 1
        
    def __getattr__(self, name):
        self.on_access(name)
        return getattr(self._obj, name)
        
    def __hasattr__(self, name):
        return hasattr(self._obj, name)
                