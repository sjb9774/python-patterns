import types
magic_methods = ("len", "str", "eq", "neq", "gt", "lt", "ne", "gte", "lte",
                 "getitem", "setitem", "dir", "del", "cmp", "le", "ge", "index",
                 "contains", "iter")

class Proxy(object):
    
    def __init__(self, obj):
        self._obj = obj
        self.__setup_magic__()
        
    def on_access(self, *args, **kwargs):
        pass
        
    def __getattr__(self, name):
        self.on_access(name)
        return getattr(self._obj, name)
        
    def __hasattr__(self, name):
        return hasattr(self._obj, name)
    
    def __setup_magic__(self):
        def magic(name):
            def wrapper(*args):
                return getattr(self._obj, name)(*(args[1:]))
            return wrapper
            
        for method in magic_methods:
            name = "__{}__".format(method)
            if hasattr(self._obj, name):
                setattr(self.__class__, name, magic(name))