import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class Projectile():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity       
        self.ux, self.uy = self.resolve(launchSpeed)
        self.h = launchHeight
        self.ypos = []
        self.xpos = []
        self.timePeriod = 0.1

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
      
mod = Projectile(50, 9.81, 20, 4)
mod.simulate()

def graph(x: list, y: list):
    plt.plot(x, y)
    plt.title("Distance of Projectile")
    plt.xlabel("x /m")
    plt.ylabel("y /m")
    plt.show()

graph(mod.xpos, mod.ypos)

'''
mw = tk.Tk()

mw.title("Projectile: No Air Resistance")

mw.mainloop()
'''