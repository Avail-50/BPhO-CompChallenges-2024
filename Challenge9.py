import numpy as np
import matplotlib.pyplot as plt

class freqProjectile():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity       
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
      
    def xCoords(self, time):
        self.xpos.append(self.ux * time)

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.getXFromT(t)
        return t, xRange
    
    def getYFromX(self, x):
        return self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h
    
    def getXFromT(self, t):
        return t * self.ux
    
    def simulate(self):
        n = self.xRange/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(self.getYFromX(x))

class apogeeProjectile(freqProjectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq):      
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, freq)
        self.apogee = self.findApogee()       
    
    def findApogee(self):   
        x = (self.uy/self.ux)/(self.g/(self.ux**2))
        y = self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h
        return x, y
    

class DragProjectile(apogeeProjectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq, dragCoefficient=0.1, area=0.07854, aDensity=1, mass=0.1):      
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, freq)
        self.deltaT = 1/freq
        self.k = (0.5*dragCoefficient*aDensity*area)/mass
        self.u = launchSpeed
        self.x_coords, self.y_coords = [], []


    def verlet(self):
        self.x_coords = [0]
        self.y_coords = [self.h]
        vx = self.ux
        vy = self.uy
        v = self.u   
        ax = -(vx/v)*self.k*v**2
        ay = -self.g -(vy/v)*self.k*v**2

        while self.y_coords[-1] >= 0:

            self.x_coords.append(self.x_coords[-1] + vx*self.deltaT + 0.5*ax*self.deltaT**2)
            self.y_coords.append(self.y_coords[-1] + vy*self.deltaT + 0.5*ay*self.deltaT**2)

            vx += ax*self.deltaT
            vy += ay*self.deltaT
            v = np.sqrt(vx**2 + vy**2)

            ax = -(vx/v)*self.k*v**2
            ay = -self.g -(vy/v)*self.k*v**2
            

        return self.x_coords, self.y_coords

normal = apogeeProjectile(30, 9.81, 20, 2, 100)
normal.simulate()

dragProj = DragProjectile(30, 9.81, 20, 2, 100)
xPoints, yPoints = dragProj.verlet()

#print(dragProj.apogee)
    
plt.plot(xPoints, yPoints, "-", label="y vs x")
plt.plot(normal.xpos, normal.ypos)



plt.show()