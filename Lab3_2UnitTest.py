import unittest
import io
import sys
from Lab3_2 import DoublyLinkedList
from Lab3_2 import print_list
class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.L = DoublyLinkedList()
        self.L.add_node(1)
        self.L.add_node(-2)
        self.L.add_node(3)
        self.L.add_node(-4)
        self.L.add_node(5)

    def test_add_node(self):
        self.assertEqual(self.L.head.value, 1)
        self.assertEqual(self.L.tail.value, 5)

    def test_print_list(self):
        captured_output = io.StringIO()                  
        sys.stdout = captured_output                     
        print_list(self.L)                                
        sys.stdout = sys.__stdout__                      
        
        self.assertEqual(captured_output.getvalue().strip(), '1\n-2\n3\n-4\n5')

    def test_empty_list(self):
        L = DoublyLinkedList()
        self.assertEqual(L.head, None)
        self.assertEqual(L.tail, None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
