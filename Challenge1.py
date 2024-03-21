import numpy as np
import matplotlib.pyplot as plt

class Model():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity       
        self.ux, self.uy = self.resolve(launchSpeed)
        self.h = launchHeight
        self.ypos = []


    def resolve(self, u):
        uy = np.sin(self.launchAngle) * u
        ux = np.cos(self.launchAngle) * u
        return(ux, uy)

    def suvat(self, time: float):
        s = self.uy * time - (self.g * time**2)/2 + self.h
        if s >= 0:
            self.ypos.append(s)
            return time
        else:
            return None

TIMEPERIOD = 0.1

'''

 /|
/ |
---

s = (ut + 1/2 *a *t**2) + h


'''

mod = Model(90, 9.81, 5, 0)
print(mod.ux)
print(mod.uy)

time = 0

time = mod.suvat(time) 

while time != None:
    time += TIMEPERIOD
    time = mod.suvat(time)   
    print(time)


print(mod.ypos)

