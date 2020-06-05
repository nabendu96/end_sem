# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:04:59 2020

@author: nabendu
"""

#question_8
#solving boundary value problem #relaxation method

import numpy as np
import matplotlib.pyplot as plt

#boundary conditions
x0=0
y0=0
xf=1
yf=2

N=100     #number of mesh points

x=np.linspace(x0,xf,N)

h=(xf-x0)/(N-1)

target=0.00001      #target accuracy 

y=np.zeros(N)
y[0]=y0
y[-1]=yf

solutions=[]

yprime=np.zeros(N)

count=0

#finding solution using relaxation
for m in range(1000000):
    for i in range(N):
        if(i==0 or i==N-1):
            yprime[i]=y[i]
        else:
            yprime[i]=(y[i+1]+y[i-1]+4*h*h*x[i])/(2+4*h*h)
    delta=max(abs(y-yprime))
    for j in range(N):
        y[j]=yprime[j]
    if(delta<target):       #checking accuracy condition
        break

yexact=x+(np.exp(2)*(np.exp(2*x)-np.exp(-2*x)))/(np.exp(4)-1)        #exact solution

plt.plot(x,y,'r',label=r'numerical result')                     #numerical solution
plt.plot(x,yexact,'--b',label=r'exact solution')                #exact solution
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.show()

#calculating the relative % errors
yerr=np.zeros(N)
#due to relaxation method
yerr[0]=0
yerr[-1]=0

for k in range(N-2): 
    yerr[k+1]=(abs(y[k+1]-yexact[k+1])/yexact[k+1])*100

print('The relative % errors at each x step are \n',yerr)
