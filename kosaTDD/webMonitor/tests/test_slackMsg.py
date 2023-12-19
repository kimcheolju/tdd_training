import unittest
from apps import slackMsg

SLACK_CHANNEL = 'https://hooks.slack.com/services/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'

class TestSlackMsg(unittest.TestCase):

    def setUp(self):
        print("Testing SlackMsg", flush=True)
    
    # 메시지 발송 실패하는 Case
    def test_slackMsg_with_invalidChannel_Failed(self):
        self.assertEqual(slackMsg.post_slack_channel("Test", "http://invalid_url"),"FAILED")        

    # 메시지 발송 성공 Case
    def test_slackMsg_with_validChannel_OK(self):
        #self.assertNotEqual(slackMsg.post_slack_channel("지중해산 참치", SLACK_CHANNEL), "FAILED")
        self.assertEqual(slackMsg.post_slack_channel("lililli", SLACK_CHANNEL), b'ok')
        
    
if __name__ == '__main__':
    unittest.main()
