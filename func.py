# libs
import requests
import os

# header to scan
headers = {
    'Host': 'ping.com'
}

def url(url, head=None, cookies=None):  # main func of scan
    if head:
        r = requests.get(url, headers={'Host': head})
    elif cookies:
        r = requests.get(url, headers={'Host': 'ping.com',
        'Cookies': cookies})
    elif head and cookies:
        r = requests.get(url, headers={'Host': head,
        'Cookies': cookies})
    else:
        r = requests.get(url, headers=headers)

    if r.status_code == 200:
        print(f'url has host header injection\n {url}')
    else:
        print(f'url does not have host header injection\n {url}')

# checks if the file exist
def check_file_existence(file_path):
    return os.path.exists(file_path)