#!
import json, requests, sys

# Ride with GPS Info
API_KEY = 'aa49d17b'
AUTH_TOKEN = '26a71f681dceeca317b8b092395ef839'
USER_ID = '45898'
EMAIL = 'tomas.quinones@gmail.com'
PASSWORD = 'GetRiding1!'


# get_user_info = requests.get(f'https://ridewithgps.com/users/current.json?email={EMAIL}&password={PASSWORD}&apikey={API_KEY}&version=2')
# user_info = get_user_info.json()


# with open('user_info.json', 'w') as json_file:
#   json.dump(user_info, json_file)


# GET /users/{id}/trips.json

get_trips = requests.get(f'https://ridewithgps.com/users/{USER_ID}/trips.json?auth_token={AUTH_TOKEN}&apikey={API_KEY}&version=3')
user_trips = get_trips.json()

with open('user_trips.json', 'w') as trips_file:
    json.dump(user_trips, trips_file)

