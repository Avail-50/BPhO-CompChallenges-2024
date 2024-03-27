import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *


from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

class trajectoryProjectile():
    def __init__(self, xDest, yDest, g) -> None:
        self.xDest = xDest
        self.yDest = yDest
        self.g = g

    def findMinU(self):
        # uy = usin(θ)   ux = ucos(θ)

        #y = self.uy*x/self.ux - self.g*(x/self.ux)**2
        #dy/dx = self.uy/self.ux - 2*self.g/self.ux**2 * x
        #(self.uy/self.ux)/(2*self.g/self.ux**2) = x

         
        pass

'''
s = yDest
u = uy
v
a = g
t

xDest = ux*t

0 =  uy/ux * xDest -g*(xDest/ux)**2 -yDest
'''