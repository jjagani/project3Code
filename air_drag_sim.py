import math
import matplotlib.pyplot as plt
import numpy as np

"""
Sources
https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/rktvrecv.html#:~:text=The%20drag%20equation%20states%20that,the%20reference%20area%20(A).
https://www.youtube.com/watch?v=3AIA1HBsTVI&t=422

Assumptions:
Egg falls in a straight line
"""

def calcAccel(Cd, A, rho, v, payload, g):
    a = ((payload * g) - (0.5 * rho * math.pow(v,2) * Cd * A)) / payload
    return a


dt = 0.01 #timestep for simulation in seconds
payload = 1 #Mass of payload (kg)
rho = 1.229 #Air density at sea level
Cd = 1.1 #Drag Coefficient of object
A = 1 #Cross sectional area of object in airflow
g = 9.8 #gravitational constant (m/s^2)
h = -11.4 #drop height (in meters)
v = 0.4 #initial velocity of payload (m/s)
t = 0;
xpoints = [] #time variable during descent
apoints = [] #acceleration during descent
vpoints = [] #velocity during descent
hpoints = [] #height during descent
while(h < 0):
    a = calcAccel(Cd, A, rho, v, payload, g)
    v += a * dt;
    h +=  v * dt + 0.5 * a * pow(dt,2)
    xpoints.append(t)
    apoints.append(a)
    vpoints.append(v)
    hpoints.append(h)
    t+=dt

print("Final Acceleration" , a)
print("Final Velocity", v)
print("Final Height", h)
print('Final time', t)

plt.plot(xpoints, apoints, color = 'green')
plt.plot(xpoints, vpoints, color = 'red')
plt.plot(xpoints, hpoints, color = 'blue')
plt.show()

print("Done")