import requests
import time

# 사용할 수 있는 정보 : {"NAME" : "web", "URL" : "192.168.56.111", "METHOD" : "GET", "RESPONSE_CODE" : 200, "STATUS" : "OK"}
def healthCheck(url, method = "GET", response_code = 200, timeout = 20, waitTime = 10, attempts = 2):
       
    online = False

    for i in range(1, attempts + 1):
        try:
            response = requests.request(method, url, timeout=timeout, allow_redirects=False)
            if response.status_code == response_code:
                online = True
                break
        except requests.exceptions.RequestException:
            pass
        
        time.sleep(waitTime)

    if online:
        print(f'Health-Check finished, {url} is online.', flush=True)
    else:
        print(f'Health-Check failed, {url} seems to be down.', flush=True)
        
    return online