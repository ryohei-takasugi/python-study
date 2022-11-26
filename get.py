import urllib.request
import json


class Curl:
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


dic = {
    'nico': 'https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search?q=%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF&targets=title&fields=contentId,title,viewCounter&_sort=-viewCounter&_offset=0&_limit=3&_context=apiguide'
}

nico = Curl('GET', dic['nico'])

print('status: {}'.format(nico.status))
print('headers: {}'.format(json.dumps(nico.headers, indent=6)))
print('meta: {}'.format(json.dumps(nico.body['meta'], indent=6)))
print('data[0]: {}'.format(json.dumps(nico.body['data'][0], indent=6)))
print('data[1]: {}'.format(json.dumps(nico.body['data'][1], indent=6)))
print('data[2]: {}'.format(json.dumps(nico.body['data'][2], indent=6)))
