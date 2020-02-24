# Plotly 
import plotly.express as px
import numpy as np
import json

with open("user_trips.json", "r") as read_file:
    data = json.load(read_file)

tripCount = list(range(0, 50))
tripDistances = []
tripDistancesMiles = []
tripElevations = []
tripData = []
tripGear = []
gearList = []

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
    tripData.append(x['name'])

for x in data['results']:
    if x not in tripGear:
        tripGear.append(x['gear_id'])

for i in tripGear:
    if i not in gearList:
        gearList.append(i)

df = px.data.iris()

fig = px.scatter_matrix(df, dimensions=gearList, color="species")

fig.show()