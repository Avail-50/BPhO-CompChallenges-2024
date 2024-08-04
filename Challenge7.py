import numpy as np
import matplotlib.pyplot as plt


def rangePerTime(u, g, theta):
    theta = theta * np.pi/180
    discriminant = np.sin(theta)**2 - 8/9
    if discriminant >= 0:
        tMax = 3*u * (np.sin(theta) + np.sqrt(discriminant))/(2*g)
        rMax = np.sqrt(u**2 * tMax**2 - g* tMax**3 * u * np.sin(theta) + 0.25*g**2 * tMax**4)
        tMin = 3*u * (np.sin(theta) - np.sqrt(discriminant))/(2*g)
        rMin = np.sqrt(u**2 * tMin**2 - g* tMin**3 * u * np.sin(theta) + 0.25*g**2 * tMin**4)
        maximum = [tMax, rMax]
        minimum = [tMin, rMin]
    else:
        maximum = None
        minimum = None
    end = 3
    t = np.linspace(0, end)
    r = []
    for i in t:
        r.append(np.sqrt(u**2 * i**2 - g* i**3 * u * np.sin(theta) + 0.25*g**2 * i**4))
    return t, r, maximum, minimum


vals = rangePerTime(10, 9.81, 70.53)
plt.plot(vals[0], vals[1], "-", label="y vs x")
if vals[2] != None:
    plt.plot(vals[2][0], vals[2][1], "rx")
    plt.plot(vals[3][0], vals[3][1], "bx")



plt.show()