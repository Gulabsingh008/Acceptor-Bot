import requests
import time

url = "https://open-dragonfly-vonex-c2746ec1.koyeb.app"

while True:
    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
    
    time.sleep(20)
