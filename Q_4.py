# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:25:55 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

n=1024

#uniformly distributed random numbers between 0 and 1
x=np.random.random(n)

plt.plot(x,'.')
plt.xlabel(r'n',fontsize=16)
plt.ylabel(r'$x_n$',fontsize=16)
plt.show()

#computing dft (without normalization)
dft=np.fft.fft(x)

P=np.abs(dft)**2/n         #power spectrum using Periodogram estimator

#k array
karr=np.fft.fftfreq(n,d=1)
karr=2*np.pi*karr
kmax=np.amax(karr)
kmin=np.amin(karr)
print('maximum and minimum value of k are respectively',kmax,'and',kmin)

plt.plot(karr,P)
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'Power spectrum',fontsize=16)
plt.show()

plt.hist(P,bins=5)
plt.xlabel(r'Power spectrum',fontsize=16)
plt.ylabel(r'Occurance',fontsize=16)
plt.show()

#plotting power spectrum in 5 k bins
k_span=int(kmax-kmin)
bins=5
width=k_span/bins
lower_bound=kmin
upper_bound=kmax

karr1=np.linspace(kmin,kmax,bins+1)

P_bin=np.zeros(bins)  
k_bin=np.zeros(bins)      


for i in range(bins):
	count=0
	for j in range(len(karr)):
		if(karr1[i]<=karr[j]<karr1[i+1]):
			P_bin[i]+=P[j]
			count+=1
	P_bin[i]=P_bin[i]/count	
	k _bin[i]=karr1[i]+(karr1[i+1]-karr1[i])/2

plt.bar(k_bin,P_bin,width)
plt.xlabel(r'binned k',fontsize=16)
plt.ylabel(r'binned power spectrum',fontsize=16)
plt.show()
