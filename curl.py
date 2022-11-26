import urllib.request
import json

class Request:
    def __init__(self, method, url, data=''):
        try:
            header = {'Content-Type': 'application/json'}
            if method == 'PUT' or method == 'POST':
                payload = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(
                    url, data=payload, method=method, headers=header)
            else:
                req = urllib.request.Request(url, headers=header)
            with urllib.request.urlopen(req) as response:
                self.status = response.getcode()
                self.headers = response.getheaders()
                if response.getcode() <= 299:
                    self.body = json.loads(response.read())
        except urllib.error.URLError as e:
            print(e.reason)

