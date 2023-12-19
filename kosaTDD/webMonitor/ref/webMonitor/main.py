import time
import schedule
import webServiceMonitor

# web Montor - Main
print("web Montor Starting...", flush=True)

webServiceMonitor.webServiceHealthCheck()

schedule.every(1).minutes.do(webServiceMonitor.webServiceFailCheck)
schedule.every(10).minutes.do(webServiceMonitor.webServiceHealthCheck)

while True:
    schedule.run_pending()
    time.sleep(60)