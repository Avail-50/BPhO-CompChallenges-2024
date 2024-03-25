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
        label = tk.Label(self, text ="Page 1")
        label.pack(side=tk.BOTTOM)
  
        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="StartPage", command=lambda : controller.show_frame(StartPage))
     
        # putting the button in its place 
        button1.pack(side=tk.BOTTOM)

        fig = Figure(figsize=(6, 6), dpi= 100)
        ax = fig.add_subplot()

        ax.set_xlabel("x /m")
        ax.set_ylabel("y /m")

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
        label = tk.Label(self, text ="Page 2")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        #button1 = tk.Button(self, text ="Page 1", command=lambda : controller.show_frame(Page1))
     
        # putting the button in its place by 
        # using grid
        #button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = tk.Button(self, text ="Startpage", command=lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


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

# Driver Code
app = tkinterApp()
app.mainloop()