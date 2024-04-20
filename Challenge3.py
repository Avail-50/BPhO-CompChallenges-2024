import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *


from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


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
        minU = np.sqrt(self.g*(self.xDest**2)/(r*(1 + np.sin(-alpha))))
        minθ = (0.5*np.pi + alpha)/2
        return minU, minθ
    
    def simulate(self):
        n = self.xDest/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        uy = self.minU * np.sin(self.minθ)
        ux = self.minU * np.cos(self.minθ)
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(uy*x/ux - (self.g/2)*(x/ux)**2)


class highLowProjectile():
    def __init__(self, xDest, yDest, gravity, launchSpeed, freq):
        self.xDest, self.yDest = xDest, yDest
        self.freq = freq
        self.g = gravity
        self.u = launchSpeed
        self.high, self.low = self.angles()
        self.lowCoords = self.simulate(self.low)
        self.highCoords = self.simulate(self.high)

    def resolve(self, angle):
        uy = np.round(np.sin(angle) * self.u, 3)
        ux = np.round(np.cos(angle) * self.u, 3)
        return(ux, uy)
        
    def angles(self):
        sqrtDiscriminant = np.sqrt((-2 * (self.u**2) * self.yDest)/(self.g * self.xDest**2) + (self.u**4)/(self.g * self.xDest)**2 - 1)
        high = np.arctan((self.u**2)/(self.g * self.xDest) + sqrtDiscriminant)
        low = np.arctan((self.u**2)/(self.g * self.xDest) - sqrtDiscriminant)
        return high, low
    
    def simulate(self, angle):
        xpos = []
        ypos = []
        uy = self.u * np.sin(angle)
        ux = self.u * np.cos(angle)
        n = self.xDest/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            xpos.append(x)
            ypos.append(uy*x/ux - (self.g/2)*(x/ux)**2)
        return xpos, ypos



missile = trajectoryProjectile(8, 3, 9.81, 40)
missile.simulate()
print(missile.minU)
print(missile.minθ)
angleMissile = highLowProjectile(8, 3, 9.81, 15, 40)
print(angleMissile.high)
print(angleMissile.low)
plt.style.use("Solarize_Light2")
plt.plot(missile.xpos, missile.ypos, "-o", label="minU")
plt.plot(angleMissile.lowCoords[0], angleMissile.lowCoords[1], "-o", label="low")
plt.plot(angleMissile.highCoords[0], angleMissile.highCoords[1], "-o", label="high")
plt.plot(missile.xDest, missile.yDest, "ro", label="Target")
plt.legend(loc="upper right")

plt.show()
