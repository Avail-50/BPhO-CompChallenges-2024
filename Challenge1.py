import numpy as np
import matplotlib.pyplot as plt

class Projectile():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity       
        self.ux, self.uy = self.resolve(launchSpeed)
        self.h = launchHeight
        self.ypos = []
        self.xpos = []

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

TIMEPERIOD = 0.01


mod = Projectile(70, 9.81, 5, 4)
print(mod.ux)
print(mod.uy)


time = 0

time = mod.suvat(time) 

while time != None:
    mod.xCoords(time)
    time += TIMEPERIOD
    time = mod.suvat(time) 
      
    print(time)


print(mod.ypos)
print(mod.xpos)

print(len(mod.xpos), "," , len(mod.ypos))

plt.plot(mod.xpos, mod.ypos)
plt.title("Distance of Projectile")
plt.xlabel("x /m")
plt.ylabel("y /m")
plt.show()
