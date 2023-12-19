import unittest
from apps import monitor



class TestHealthCheck(unittest.TestCase):

    def setUp(self):
        print("Testing Health Check", flush=True)
    
    # Health Check 실패하는 Case
    def test_healthCheck(self):
        self.assertFalse(monitor.HealthCheck("http://invalid_url"))

    # Health Check 성공하는 Case
    def test_healthCheck_with_validUrl_ok(self):
        self.assertTrue(monitor.HealthCheck("http://google.com"))
        
    
if __name__ == '__main__':
    unittest.main()
