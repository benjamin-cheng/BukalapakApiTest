import sys
import json
import requests

headers = {'Content-Type': "application/json; charset=utf-8"}

token_url = 'https://www.bukalapak.com/auth_proxies/request_token'
token_response = requests.post(token_url, headers=headers)
print('Get token status code: ' + str(token_response.status_code))
print('Raise for status: ' + str(token_response.raise_for_status()))
print('Token result:\n' + token_response.text)
token_json = json.loads(token_response.text)
access_token = token_json['access_token']

promotions_url = 'https://api.bukalapak.com/info/promotions?sort=-start_date&limit=15&offset=0&access_token='
promotions_response = requests.get(promotions_url, headers=headers)
print('\n')
print('Get promotions status code:' + str(promotions_response.status_code))
print('Raise for status:' + str(promotions_response.raise_for_status()))
print('Promotions result:\n' + promotions_response.text)
