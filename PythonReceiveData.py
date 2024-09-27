import serial
import numpy as np
import math
from FitCurve import f
import matplotlib.pyplot as plt

arduinoComPort = "/dev/ttyACM1"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
 
total_pan_degrees = 46
total_tilt_degrees = 70
counter = 0
sensorOutputArr = np.zeros((total_pan_degrees,total_tilt_degrees))
sensorOutputs = []
# sensorOutputArr = np.random.randint(0, 560, (91,91))

while (counter < ((total_pan_degrees) / (1) * (total_tilt_degrees) / (2))):
  lineOfData = serialPort.readline().decode().strip()
  if len(lineOfData) > 0:
    # Serial lines are in the format: [panPos]/[tiltPos]/[sensorOutput] \n
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

"""
cartesianPointsArr = np.zeros(sensorOutputArr.shape)
for i in range(len(cartesianPointsArr)):
  for j in range(len(cartesianPointsArr)):
    
    rho = sensorOutputArr[i][j]
    theta = math.radians(i)
    phi = math.radians(j)
    # Conver from Spherical Coordinates to Cartesian
    x = rho * math.sin(phi) * math.cos(theta)
    y = rho * math.sin(phi) * math.sin(theta)
    z = rho * math.cos(phi)
    # cartesianPointsArr[i][j] = (x,y,z) # Set the pan-tilt degree index to be the coordinates in x,y,z


    if x < 20 and y < 10:
      continue
    else:
      xs.append(x)
      ys.append(y)
      zs.append(z)

"""

for i in sensorOutputs:
  rho = i[0]
  theta = math.radians(i[1])
  phi = math.radians(i[2])

  x = rho * math.sin(phi) * math.cos(theta)
  y = rho * math.sin(phi) * math.sin(theta)
  z = rho * math.cos(phi)
  xs.append(x)
  ys.append(y)
  zs.append(z)


# Graph a scatterplot of the object in 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(xs, ys, zs)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
