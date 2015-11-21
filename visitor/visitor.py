class Element(object):
    
    def accept(self, visitor):
        visitor.visit(self)
        
class Visitor(object):
    
    def visit(self, element):
        self.operate(element)
        

class Node(Element):
    
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        
class DescriptiveVisitor(Visitor):
    
    def __init__(self):
        self.counter = 0
        
    def operate(self, element):
        self.counter += 1
        print "Visit {n}: {e}; data {d}".format(n=self.counter, e=element, d=element.data)

class ManipulativeVisitor(Visitor):
    
    def __init__(self):
        self.running_total = 0
        
    def operate(self, element):
        element.running_total = self.running_total + element.data
        self.running_total = element.running_total
        
class DeleteVisitor(Visitor):
    
    def __init__(self, **criteria):
        self.criteria = criteria
        self.previous = None
        
    def operate(self, element):
        for k, v in self.criteria.iteritems():
            if hasattr(element, k) and getattr(element, k) == v:
                if self.previous:
                    self.previous.parent = element.parent
        else:
            self.previous = element
        
        
        
        
previous_node = None
for i in xrange(10):
    previous_node = Node(i, parent=previous_node)
    
    
xv = DeleteVisitor(data=4)
next_node = previous_node
while next_node:
    next_node.accept(xv)
    next_node = next_node.parent
    
dv = DescriptiveVisitor()
next_node = previous_node
while next_node:
    next_node.accept(dv)
    next_node = next_node.parent
    

    

        