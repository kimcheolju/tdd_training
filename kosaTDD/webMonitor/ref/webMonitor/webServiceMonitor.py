import conf.config as config
import apps.monitor as monitor
import apps.slackMsg as slackMsg
from datetime import datetime

# 사용할 수 있는 정보 : {"NAME" : "web", "URL" : "192.168.56.111", "METHOD" : "GET", "RESPONSE_CODE" : 200, "STATUS" : "OK"}
def webServiceHealthCheck():
    current_time = datetime.now()
    print(f'----- webService Health Cheking ({current_time})-----', flush=True)
    for serviceUrl in config.SERVICE_URLS:
        status = monitor.healthCheck(serviceUrl["URL"], method=serviceUrl["METHOD"], response_code=serviceUrl["RESPONSE_CODE"])
        if status and serviceUrl["STATUS"] == "FAILED":
            serviceUrl["STATUS"] = "OK"
            for channel in config.SLACK_CHANNEL_URLS:
                slackMsg.post_slack_channel(f'>>>>>> !!! {serviceUrl["NAME"]} : {serviceUrl["STATUS"]} - Back to normal and running... !!! <<<', channel)
        if not status:
            serviceUrl["STATUS"] = "FAILED"
            for channel in config.SLACK_CHANNEL_URLS:
                slackMsg.post_slack_channel(f'>>>>>> !!! {serviceUrl["NAME"]} : {serviceUrl["STATUS"]} - Health Check failed... !!! <<<', channel)

def webServiceFailCheck():
    current_time = datetime.now()
    print(f'----- webService Fail Cheking ({current_time})-----', flush=True)
    for serviceUrl in config.SERVICE_URLS:
        if serviceUrl["STATUS"] == "FAILED":
            print(f'Fail-Check failed, {serviceUrl["NAME"]} : {serviceUrl["STATUS"]} seems to be down.', flush=True)
            webServiceHealthCheck()
            break

if __name__ == '__main__':
    webServiceHealthCheck()
    webServiceFailCheck()