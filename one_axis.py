import serial
import numpy as np
from FitCurve import f
import matplotlib.pyplot as plt

arduinoComPort = "/dev/ttyACM0"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

counter = 0
sensorOutputs = []
sensorOutputsArr = np.zeros((45,1))

while (counter < 45):
    lineOfData = serialPort.readline().decode().strip()
    if len(lineOfData) > 0:
        print(lineOfData)
        sensorOutput = int(lineOfData)
        distance = f(sensorOutput)
        sensorOutputsArr[counter][0] = distance
        counter += 1

# Graph heatmap
print(sensorOutputsArr)
plt.imshow(sensorOutputsArr)
plt.colorbar()
plt.show()