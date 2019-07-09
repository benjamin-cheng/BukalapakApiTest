import sys
import json
import requests

headers = {'Content-Type': "application/json; charset=utf-8"}


def get_access_token():
    token_url = 'https://www.bukalapak.com/auth_proxies/request_token'
    token_response = requests.post(token_url, headers=headers)
    print('Get token status code: ' + str(token_response.status_code)
          + ', raise for status: ' + str(token_response.raise_for_status()))
    token_json = json.loads(token_response.text)
    print('Token result:\n' + json.dumps(token_json, indent=4))
    return token_json['access_token']


def print_promotions_json_result(type_name, url, access_token):
    promotions_response = requests.get(url + access_token, headers=headers)
    print('\n')
    print("Get {type_name} promotions status code: {status_code}, raise for status: {raise_for_status}".format(
        type_name=type_name,
        status_code=str(promotions_response.status_code),
        raise_for_status=str(promotions_response.raise_for_status())
    ))
    promotions_json = json.loads(promotions_response.text)
    print("{type_name} promotions result:\n {json_result}".format(
          type_name=type_name,
          json_result=json.dumps(promotions_json, indent=4)
          ))


access_token = get_access_token()

promotions_dict = (
    ('all', 'https://api.bukalapak.com/info/promotions?sort=-start_date&limit=15&offset=0&access_token='),
    ('new user', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=new_user&limit=15&offset=0&access_token='),
    ('item', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=item&limit=15&offset=0&access_token='),
    ('payment', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=payment&limit=15&offset=0&access_token='),
    ('shipping', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=shipping&limit=15&offset=0&access_token='),
    ('voucher', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=vp&limit=15&offset=0&access_token='),
    ('flash deals', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=flash&limit=15&offset=0&access_token='),
    ('brand', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=brand&limit=15&offset=0&access_token='),
    ('finance', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=finance&limit=15&offset=0&access_token='),
    ('others', 'https://api.bukalapak.com/info/promotions?sort=-start_date&type=others&limit=15&offset=0&access_token='),
)

for type_name, url in promotions_dict:
    print_promotions_json_result(type_name, url, access_token)
