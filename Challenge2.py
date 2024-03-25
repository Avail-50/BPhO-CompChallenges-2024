import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure



class Projectile():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, timePeriod) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity       
        self.ux, self.uy = self.resolve(launchSpeed)
        self.h = launchHeight
        self.ypos = []
        self.xpos = []
        self.timePeriod = timePeriod

    def resolve(self, u):
        uy = np.round(np.sin(self.launchAngle) * u, 2)
        ux = np.round(np.cos(self.launchAngle) * u, 2)
        return(ux, uy)

    def suvat(self, time: float):
        s = self.uy * time - (self.g * time**2)/2 + self.h
        if s >= 0:
            self.ypos.append(s)
            return time
        else:
            return None
        
    def xCoords(self, time):
        self.xpos.append(self.ux * time)

    def simulate(self):
        time = 0
        time = self.suvat(time) 

        while time != None:
            self.xCoords(time)
            time += self.timePeriod
            time = self.suvat(time) 

##### ^From prev challenge. ...Should compbine into 1 UI with multiple pages

## s = ut + a/2t^2 +
## 0 = a/2t^2 + ut + h         
## (-b + sqrt(b**2 - 4ac))/2a          

class detailedProjectile(Projectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, timePeriod):
       
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, timePeriod)
        self.simulate()
        self.t, self.xRange = self.calcRange()
        self.apogee = self.findApogee()
        

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.ux * t
        return t, xRange
    
    def findApogee(self):
        maximum = np.max(self.ypos)
        return self.xpos[self.ypos.index(maximum)], maximum




proj = detailedProjectile(45, 9.8, 20, 3, 0.1)

plt.plot(proj.xpos, proj.ypos)
plt.plot(proj.xpos, proj.ypos, "o")
plt.plot(proj.apogee[0], proj.apogee[1], "x")

plt.show()