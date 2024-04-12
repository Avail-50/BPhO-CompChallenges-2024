import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *


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

class detailedProjectile(Projectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq):
       
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, 0)
        self.t, self.xRange = self.calcRange()
        self.apogee = self.findApogee()
        self.freq = freq
        

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.ux * t
        return t, xRange
    
    def findApogee(self):   
        x = (self.uy/self.ux)/(2*self.g/(self.ux**2))
        y = self.uy*x/self.ux - self.g*(x/self.ux)**2
        return x, y

    
    def simulate(self):
        n = self.xRange/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(self.uy*x/self.ux - self.g*(x/self.ux)**2)

class trajectoryProjectile():
    def __init__(self, xDest, yDest, g, freq) -> None:
        self.xDest = xDest
        self.yDest = yDest
        self.g = g
        self.freq = freq
        self.minU, self.minθ = self.findMin()
        self.ypos = []
        self.xpos = []


    def findMin(self):
        # uy = usin(θ)   ux = ucos(θ)
        #harmonic formula
        r = np.sqrt(self.xDest**2 + self.yDest**2)
        alpha = np.arctan(self.yDest/self.xDest)
        minU = np.sqrt(self.g*(self.xDest**2)/(r*(1 + np.sin(-alpha))/2))
        minθ = (0.5*np.pi + alpha)/2
        return minU, minθ
    
    def simulate(self):
        n = self.xDest/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        uy = self.minU * np.sin(self.minθ)
        ux = self.minU * np.cos(self.minθ)
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(uy*x/ux - self.g*(x/ux)**2)

'''
class highLowProjectile():
    def __init__(self, xDest, yDest, gravity, launchSpeed, freq):
        self.xDest, self.yDest = xDest, yDest
        self.freq = freq
        self.g = gravity
        self.u = launchSpeed
        self.ypos = []
        self.xpos = []

    def high(self):
        pass
'''


missile = trajectoryProjectile(3, 2, 9.8, 20)
missile.simulate()
plt.style.use("Solarize_Light2")
plt.plot(missile.xpos, missile.ypos, "-o", label="minU: y vs x")
plt.plot(missile.xDest, missile.yDest, "ro", label="Target")
plt.legend(loc="upper right")

plt.show()
