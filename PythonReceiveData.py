import serial
import numpy as np
import math
from FitCurve import f
import matplotlib.pyplot as plt

arduinoComPort = "/dev/ttyACM1"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
 
total_pan_degrees = 46
total_tilt_degrees = 64
counter = 0
sensorOutputArr = np.zeros((total_pan_degrees,total_tilt_degrees))
sensorOutputs = []

while (counter < ((total_pan_degrees) / (1) * (total_tilt_degrees) / (2))):
  lineOfData = serialPort.readline().decode().strip()
  if len(lineOfData) > 0:
    print(lineOfData)
    data = lineOfData.split("/") 
    if len(data) == 3:
      panPos = int(data[0])
      tiltPos = int(data[1])
      sensorOutput = int(data[2])
      distance = f(sensorOutput)

      sensorOutputArr[panPos][tiltPos] = distance
      sensorOutputs.append((panPos,tiltPos, distance))
      counter += 1

xs = []
ys = []
zs = []

for i in sensorOutputs:
  theta = math.radians(i[0])
  phi = math.radians(i[1])
  rho = i[2]

  x = rho * math.sin(phi) * math.cos(theta)
  y = rho * math.sin(phi) * math.sin(theta)
  z = rho * math.cos(phi)
  xs.append(x)
  ys.append(y)
  zs.append(z)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the 3D scatter plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(xs, ys, zs)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Plot the 2D heatmap
cax = ax2.imshow(sensorOutputArr, cmap='viridis', aspect='auto')
ax2.set_title('2D Heatmap')
fig.colorbar(cax, ax=ax2)

# Display the plot
plt.tight_layout()
plt.show()

