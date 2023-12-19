# Test Example
import unittest
import apps.slackMsg as slackMsg
import conf.config as config

class TestSlackMsg(unittest.TestCase):
    
    def setUp(self):
        print("Testing SlackMsg", flush=True)
    
    def test_slackMsg_with_invalidChannel_Failed(self):
        self.assertEqual(slackMsg.post_slack_channel("Test", "http://invalid_url"),"FAILED")
        
    def test_slackMsg_with_validChannel_OK(self):
        for channel in config.SLACK_CHANNEL_URLS:
            self.assertNotEqual(slackMsg.post_slack_channel(">>>>>> !!! Web Server Monitor - testing SlackMsg... !!! <<<", channel), "FAILED")
            
    def test_slackMsg_with_sampleMsg_OK(self):
        for channel in config.SLACK_CHANNEL_URLS:
            self.assertNotEqual(slackMsg.post_slack_channel(f'>>>>>> !!! {config.SERVICE_URLS[0]["NAME"]} : {config.SERVICE_URLS[0]["STATUS"]} - This is an example message... !!! <<<', channel), "FAILED")

if __name__ == '__main__':
    unittest.main()