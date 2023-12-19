# Test Example
import unittest
import conf.config as config
import webServiceMonitor as serviceMonitor

class TestWebServiceMonitor(unittest.TestCase):
    
    def setUp(self):
        print("Testing WebServiceMonitor", flush=True)
    
    def test_webServiceHealthCheck_Run(self):
        print("Testing WebServiceMonitor - webServiceHealthCheck", flush=True)
        serviceMonitor.webServiceHealthCheck()
        
    def test_webServiceFailCheck_Run(self):
        print("Testing WebServiceMonitor - webServiceFailCheck", flush=True)
        serviceMonitor.webServiceFailCheck()
        
    def test_webServiceFailCheck_with_FailedStatus(self):
        print("Testing WebServiceMonitor - webServiceFailCheck with FAILED Status", flush=True)
        oldStatus = config.SERVICE_URLS[0]["STATUS"]
        config.SERVICE_URLS[0]["STATUS"] = "FAILED"
        serviceMonitor.webServiceFailCheck()
        self.assertEqual(config.SERVICE_URLS[0]["STATUS"], oldStatus)
                
if __name__ == '__main__':
    unittest.main()