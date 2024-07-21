import requests
import logging

# Set up logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Application URL
APP_URL = 'https://en.wikipedia.org/wiki/Flower'

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = 'up'
        else:
            status = 'down'
        log_status(status, response.status_code)
        return status
    except requests.exceptions.RequestException as e:
        log_status('down', str(e))
        return 'down'

def log_status(status, detail):
    message = f"Application is {status}. Detail: {detail}"
    print(message)
    logging.info(message)

def main():
    status = check_application_health(APP_URL)
    print(f"Application status: {status}")

if __name__ == "__main__":
    main()
