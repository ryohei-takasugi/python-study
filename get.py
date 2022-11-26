import json
import curl

dic = {
    'nico': 'https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search?q=%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF&targets=title&fields=contentId,title,viewCounter&_sort=-viewCounter&_offset=0&_limit=3&_context=apiguide'
}

nico = curl.Request('GET', dic['nico'])

print('status: {}'.format(nico.status))
print('headers: {}'.format(json.dumps(nico.headers, indent=6)))
print('meta: {}'.format(json.dumps(nico.body['meta'], indent=6)))
print('data[0]: {}'.format(json.dumps(nico.body['data'][0], indent=6)))
print('data[1]: {}'.format(json.dumps(nico.body['data'][1], indent=6)))
print('data[2]: {}'.format(json.dumps(nico.body['data'][2], indent=6)))
