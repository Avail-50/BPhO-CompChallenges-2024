import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *


from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top") 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = tk.Label(self, text ="Startpage")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
  
        button1 = tk.Button(self, text ="Page 1", command=lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Page 2", command=lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Challenge 1")
        label.pack(side=tk.TOP)
  
        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="StartPage", command=lambda : controller.show_frame(StartPage))
     
        # putting the button in its place 
        button1.pack(side=tk.BOTTOM)

        fig = Figure(figsize=(6, 6), dpi= 100)
        ax = fig.add_subplot()

        ax.set_xlabel("x /m")
        ax.set_ylabel("y /m")
        ax.set_aspect("equal")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
        toolbar.update()


        launchAngle_var = tk.IntVar()
        gravity_var = tk.IntVar()
        launchSpeed_var = tk.IntVar()
        launchHieght_var = tk.IntVar()

        timePeriod_var = tk.StringVar()

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
            ax.set_xlabel("x /m")
            ax.set_ylabel("y /m")
            ax.set_aspect("equal")
            canvas.draw()

        launchAngle_label, launchAngle_entry = tk.Label(self, text = 'Launch Angle', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchAngle_var, font=('calibre',10,'normal'))
        gravity_label, gravity_entry = tk.Label(self, text = 'Gravity', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = gravity_var, font=('calibre',10,'normal'))
        launchSpeed_label, launchSpeed_entry = tk.Label(self, text = 'Launch Speed', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchSpeed_var, font=('calibre',10,'normal'))
        launchHeight_label, launchHeight_entry = tk.Label(self, text = 'Launch Height', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchHieght_var, font=('calibre',10,'normal'))

        tP_label, tP_entry = tk.Label(self, text = 'Time Period', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = timePeriod_var, font=('calibre',10,'normal'))

        sub_btn=tk.Button(self, text = 'Submit', command = submit)


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


        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
  
  
  
  
# third window frame page2
class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Challenge 2")
        label.pack(side=tk.TOP)
  
        button1 = tk.Button(self, text ="Startpage", command=lambda : controller.show_frame(StartPage))
        button1.pack(side=tk.BOTTOM)

        fig = Figure(figsize=(6, 6), dpi= 100)
        ax = fig.add_subplot()

        ax.set_xlabel("x /m")
        ax.set_ylabel("y /m")
        ax.set_aspect("equal")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
        toolbar.update()


        launchAngle_var = tk.IntVar()
        gravity_var = tk.IntVar()
        launchSpeed_var = tk.IntVar()
        launchHieght_var = tk.IntVar()

        frequency_var = tk.IntVar()

        def submit():

            angle = launchAngle_var.get()
            grav = gravity_var.get()
            speed = launchSpeed_var.get()
            height = launchHieght_var.get()
            freq = frequency_var.get()

            dP = detailedProjectile(angle, grav, speed, height, freq)
            dP.simulate()
            ax.clear()

            range_label.config(text="Range = "+ str(np.round(dP.xRange, 3)))
            airTime_label.config(text="Air Time = "+ str(np.round(dP.t, 3)))
            apogee_label.config(text="Apogee = ["+ str(np.round(dP.apogee[0], 3)) + ", " +str(np.round(dP.apogee[1], 3))+"]")

            ax.plot(dP.xpos, dP.ypos, "-o", label="y vs x")
            ax.plot(dP.apogee[0], dP.apogee[1], "ro", label="apogee")
            ax.set_xlabel("x /m")
            ax.set_ylabel("y /m")
            ax.set_aspect("equal")
            ax.legend(loc="upper right")
            
            
            canvas.draw()
        
        launchAngle_label, launchAngle_entry = tk.Label(self, text = 'Launch Angle', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchAngle_var, font=('calibre',10,'normal'))
        gravity_label, gravity_entry = tk.Label(self, text = 'Gravity', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = gravity_var, font=('calibre',10,'normal'))
        launchSpeed_label, launchSpeed_entry = tk.Label(self, text = 'Launch Speed', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchSpeed_var, font=('calibre',10,'normal'))
        launchHeight_label, launchHeight_entry = tk.Label(self, text = 'Launch Height', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchHieght_var, font=('calibre',10,'normal'))

        tP_label, tP_entry = tk.Label(self, text = 'Frequency', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = frequency_var, font=('calibre',10,'normal'))

        sub_btn=tk.Button(self, text = 'Submit', command = submit)


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


        range_label = tk.Label(self, text=("Range ="), font=('calibre',20, 'bold'))
        airTime_label = tk.Label(self, text=("Air Time ="), font=('calibre',20, 'bold'))
        apogee_label = tk.Label(self, text=("Apogee ="), font=('calibre',20, 'bold'))
        range_label.pack(side=tk.TOP)
        airTime_label.pack(side=tk.TOP)
        apogee_label.pack(side=tk.TOP)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        

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

class detailedProjectile(Projectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq):
       
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, 0)
        self.t, self.xRange = self.calcRange()
        self.apogee = self.findApogee()
        self.freq = freq
        

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.ux * t
        return t, xRange
    
    ##redo
    def findApogee(self):   
        #y = self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2
        #dy/dx = self.uy/self.ux - self.g/self.ux**2 * x
        #(self.uy/self.ux)/(2*self.g/self.ux**2) = x
        x = (self.uy/self.ux)/(self.g/(self.ux**2))
        y = self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h
        return x, y

    
    def simulate(self):
        n = self.xRange/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h)


# Driver Code
app = tkinterApp()
app.mainloop()