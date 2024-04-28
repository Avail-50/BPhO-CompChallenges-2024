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
    

maxProj = maxRangeProjectile(9.81, 10, 1, 50)
maxProj.simulate()

proj = apogeeProjectile(15, 9.81, 10, 1, 50)
proj.simulate()
plt.style.use("Solarize_Light2")
plt.plot(proj.xpos, proj.ypos, "-o", label="y vs x")
plt.plot(proj.apogee[0], proj.apogee[1], "ro", label="apogee")
plt.plot(maxProj.xpos, maxProj.ypos, "-o", label="max range")
plt.legend(loc="upper right")


plt.show()
