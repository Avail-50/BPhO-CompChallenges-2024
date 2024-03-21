import numpy as np
import matplotlib.pyplot as plt

class Model():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity       
        self.ux, self.uy = self.resolve(launchSpeed)
        self.h = launchHeight

    def resolve(self, u):
        uy = np.sin(self.launchAngle) * u
        ux = np.cos(self.launchAngle) * u
        return(ux, uy)

    def suvat(self):
        pass

'''

 /|
/ |
---

'''

mod = Model(0, 9.81, 5, 0)
print(mod.ux)
print(mod.uy)