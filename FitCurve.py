"""
A script to fit a curve to the calibration data.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Calibration Curve Fitting
points = pd.read_csv("calibration_data.csv")
df = points.values

x = np.array(df[:, 2])
y = np.array(df[:, 1])

z = np.polyfit(x, y, 5)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

# Plot the fitted curve f with the points

# plt.plot(x,y,'o', x_new, y_new)
# plt.xlim([x[0]-1, x[-1] + 1])
# plt.xlabel('Analog Voltage Reading')
# plt.ylabel('Distance (cm)')

# plt.show()
