# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:46:30 2022

@author: johnf
"""

import numpy as np
import matplotlib.pyplot as plt

x0=np.array([1,1,1,1,1])
x1=np.array([1,3.5,6,9,10])
y=np.array([1,1,0,0,0])

th0=0
th1=-1
theta=np.array([th0,th1])
print("theta=",theta)
print(theta.shape)
X=np.array([x0,x1])
print("X=",X)
print(X.shape) 
#h=1/(1+np.exp(-np.dot(theta.T,X)))
h=1/(1+np.exp(-theta[0]*X[0]-theta[1]*X[1]))
print("h=",h)
print(h.shape)
print("y",y)
print(y.shape)

m=len(x1)
alfa=0.1

plt.plot(x1,y,"+")
xg=np.arange(0,10,0.1)
hg=1/(1+np.exp(-theta[0]-theta[1]*xg))
plt.xlabel("x")
plt.ylabel("y")
g,=plt.plot(xg,hg)

for i in range(100000):  
    theta=theta-alfa*np.array([sum((h-y)*X[0]),sum((h-y)*X[1])])
    h=1/(1+np.exp(-theta[0]*X[0]-theta[1]*X[1]))
    hg=1/(1+np.exp(-theta[0]-theta[1]*xg))
    g,=plt.plot(xg,hg,"b")
    plt.pause(0.001)
    g.remove()
    print(theta)
print(theta)


