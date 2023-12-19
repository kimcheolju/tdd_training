# Slack Channle에 메시지 보내기
# ref : https://jojoldu.tistory.com/552

import json
import urllib.request

def post_slack_channel(argStr, channelUrl):
    message = argStr
    send_data = {
        "text": message,
    }
    send_text = json.dumps(send_data)
    request = urllib.request.Request(
        channelUrl, 
        data=send_text.encode('utf-8'), 
    )
    
    try:
        with urllib.request.urlopen(request) as response:
            slack_message = response.read()
            return slack_message
    except Exception as e:
        print(f'slack error : {e}', flush=True)
        return 'FAILED'
