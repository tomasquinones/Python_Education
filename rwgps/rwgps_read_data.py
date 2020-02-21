# Count the Trips in riderData.json

import json

with open("user_trips.json", "r") as read_file:
    data = json.load(read_file)

totalMeters = 0.0

for x in data['results'][0:100]:
    if x["distance"] == None:
        continue
    totalMeters = totalMeters + x["distance"]

totalMeters = int(totalMeters)

# print(allDistances)
print (f'Total Distance in Meters: {totalMeters:,}')

totalKilometers = totalMeters // 1000
print (f'Total Distance in Kilometers: {totalKilometers:,}')

totalMiles = totalMeters // 1609.34
print(f'Total Distance in Miles: {totalMiles:,}')

ride_id = []
for x in data['results'][0:100]:
    ride_id.append(x["id"])

# A list of the first 100 ride IDs
print(ride_id)
