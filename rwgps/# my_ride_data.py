# my_ride_data

class my_ride_data:
    def tripData
        tripCount = list(range(0, 50))
        tripDistances = []
        tripDistancesMiles = []
        tripElevations = []
        tripName = []

# Pulling trip distances from user_trips.json
for x in data['results']:
    tripDistances.append(x['distance'])

# Convert the trip distances from meters to KM
for x in tripDistances:
    tripDistancesMiles.append(x / 1609.34)

# Pulling trip distances from user_trips.json
for x in data['results']:
    tripElevations.append((x['elevation_gain'] * 3.28084) / 10 )

for x in data['results']:
    tripName.append(x['name'])