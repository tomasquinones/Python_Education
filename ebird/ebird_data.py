# Getting Data From Ebird
# Documentation: https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest#intro
# Audrey's Profile https://ebird.org/profile/NjA0MzYy/world

import json, requests, sys

API_KEY = r4jvqhblq5kb

import requests, json
url = 'https://api.ebird.org/v2/product/top100/US/2020/01/01'
payload = {'X-eBirdApiToken': 'r4jvqhblq5kb'}
r = requests.get(url, params=payload)

r = requests.get('https://api.ebird.org/v2/product/top100/US/2020/01/01?X-eBirdApiToken=r4jvqhblq5kb')

top_100 = r.json()


with open('top_100.json', 'w') as top_lists:
    json.dump(top_100, top_lists)









# https://api.ebird.org/v2/product/top100/{{regionCode}}/{{y}}/{{m}}/{{d}}

# top100 = requests.get(f'{https://api.ebird.org/v2/product/top100/US/2020/01/01}')

# Example # curl --location --request GET 'https://api.ebird.org/v2/product/top100/US/2020/01/01' --header 'X-eBirdApiToken: r4jvqhblq5kb'
url = 'https://api.ebird.org/v2/product/top100/US/2020/01/01'
payload = {'some': 'data'}
headers = {'X-eBirdApiToken': 'r4jvqhblq5kb'}

r = requests.post(url, data=json.dumps(payload), headers=headers)


