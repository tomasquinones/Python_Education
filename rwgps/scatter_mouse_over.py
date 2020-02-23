# Scatter with mouse over

import plotly.graph_objects as go
import numpy as np
import json

with open("user_trips.json", "r") as read_file:
    data = json.load(read_file)

tripCount = list(range(0, 50))
tripDistances = []
tripDistancesMiles = []
tripElevations = []
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

# Plotly 
fig = go.Figure(data=go.Scatter(
    y=tripDistancesMiles,
    x=tripCount,
    mode='markers',
    marker=dict(
        size=tripElevations,
        color=tripElevations, #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True,
    ), 
    text=tripData,
))

fig.show()