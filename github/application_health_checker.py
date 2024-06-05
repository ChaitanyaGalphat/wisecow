import requests
import logging

# Configure logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the application URL and the expected status code
APP_URL = 'http://example.com'
EXPECTED_STATUS_CODE = 200

def check_application_health(url, expected_status_code):
    try:
        response = requests.get(url)
        if response.status_code == expected_status_code:
            logging.info(f'Application is up. Status code: {response.status_code}')
            print(f'Application is up. Status code: {response.status_code}')
        else:
            logging.warning(f'Application is down. Status code: {response.status_code}')
            print(f'Alert: Application is down. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking application health: {e}')
        print(f'Alert: Error checking application health: {e}')

if __name__ == "__main__":
    check_application_health(APP_URL, EXPECTED_STATUS_CODE)
    print("Application health check complete. Check 'application_health.log' for details.")
