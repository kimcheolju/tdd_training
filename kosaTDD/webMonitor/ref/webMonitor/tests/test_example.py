# Test Example
import unittest

class TestExample(unittest.TestCase):
    
    def setUp(self):
        print("Testing example", flush=True)
        self.msg = "Hello Test"
    
    def test_msg_is_hello_test(self):
        msg = self.msg
        self.assertEqual(msg, "Hello Test")
        
if __name__ == '__main__':
    unittest.main()