# encoding: utf-8
"""
    获取baidu token
"""
import requests
import json

App_ID = '7845111'
API_Key = 'LgijcySFqmhzAFq32IoH9VGh'
Secret_Key = 'f51777bfd9ea44b5d0b6a1b133d6de36'

def get_token():
    """
    参考 http://developer.baidu.com/wiki/index.php?title=docs/oauth/client
    :return:
    """
    url = 'https://openapi.baidu.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': API_Key,
        'client_secret': Secret_Key,
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        res = json.loads(r.text)
        if 'error' in res:
            print(res['error_description'])
            return ""
        return res['access_token']
    return ''

TOKEN = get_token()
