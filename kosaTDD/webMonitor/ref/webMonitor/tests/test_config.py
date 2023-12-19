# Test Example
import unittest
import conf.config as config

class TestConfig(unittest.TestCase):
    
    def setUp(self):
        print("Testing config", flush=True)
    
    # 2개이상의 검증 케이스가 속해있어서, 좋지 못한 케이스임(단일책임원칙)
    def test_SLACK_CHANNEL_URLS(self):
        self.assertGreaterEqual(len(config.SLACK_CHANNEL_URLS), 1)
        for channel in config.SLACK_CHANNEL_URLS:
            self.assertIn("https://hooks.slack.com/services/", channel)
            print(f"Channel: {channel}", flush=True)

    def test_SERVICE_URLS(self):
        self.assertGreaterEqual(len(config.SERVICE_URLS), 1)
        for service in config.SERVICE_URLS:
            print(f"Service: {service}", flush=True)
        oldStatus = config.SERVICE_URLS[0]["STATUS"]
        config.SERVICE_URLS[0]["STATUS"] = "CHANGED"
        self.assertEqual(config.SERVICE_URLS[0]["STATUS"], "CHANGED")
        config.SERVICE_URLS[0]["STATUS"] = oldStatus
        self.assertEqual(config.SERVICE_URLS[0]["STATUS"], oldStatus)
        
    def test_WebModeRelease(self):
            self.assertEqual(len(config.SLACK_CHANNEL_URLS), 1)
                
if __name__ == '__main__':
    unittest.main()