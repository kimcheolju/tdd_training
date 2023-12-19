import requests

def HealthCheck(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
