# Getting Started with Plotly

import plotly.graph_objects as go
import json

with open("user_trips.json", "r") as read_file:
    data = json.load(read_file)


tripCount = list(range(0, 50))
tripDistances = [] # List of 50 distances in meters
tripDistancesMiles = [] # List of 50 distances converted to Miles
tripElevations = [] # List of 50 trip
tripData = []

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


fig = go.Figure(data=go.Bar(y=tripDistancesMiles))
fig.show()


fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig.show()