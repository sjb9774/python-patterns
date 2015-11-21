class Task(object):
    
    def __init__(self, name=None, default=False, args=(), kwargs={}):
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.default = default
        
class Processor(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def handle_default(*args, **kwargs):
        pass
        
    def handle(self, task):
        result = None
        if self.can_execute(task):
            method = task.name if hasattr(self, "handle_" + task.name) else "default"
            return getattr(self, "handle_" + method)(*task.args, **task.kwargs)
        elif self.parent:
            return self.parent.handle(task)
            
    def can_execute(self, task):
        return (hasattr(self, "handle_" + task.name) and callable(getattr(self, "handle_" + task.name))) or task.default
