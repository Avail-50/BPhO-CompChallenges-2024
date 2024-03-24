import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


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
      
#mod = Projectile(50, 9.81, 20, 4)
#mod.simulate()

mw = tk.Tk()
mw.title("Projectile: No Air Resistance")

fig = Figure(figsize=(6, 6), dpi= 100)
ax = fig.add_subplot()

ax.set_xlabel("x /m")
ax.set_ylabel("y /m")

canvas = FigureCanvasTkAgg(fig, master=mw)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, mw, pack_toolbar=False)
toolbar.update()

'''
canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)
'''

button_quit = tk.Button(master=mw, text="Quit", command=mw.destroy)

launchAngle_var = tk.IntVar()
gravity_var = tk.IntVar()
launchSpeed_var = tk.IntVar()
launchHieght_var = tk.IntVar()
####
timePeriod_var = tk.StringVar()
####

def submit():
    angle = launchAngle_var.get()
    grav = gravity_var.get()
    speed = launchSpeed_var.get()
    height = launchHieght_var.get()
    tP = timePeriod_var.get()

    mod = Projectile(angle, grav, speed, height, float(tP))
    mod.simulate()
    ax.clear()
    ax.plot(mod.xpos, mod.ypos)
    canvas.draw()

launchAngle_label, launchAngle_entry = tk.Label(mw, text = 'Launch Angle', font=('calibre',10, 'bold')), tk.Entry(mw,textvariable = launchAngle_var, font=('calibre',10,'normal'))
gravity_label, gravity_entry = tk.Label(mw, text = 'Gravity', font=('calibre',10, 'bold')), tk.Entry(mw,textvariable = gravity_var, font=('calibre',10,'normal'))
launchSpeed_label, launchSpeed_entry = tk.Label(mw, text = 'Launch Speed', font=('calibre',10, 'bold')), tk.Entry(mw,textvariable = launchSpeed_var, font=('calibre',10,'normal'))
launchHeight_label, launchHeight_entry = tk.Label(mw, text = 'Launch Height', font=('calibre',10, 'bold')), tk.Entry(mw,textvariable = launchHieght_var, font=('calibre',10,'normal'))

tP_label, tP_entry = tk.Label(mw, text = 'Time Period', font=('calibre',10, 'bold')), tk.Entry(mw,textvariable = timePeriod_var, font=('calibre',10,'normal'))

sub_btn=tk.Button(mw, text = 'Submit', command = submit)


launchAngle_label.pack(side=tk.TOP)
launchAngle_entry.pack(side=tk.TOP)
gravity_label.pack(side=tk.TOP)
gravity_entry.pack(side=tk.TOP)
launchSpeed_label.pack(side=tk.TOP)
launchSpeed_entry.pack(side=tk.TOP)
launchHeight_label.pack(side=tk.TOP)
launchHeight_entry.pack(side=tk.TOP)

tP_label.pack(side=tk.TOP)
tP_entry.pack(side=tk.TOP)

sub_btn.pack(side=tk.TOP)


button_quit.pack(side=tk.BOTTOM)
#slider_update.pack(side=tk.BOTTOM)
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

mw.mainloop()

