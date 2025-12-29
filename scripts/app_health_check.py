import requests
import logging
from datetime import datetime

logging.basicConfig(
    filename='app_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'

)

APP_URL = "https://wisecow.local:8443/"

def check_app():
    try:
        response = requests.get(APP_URL, verify=False, timeout=5)
        if response.status_code == 200:
            logging.info(f"Application is UP. Status Code: {response.status_code}")
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            logging.error(f"Application is DOWN! Status Code: {response.status_code}")
            print(f"Application is DOWN! Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN! Exception: {e}")
        print(f"Application is DOWN! Exception: {e}")

if __name__ == "__main__":
    check_app()