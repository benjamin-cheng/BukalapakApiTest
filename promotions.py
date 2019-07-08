import json
import requests

url = 'https://www.bukalapak.com/auth_proxies/request_token'
headers = {'Content-Type': "application/json; charset=utf-8"}
res = requests.post(url, headers=headers)
print (res.status_code)
print (res.raise_for_status())
print (res.text)
j = json.loads(res.text)
print (j['access_token'])

url2 = "https://api.bukalapak.com/info/promotions?sort=-start_date&limit=15&offset=0&access_token=" + j['access_token']
headers2 = {'Content-Type': "application/json; charset=utf-8"}
res2 = requests.get(url2, headers=headers2)
print (res2.status_code)
print (res2.raise_for_status())
print (res2.text)