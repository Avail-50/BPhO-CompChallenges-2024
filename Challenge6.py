import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


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

    def resolve(self, u):
        uy = np.round(np.sin(self.launchAngle) * u, 2)
        ux = np.round(np.cos(self.launchAngle) * u, 2)
        return(ux, uy)

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.ux * t
        return t, xRange
    
    def simulate(self):
        n = self.xRange/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h)

class apogeeProjectile(freqProjectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq):      
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, freq)
        self.apogee = self.findApogee()       
    
    def findApogee(self):   
        x = (self.uy/self.ux)/(self.g/(self.ux**2))
        y = self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h
        return x, y

class maxRangeProjectile(freqProjectile):
    def __init__(self, gravity, launchSpeed, launchHeight, freq):
        super().__init__(0, gravity, launchSpeed, launchHeight, freq)
        self.launchAngle = self.optimumAngle()
        self.ux, self.uy = self.resolve(launchSpeed)
        self.t, self.xRange = self.calcRange()

    def optimumAngle(self):
        return np.arcsin(1/np.sqrt(2 + 2*self.g*self.h/(self.u**2)))
    
class distanceCalcProj(freqProjectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq):
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, freq)

    def speedOverTime(self):
        #v = np.sqrt((self.uy - self.g*x)**2 + (self.ux)**2)
        pass

    '''
    def findDistance(self):
        z1 = np.tan(self.launchAngle)
        print("z1", z1)
        
        z2 = z1 - ((self.g * self.xRange)/self.u**2) * (1 * z1**2)
        print("z2", z2)
        lim1 = (0.5)*np.log(np.fabs(np.sqrt(1 + z1**2)+z1)) + 0.5*z1*np.sqrt(1 + z1**2)
        lim2 = (0.5)*np.log(np.fabs(np.sqrt(1 + z2**2)+z2)) + 0.5*z2*np.sqrt(1 + z2**2)
        return ((self.u**2)/(self.g*(1+z1**2))) * (lim1 - lim2)
    '''
    
    def findDistanceVer2(self):
        z1 = self.uy - self.g * self.t
        z2 = self.uy
        lim1 = -z1*np.sqrt(self.ux**2 + z1**2)/(2*self.g) - (self.ux**2)/(2*self.g) * np.log(np.fabs((np.sqrt(self.ux**2 + z1**2)+z1))/self.ux)
        lim2 = -z2*np.sqrt(self.ux**2 + z2**2)/(2*self.g) - (self.ux**2)/(2*self.g) * np.log(np.fabs((np.sqrt(self.ux**2 + z2**2)+z2))/self.ux)
        return lim1-lim2

maxProj = maxRangeProjectile(9.81, 10, 2, 100)
maxProj.simulate()

proj = apogeeProjectile(60, 9.81, 10, 2, 100)
proj.simulate()

disProj = distanceCalcProj(60, 9.81, 10, 2, 100)

print(disProj.findDistanceVer2())
plt.style.use("Solarize_Light2")
plt.plot(proj.xpos, proj.ypos, "-", label="y vs x")
plt.plot(proj.apogee[0], proj.apogee[1], "ro", label="apogee")
plt.plot(maxProj.xpos, maxProj.ypos, "--", label="max range")
plt.legend(loc="upper right")


plt.show()
