import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

# changed to timeProjectile

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
      
mod = Projectile(45, 9.81, 20, 2, 0.02)
mod.simulate()
print(mod.ypos)
