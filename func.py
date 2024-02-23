# libs
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os

# Suppress only the InsecureRequestWarning caused by skipping certificate verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# header to scan
headers = {
    'Host': 'ping.com'
}

def url(url, head=None, cookies=None):  # main func of scan
    try:
        if head:
            r = requests.get(url, headers={'Host': head}, verify=False)
        elif cookies:
            r = requests.get(url, headers={'Host': 'ping.com', 'Cookies': cookies}, verify=False)
        elif head and cookies:
            r = requests.get(url, headers={'Host': head, 'Cookies': cookies}, verify=False)
        else:
            r = requests.get(url, headers=headers, verify=False)

        if r.status_code == 200:
            print(f'url has host header injection\n {url}')
        else:
            print(f'url does not have host header injection\n {url}')

    except requests.exceptions.SSLError as e:
        print(f"SSL Certificate Verification Error: {e}")
        # Handle SSL certificate verification error as needed

# checks if the file exists
def check_file_existence(file_path):
    return os.path.exists(file_path)
