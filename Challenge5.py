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

class boundingParabola():
    def __init__(self, gravity, launchSpeed, launchHeight, freq) -> None:
        self.g = gravity
        self.u = launchSpeed
        self.h = launchHeight
        self.freq = freq

    def bound(self):
        xMax = np.sqrt(((self.u**4)/self.g + 2*self.h*self.u**2)/self.g)
        xpos = np.linspace(0, xMax, self.freq)
        ypos = list(((self.u**2)/(2*self.g) - self.g*x**2/(2*self.u**2) + self.h) for x in xpos)
        return xpos, ypos
    
p = boundingParabola(9.81, 40, 5, 20)
print(p.bound())