import unittest


class TestExample(unittest.TestCase):

    def setUp(self):
        # 테스트 케이스가 실행되기 전에 최초에 한번 실행되는 것
        print("Testing example", flush=True)
        self.msg = "Hello Test"

    def test_msg_is_hello_test(self): # test_로 시작하는 함수를 만들면 자동으로 실행됨
        msg = self.msg
        self.assertEqual(msg, "Hello Test")

if __name__ == '__main__':
    unittest.main()
