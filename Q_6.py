# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:02:50 2020

@author: nabendu
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#function that returns dy/dx
def model(z,x):
    y1=z[0]
    y2=z[1]
    dy1dx=32*y1+66*y2+(2/3)*x+2/3
    dy2dx=-66*y1-133*y2-(1/3)*x-1/3
    return([dy1dx,dy2dx])

#initial conditions
z0=[1/3,1/3]

#x points
x=np.linspace(0,0.5,100)

#solve ODEs
z=odeint(model,z0,x)

y1=z[:,0]
y2=z[:,1]

#plotting results
plt.plot(x,y1,'r',label=r'$y_1$ numerical')
plt.plot(x,y2,'k',label=r'$y_2$')
plt.plot(x,(2*x-np.exp(-100*x)+2*np.exp(-x))/3,'--b',label=r'$y_1$ exact')
plt.plot(x,(-x+2*np.exp(-100*x)-np.exp(-x))/3,'--c',label=r'$y_1$ exact')
plt.xlabel(r'$x$',fontsize=20)
plt.legend()
plt.show()
