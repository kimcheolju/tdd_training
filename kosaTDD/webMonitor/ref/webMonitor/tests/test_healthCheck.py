# Test Example
import unittest
import apps.monitor as monitor
import conf.config as config

class TestHealthCheck(unittest.TestCase):
    
    def setUp(self):
        print("Testing HealthCheck", flush=True)
    
    def test_healthCheck_with_invalidUrl_Failed(self):
        self.assertFalse(monitor.healthCheck(url="http://invalid_url:1234", method="GET", timeout=5, waitTime=1, attempts=2))
        
    def test_healthCheck_with_valiedUrl_OK(self):
        self.assertTrue(monitor.healthCheck("http://www.google.com", method="GET", timeout=5, waitTime=1, attempts=2))
        
    def test_healthCheck_with_configUrl_OK(self):
        for serviceUrl in config.SERVICE_URLS:
            self.assertTrue(monitor.healthCheck(serviceUrl["URL"], method=serviceUrl["METHOD"], response_code=serviceUrl["RESPONSE_CODE"], timeout=5, waitTime=1, attempts=2))
                
if __name__ == '__main__':
    unittest.main()