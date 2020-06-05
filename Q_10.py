# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:45:59 2020

@author: nabendu
"""

#Problem 10
#Fourier Transform of box function using numpy

import numpy as np
import cmath
import matplotlib.pyplot as plt

#The given box function 
def f(x):
    if(abs(x)<1):
        return(1.0)
    else:
        return(0.0)

#limit of x for which we want to sample f(x) 
xmin=-16.0
xmax=16.0

numpoints=[128,256,512]                             #total number of points at which we want to sample f(x)

k_arr=[]

aft_arr=[]

for p in range(3):
    dx=(xmax-xmin)/(numpoints[p]-1)              #sampling rate 

    sampled_data=np.zeros(numpoints[p])
    xarr=np.zeros(numpoints[p])

    #sampling f(x)
    for i in range(numpoints[p]):
        sampled_data[i]=f(xmin+i*dx)         #sampling of f(x)
        xarr[i]=xmin+i*dx                    #sample points
    
    #DFT of the sample
    nft=np.fft.fft(sampled_data, norm='ortho')

    #The k array
    karr=np.fft.fftfreq(numpoints[p], d=dx)
    karr=2*np.pi*karr

    #The factor due to the fact that xmin is not equal to zero
    factor=np.exp(-1j*karr*xmin)

    #Transforming DFT to FT
    aft=np.real(dx*np.sqrt(numpoints[p]/(2.0*np.pi))*factor*nft)
    
    k_arr.append(karr)
    
    aft_arr.append(aft)

x=np.linspace(-16,16,1000)
f_arr=np.zeros(1000)
for m in range(1000):
    f_arr[m]=f(x[m])
plt.plot(x,f_arr,'r') 
plt.xlabel(r'$x$',fontsize=16)
plt.ylabel(r'$f(x)$',fontsize=16)
plt.xlim(-5.0,5.0)
plt.show()

#plotting the FTs
plt.plot(k_arr[0],aft_arr[0],'r',label=r'numpoints=256')
plt.plot(k_arr[1],aft_arr[1],'b',label=r'numpoints=512') 
plt.plot(k_arr[2],aft_arr[2],'g',label=r'numpoints=1024') 
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.legend()
plt.show()
