class Task(object):
    
    def __init__(self, name=None, default=False, args=(), kwargs={}):
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.default = default
        
class TaskNode(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def default(*args, **kwargs):
        pass
        
    def handle(self, task):
        result = None
        if self.can_execute(task):
            method = task.name if hasattr(self, task.name) else "default"
            result = getattr(self, method)(*task.args, **task.kwargs)
        elif self.parent:
            result = self.parent.handle(task)
        
        return result
            
    def can_execute(self, task):
        return (hasattr(self, task.name) and hasattr(getattr(self, task.name), "__call__")) or task.default
