import numpy as np
import matplotlib.pyplot as plt

class BouncingProjectile():
    def __init__(self, launchAngle, launchSpeed, launchHeight, n, g=9.81, freq=250):
        self.theta = launchAngle * np.pi/180
        self.ux, self.uy = self.resolve(launchSpeed)
        self.y_0 = launchHeight
        self.freq = freq
        self.g = g
        self.deltaT = 1/freq
        self.C = 0.7
        self.n = n

    def resolve(self, u):
        uy = np.round(np.sin(self.theta) * u, 2)
        ux = np.round(np.cos(self.theta) * u, 2)
        return(ux, uy)
    
    def verlet(self):
        x_coords = [0]
        y_coords = [self.y_0]
        vy = self.uy
        t = 0
        bounceN = 0

        while bounceN <= self.n:
            x_coords.append(x_coords[-1] + self.ux*self.deltaT)
            y_coords.append(y_coords[-1] + vy*self.deltaT - 0.5*self.g*self.deltaT**2)
            vy -= self.g*self.deltaT
            t += self.deltaT

            if y_coords[-1] < 0:
                y_coords[-1] = 0
                vy *= -self.C
                bounceN += 1
        
        return x_coords, y_coords, t
        
bounce = BouncingProjectile(45, 5, 10, 6)
plot = bounce.verlet()
plt.plot(plot[0], plot[1], "r-", label="y vs x")
print(plot[2])


plt.show()



