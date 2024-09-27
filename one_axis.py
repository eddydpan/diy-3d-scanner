import serial
import numpy as np
import math
from FitCurve import f
import matplotlib.pyplot as plt

arduinoComPort = "/dev/ttyACM0"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

counter = 0
sensorOutputs = []
# sensorOutputArr = np.random.randint(0, 560, (91,91))
sensorOutputsArr = np.zeros((45,1))

while (counter < 45):
    lineOfData = serialPort.readline().decode().strip()
    if len(lineOfData) > 0:
        # Serial lines are in the format: [panPos]/[tiltPos]/[sensorOutput] \n
        print(lineOfData)
        sensorOutput = int(lineOfData)
        distance = f(sensorOutput)
        sensorOutputsArr[counter][0] = distance
        counter += 1

# xs = []
# ys = []
# zs = []    

# for i in sensorOutputs:
#   rho = i[0]
#   theta = math.radians(i[1])
#   phi = math.radians(i[2])

#   x = rho * math.sin(phi) * math.cos(theta)
#   y = rho * math.sin(phi) * math.sin(theta)
#   z = rho * math.cos(phi)
#   xs.append(x)
#   ys.append(y)
#   zs.append(z)


# Graph a scatterplot of the object in 3D
print(sensorOutputsArr)
plt.imshow(sensorOutputsArr)
plt.colorbar()

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(xs, ys, zs)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
plt.show()
