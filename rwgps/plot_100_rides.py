# trip scatter plot

# TODO: X is the number of rides
# TODO: Y is the distance of the rides
# TODO: SIZE is the elevation gain
# TODO: color is the amount of time
# TODO EXTRA: Hover_name = Ride Name, Date, Distance, Elevation, Time, Start City

# y = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 10, 20, 30, 40, 50, 15, 25, 35, 45, 55]

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = 45
y = 24
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()