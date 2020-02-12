#!
import json
import requests

# Ride with GPS Info
api_key = 'aa49d17b'
auth_token = '26a71f681dceeca317b8b092395ef839'
tqUserId = '45898'
base_url = 'https://ridewithgps.com/'


api_userRides = requests.get('https://ridewithgps.com/users/45898/trips.json')
userRides = api_userRides.json()

print(userRides)

#for r in userRides['']:
#    print(r['']['name'])
