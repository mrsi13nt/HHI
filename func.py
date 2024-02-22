# func.py
import requests

headers = {
    'Host': 'ping.com'
}

def url(url, head=None):  # Set a default value for head to None
    if head:
        r = requests.get(url, headers={'Host': head})
    else:
        r = requests.get(url, headers=headers)

    if r.status_code == 200:
        print(f'url has host header injection\n {url}')
    else:
        print(f'url does not have host header injection\n {url}')
