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
        for F in (StartPage, Page1, Page2, Page3, Page4):
  
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
  
        button1 = tk.Button(self, text ="Challenge 1", command=lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Challenge 2", command=lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        button3 = tk.Button(self, text ="Challenge 3", command=lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)

        button4 = tk.Button(self, text ="Challenge 4", command=lambda : controller.show_frame(Page4))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10)


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

            mod = timeProjectile(angle, grav, speed, height, float(tP))
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

            dP = apogeeProjectile(angle, grav, speed, height, freq)
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

# fourth window frame page3
class Page3(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Challenge 3")
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


        gravity_var = tk.IntVar()
        launchSpeed_var = tk.IntVar()
        #launchHieght_var = tk.IntVar()
        x_var = tk.IntVar()
        y_var = tk.IntVar()

        frequency_var = tk.IntVar()

        def submit():

            xTarget = x_var.get()
            yTarget = y_var.get()
            grav = gravity_var.get()
            speed = launchSpeed_var.get()
            #height = launchHieght_var.get()
            freq = frequency_var.get()

            minUProjectile = trajectoryProjectile(xTarget, yTarget, grav, freq)
            minUProjectile.simulate()
            highLowAngles = highLowProjectile(xTarget, yTarget, grav, speed, freq)

            ax.clear()


            minU_label.config(text="Min U = "+ str(np.round(minUProjectile.minU, 3)))
            minUAngle_label.config(text="Min U θ = "+ str(np.round(minUProjectile.minθ, 3)))
            highAngle_label.config(text="High Angle = "+ str(np.round(highLowAngles.high, 3)))
            lowAngle_label.config(text="Low Angle = "+ str(np.round(highLowAngles.low, 3)))
            
            ax.plot(highLowAngles.lowCoords[0], highLowAngles.lowCoords[1], "-o", label="low")
            ax.plot(highLowAngles.highCoords[0], highLowAngles.highCoords[1], "-o", label="high")
            ax.plot(minUProjectile.xpos, minUProjectile.ypos, "-o", label="min U")
            ax.plot(minUProjectile.xDest, minUProjectile.yDest, "rx", label="Target")
            ax.set_xlabel("x /m")
            ax.set_ylabel("y /m")
            ax.set_aspect("equal")
            ax.legend(loc="upper right")
            
            
            canvas.draw()
        
        target_label, targetX_entry, targetY_entry = tk.Label(self, text = 'Target (x, y)', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = x_var, font=('calibre',10,'normal')), tk.Entry(self,textvariable = y_var, font=('calibre',10,'normal'))
        gravity_label, gravity_entry = tk.Label(self, text = 'Gravity', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = gravity_var, font=('calibre',10,'normal'))
        launchSpeed_label, launchSpeed_entry = tk.Label(self, text = 'Launch Speed', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchSpeed_var, font=('calibre',10,'normal'))
        #launchHeight_label, launchHeight_entry = tk.Label(self, text = 'Launch Height', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = launchHieght_var, font=('calibre',10,'normal'))

        freq_label, freq_entry = tk.Label(self, text = 'Frequency (no. of data points)', font=('calibre',10, 'bold')), tk.Entry(self,textvariable = frequency_var, font=('calibre',10,'normal'))

        sub_btn=tk.Button(self, text = 'Submit', command = submit)


        target_label.pack(side=tk.TOP)
        targetX_entry.pack(side=tk.TOP)
        targetY_entry.pack(side=tk.TOP)
        gravity_label.pack(side=tk.TOP)
        gravity_entry.pack(side=tk.TOP)
        launchSpeed_label.pack(side=tk.TOP)
        launchSpeed_entry.pack(side=tk.TOP)
        #launchHeight_label.pack(side=tk.TOP)
        #launchHeight_entry.pack(side=tk.TOP)

        freq_label.pack(side=tk.TOP)
        freq_entry.pack(side=tk.TOP)

        sub_btn.pack(side=tk.TOP)


        minU_label = tk.Label(self, text=("Min U ="), font=('calibre',20, 'bold'))
        minUAngle_label = tk.Label(self, text=("Min U θ = "), font=('calibre',20, 'bold'))
        highAngle_label = tk.Label(self, text=("High Angle = "), font=('calibre',20, 'bold'))
        lowAngle_label = tk.Label(self, text=("Low Angle = "), font=('calibre',20, 'bold'))
        minU_label.pack(side=tk.TOP)
        minUAngle_label.pack(side=tk.TOP)
        highAngle_label.pack(side=tk.TOP)
        lowAngle_label.pack(side=tk.TOP)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# fifth window frame page3
class Page4(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Challenge 4")
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

            fP = freqProjectile(angle, grav, speed, height, freq)
            fP.simulate()
            mrP = maxRangeProjectile(grav, speed, height, freq)
            mrP.simulate()
            ax.clear()

            range_label.config(text="Max Range = "+ str(np.round(mrP.xRange, 3)))
            airTime_label.config(text="Max Air Time = "+ str(np.round(mrP.t, 3)))
            maxTheta_label.config(text="Max θ = "+ str(np.round(mrP.launchAngle * 180/np.pi, 1)))

            ax.plot(fP.xpos, fP.ypos, "-o", label="θ = "+str(angle)+"°")
            ax.plot(mrP.xpos, mrP.ypos, "--", label="Max range")
            
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


        range_label = tk.Label(self, text=("Max Range ="), font=('calibre',15, 'bold'))
        airTime_label = tk.Label(self, text=("Max Air Time ="), font=('calibre',15, 'bold'))
        maxTheta_label = tk.Label(self, text=("Max θ = "), font=('calibre',15, 'bold'))
        range_label.pack(side=tk.TOP)
        airTime_label.pack(side=tk.TOP)
        maxTheta_label.pack(side=tk.TOP)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class timeProjectile():
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

class freqProjectile():
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq) -> None:
        self.launchAngle = launchAngle * np.pi/180
        self.g = gravity
        self.u = launchSpeed       
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

    def calcRange(self):
        #quadratic formula rearanged
        t = (self.uy + np.sqrt(self.uy**2 + 2*self.g*self.h))/self.g
        xRange = self.ux * t
        return t, xRange
    
    def simulate(self):
        n = self.xRange/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h)

class apogeeProjectile(freqProjectile):
    def __init__(self, launchAngle, gravity, launchSpeed, launchHeight, freq):      
        super().__init__(launchAngle, gravity, launchSpeed, launchHeight, freq)
        self.apogee = self.findApogee()       
    
    def findApogee(self):   
        x = (self.uy/self.ux)/(self.g/(self.ux**2))
        y = self.uy*x/self.ux - (self.g/2)*(x/self.ux)**2 + self.h
        return x, y
    
class trajectoryProjectile():
    def __init__(self, xDest, yDest, g, freq) -> None:
        self.xDest = xDest
        self.yDest = yDest
        self.g = g
        self.freq = freq
        self.minU, self.minθ = self.findMin()
        self.ypos = []
        self.xpos = []


    def findMin(self):
        # uy = usin(θ)   ux = ucos(θ)
        #harmonic formula
        r = np.sqrt(self.xDest**2 + self.yDest**2)
        alpha = np.arctan(self.yDest/self.xDest)
        minU = np.sqrt(self.g*(self.xDest**2)/(r*(1 + np.sin(-alpha))))
        minθ = (0.5*np.pi + alpha)/2
        return minU, minθ
    
    def simulate(self):
        n = self.xDest/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        uy = self.minU * np.sin(self.minθ)
        ux = self.minU * np.cos(self.minθ)
        for x in xGenerator:
            self.xpos.append(x)
            self.ypos.append(uy*x/ux - (self.g/2)*(x/ux)**2)


class highLowProjectile():
    def __init__(self, xDest, yDest, gravity, launchSpeed, freq):
        self.xDest, self.yDest = xDest, yDest
        self.freq = freq
        self.g = gravity
        self.u = launchSpeed
        self.high, self.low = self.angles()
        self.lowCoords = self.simulate(self.low)
        self.highCoords = self.simulate(self.high)

    def resolve(self, angle):
        uy = np.round(np.sin(angle) * self.u, 3)
        ux = np.round(np.cos(angle) * self.u, 3)
        return(ux, uy)
        
    def angles(self):
        sqrtDiscriminant = np.sqrt((-2 * (self.u**2) * self.yDest)/(self.g * self.xDest**2) + (self.u**4)/(self.g * self.xDest)**2 - 1)
        high = np.arctan((self.u**2)/(self.g * self.xDest) + sqrtDiscriminant)
        low = np.arctan((self.u**2)/(self.g * self.xDest) - sqrtDiscriminant)
        return high, low
    
    def simulate(self, angle):
        xpos = []
        ypos = []
        uy = self.u * np.sin(angle)
        ux = self.u * np.cos(angle)
        n = self.xDest/self.freq
        xGenerator = (n * i for i in range(self.freq+1))
        for x in xGenerator:
            xpos.append(x)
            ypos.append(uy*x/ux - (self.g/2)*(x/ux)**2)
        return xpos, ypos

class maxRangeProjectile(freqProjectile):
    def __init__(self, gravity, launchSpeed, launchHeight, freq):
        super().__init__(0, gravity, launchSpeed, launchHeight, freq)
        self.launchAngle = self.optimumAngle()
        self.ux, self.uy = self.resolve(launchSpeed)
        self.t, self.xRange = self.calcRange()

    def optimumAngle(self):
        return np.arcsin(1/np.sqrt(2 + 2*self.g*self.h/(self.u**2)))

# Driver Code
app = tkinterApp()
app.mainloop()