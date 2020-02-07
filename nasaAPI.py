#!
import requests

# Nasa's Open Notify API

# request = requests.get('http://api.open-notify.org')
# print(request.text)

people = requests.get('http://api.open-notify.org/astros.json')
#print(people.text)

people_json  = people.json()
# print(people_json)

for p in people_json['people']:
    print(p['name'])
