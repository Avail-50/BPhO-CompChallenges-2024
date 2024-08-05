import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BouncingProjectile():
    def __init__(self, launchAngle, launchSpeed, launchHeight, n, g=9.81, freq=100):
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

'''
def update(frame):
    x = plot[0][:frame]
    y = plot[1][:frame]
    
    anim.set_xdata(plot[0][:frame])
    anim.set_ydata(plot[1][:frame])

    return anim


        
bounce = BouncingProjectile(45, 5, 10, 6)
plot = bounce.verlet()
fig, ax = plt.subplots()
anim = ax.plot(plot[0][0], plot[1][0])
#plt.plot(plot[0], plot[1], "r-", label="y vs x")


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()
'''

fig, ax = plt.subplots()
bounce = BouncingProjectile(45, 5, 10, 6)
plotx, ploty, t = bounce.verlet()
line2 = ax.plot(plotx[0], ploty[0], "r-")[0]
ball = ax.plot(plotx[0], ploty[0], "go")[0]

ax.set(xlim=[0, 40], ylim=[0, 15], xlabel='x /m', ylabel='y /m')
#ax.legend()

def update(frame):

    # update the line plot:
    line2.set_xdata(plotx[:frame])
    line2.set_ydata(ploty[:frame])

    ball.set_xdata([plotx[frame]])
    ball.set_ydata([ploty[frame]])
    
    return (line2, ball)


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(plotx), interval = 10)
plt.show()

