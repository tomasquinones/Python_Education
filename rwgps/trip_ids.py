# Count the Trips in riderData.json

import json

with open("riderData.json", "r") as read_file:
    data = json.load(read_file)


"""
# Creates a list of ride IDs
ride_id = []
for x in data:
    ride_id.append(x["id"])

"""