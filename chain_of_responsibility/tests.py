import unittest
from chain import Task, TaskNode

class TestChainOfResponsibility(unittest.TestCase):
    
    def setUp(self):
        self.task = Task(name="test_task", args=("testarg",), kwargs={"testkwarg": True})
        self.root_node = TaskNode()
        self.root_node.test_task = lambda *a, **k: "success"
        
    def test_chain_executes_successfully(self):
        node = TaskNode(self.root_node)
        node2 = TaskNode(node)
        self.assertEqual(node2.handle(self.task), "success")
        
    def test_chain_executes_unsuccessfully(self):
        node = TaskNode(self.root_node)
        node2 = TaskNode(node)
        node3 = TaskNode(node2)
        self.task.name = "unhandleable"
        result = node3.handle(self.task)
        self.assertEqual(result, None)
        
    def test_executes_with_args(self):
        node = TaskNode(self.root_node)
        self.root_node.test_task = lambda *a, **k: (a, k)
        args, kwargs = node.handle(self.task)
        self.assertEqual(args, self.task.args)
        self.assertEqual(kwargs, self.task.kwargs)
    
    def test_can_execute(self):
        self.assertTrue(self.root_node.can_execute(self.task))
        self.task.default = True
        self.assertTrue(TaskNode().can_execute(self.task))
        self.task.name = "some_other_name"
        self.assertTrue(self.root_node.can_execute(self.task))
        self.task.default = False
        self.assertFalse(self.root_node.can_execute(self.task))
        
        
        
        