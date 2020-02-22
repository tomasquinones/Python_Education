import matplotlib.pyplot as plt
import json

with open("user_trips.json", "r") as read_file:
    data = json.load(read_file)

tripCount = list(range(0, 50))
tripDistances = []
tripDistancesMiles = []
tripElevations = []

# Pulling trip distances from user_trips.json
for x in data['results']:
    tripDistances.append(x['distance'])

# Convert the trip distances from meters to KM
for x in tripDistances:
    tripDistancesMiles.append(x / 1609.34)

# Pulling trip distances from user_trips.json
for x in data['results']:
    tripElevations.append(x['elevation_gain'])

# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(tripCount, tripDistancesMiles, s=tripElevations, c=tripElevations, cmap=plt.cm.Paired, alpha=0.50)

# scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=12)

# Labels
ax.set_xlabel(r'Trip Numbers', fontsize=10)
ax.set_ylabel(r'Distance in Miles', fontsize=10)
ax.set_title('First 50 Trips', fontsize=20)

plt.show()