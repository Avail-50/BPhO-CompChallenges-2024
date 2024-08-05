import numpy as np
import matplotlib.pyplot as plt

class freqProjectile():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity
        self.u = launchSpeed       
        self.ux, self.uy = self.resolve(launchSpeed)
        self.h = launchHeight
        self.ypos = []
        self.xpos = []
        self.freq = freq
        self.t, self.xRange = self.calcRange()
        self.pathLength = self.findDistance()

    def resolve(self, u):
        uy = np.round(np.sin(self.launchAngle) * u, 2)
        ux = np.round(np.cos(self.launchAngle) * u, 2)
        return(ux, uy)

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.ux * t
        return t, xRange
    
    def getYFromX(self, x):
        return self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h
    
    def simulate(self):
        n = self.xRange/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(self.getYFromX(x))

    def findDistance(self):
        z1 = self.uy - self.g * self.t
        z2 = self.uy
        lim1 = -z1*np.sqrt(self.ux**2 + z1**2)/(2*self.g) - (self.ux**2)/(2*self.g) * np.log(np.fabs((np.sqrt(self.ux**2 + z1**2)+z1))/self.ux)
        lim2 = -z2*np.sqrt(self.ux**2 + z2**2)/(2*self.g) - (self.ux**2)/(2*self.g) * np.log(np.fabs((np.sqrt(self.ux**2 + z2**2)+z2))/self.ux)
        return lim1-lim2

def rangePerTime(u, g, theta):
    theta = theta * np.pi/180
    discriminant = np.sin(theta)**2 - 8/9
    if discriminant >= 0:
        tMax = 3*u * (np.sin(theta) - np.sqrt(discriminant))/(2*g)
        rMax = np.sqrt(u**2 * tMax**2 - g* tMax**3 * u * np.sin(theta) + 0.25*g**2 * tMax**4)
        tMin = 3*u * (np.sin(theta) + np.sqrt(discriminant))/(2*g)
        rMin = np.sqrt(u**2 * tMin**2 - g* tMin**3 * u * np.sin(theta) + 0.25*g**2 * tMin**4)
        maximum = [tMax, rMax]
        minimum = [tMin, rMin]
        end = minimum[0] + 0.5 * minimum[0]
        if end < 4:
            end = 4
    else:
        maximum = None
        minimum = None
        end = 4
    
    t = np.linspace(0, end)
    r = []
    for i in t:
        r.append(np.sqrt(u**2 * i**2 - g* i**3 * u * np.sin(theta) + 0.25*g**2 * i**4))
    return t, r, maximum, minimum


vals = rangePerTime(20, 9.81, 80)

plt.plot(vals[0], vals[1], "-", label="y vs x")
if vals[2] != None:
    plt.plot(vals[2][0], vals[2][1], "rx")
    plt.plot(vals[3][0], vals[3][1], "bx")



plt.show()