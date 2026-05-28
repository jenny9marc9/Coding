#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:10:33 2026

@author: marc_o_polo
"""

import numpy as np
import matplotlib.pyplot as plt

L2=np.loadtxt('IERS_14_C04_IAU2000_act.txt',skiprows=14)
L1=L2[:len(L2)-2331]
ns=15
d=len(L1)/ns
dt=int(d)
t=L1[:,3]
x=L1[:,4]
y=L1[:,5]
w1=2*np.pi/365.25
w2=2*np.pi/432.25
a=np.ones((ns+1,1))
for i in range(ns+1):
    a[i]=t[0]+i*dt
A=np.zeros((2*len(L1),6*(ns+1)))
for i in range(ns):
    for k in range(dt):
        n=k+i*dt
        A[n,i]=(a[i+1]-t[n])/dt
        A[n,i+1]=(t[n]-a[i])/dt
        A[n,(ns+1)*2+i]=(a[i+1]-t[n])/dt*np.cos(w1*t[n])
        A[n,(ns+1)*2+i+1]=(t[n]-a[i])/dt*np.cos(w1*t[n])
        A[n,(ns+1)*3+i]=-(a[i+1]-t[n])/dt*np.sin(w1*t[n])
        A[n,(ns+1)*3+i+1]=-(t[n]-a[i])/dt*np.sin(w1*t[n])
        A[n,(ns+1)*4+i]=(a[i+1]-t[n])/dt*np.cos(w2*t[n])
        A[n,(ns+1)*4+i+1]=(t[n]-a[i])/dt*np.cos(w2*t[n])
        A[n,(ns+1)*5+i]=-(a[i+1]-t[n])/dt*np.sin(w2*t[n])
        A[n,(ns+1)*5+i+1]=-(t[n]-a[i])/dt*np.sin(w2*t[n])
    for k in range(dt):
        n=k+i*dt+len(L1)
        p=k+i*dt
        A[n,(ns+1)+i]=-(a[i+1]-t[p])/dt
        A[n,(ns+1)+i+1]=-(t[p]-a[i])/dt
        A[n,(ns+1)*2+i]=-(a[i+1]-t[p])/dt*np.sin(w1*t[p])
        A[n,(ns+1)*2+i+1]=-(t[p]-a[i])/dt*np.sin(w1*t[p])
        A[n,(ns+1)*3+i]=-(a[i+1]-t[p])/dt*np.cos(w1*t[p])
        A[n,(ns+1)*3+i+1]=-(t[p]-a[i])/dt*np.cos(w1*t[p])
        A[n,(ns+1)*4+i]=-(a[i+1]-t[p])/dt*np.sin(w2*t[p])
        A[n,(ns+1)*4+i+1]=-(t[p]-a[i])/dt*np.sin(w2*t[p])
        A[n,(ns+1)*5+i]=-(a[i+1]-t[p])/dt*np.cos(w2*t[p])
        A[n,(ns+1)*5+i+1]=-(t[p]-a[i])/dt*np.cos(w2*t[p])

H=np.zeros((2*(ns),6*(ns+1))) 
for n in range(ns):
    H[n,n]=1
    H[n,n+1]=-2
    H[n,n+2]=1
for k in range(ns):
    n=k+ns
    H[n,n+2]=1
    H[n,n+3]=-2
    H[n,n+4]=1
A1=np.concatenate((A,H))
sigma=14
fs=1
f=50
w=fs*(f*sigma*365/(3*dt))
O=np.identity((2*len(L1)+2*ns))
for n in range(2*ns):
    k=6*(ns+1)
    O[k,k]=sigma**2/w**2
h=np.zeros((2*ns,))
z1=np.concatenate((x,y))
z=np.concatenate((z1,h))
At=np.transpose(A1)
N=At@O@A1
N1=np.linalg.inv(N)
b=At@z
x1=N1@b  
C2=np.array_split(t,ns)
P=np.array_split(x,ns)
Q=np.array_split(y,ns)
TB=t[0]
L5=np.zeros((2354,))
L6=np.zeros((2354,))
fig=plt.figure(figsize=(30,20),dpi=300)
plt.rc("font",size=20)
plt.rc("axes",labelsize=30)
plt.rc("axes",titlesize=30)

for n in range(ns): 
    L=((TB+(n+1)*dt-C2[n])*x1[n]+(C2[n]-(TB+n*dt))*x1[n+1])/dt
    M=((TB+(n+1)*dt-C2[n])*x1[n+ns+1]+(C2[n]-(TB+n*dt))*x1[n+ns+2])/dt
    L0=((TB+(n+1)*dt-C2[n])*x1[n+2*(ns+1)]+(C2[n]-(TB+n*dt))*x1[n+2*(ns+1)+1])/dt
    M0=((TB+(n+1)*dt-C2[n])*x1[n+3*(ns+1)]+(C2[n]-(TB+n*dt))*x1[n+3*(ns+1)+1])/dt
    L1=((TB+(n+1)*dt-C2[n])*x1[n+4*(ns+1)]+(C2[n]-(TB+n*dt))*x1[n+4*(ns+1)+1])/dt
    M1=((TB+(n+1)*dt-C2[n])*x1[n+5*(ns+1)]+(C2[n]-(TB+n*dt))*x1[n+5*(ns+1)+1])/dt
    L3=L+L0*np.cos(w1*C2[n])-M0*np.sin(w1*C2[n])+L1*np.cos(w2*C2[n])-M1*np.sin(w2*C2[n])
    L4=M+M0*np.cos(w1*C2[n])+L0*np.sin(w1*C2[n])+M1*np.cos(w2*C2[n])+L1*np.sin(w2*C2[n])
    """plt.plot(C2[n],L3,"blue")
    plt.plot(C2[n],-L4,"red")
    plt.plot(C2[n],P[n]-L3,"g")
    plt.plot(C2[n],Q[n]+L4,"black")"""
    plt.plot(M,-L,"black")
    plt.plot(L4,-L3,"red")
    """for k in range(2352):
        L5[k+1]=(L[k+2]-L[k])/2
        L6[k+1]=(M[k+2]-M[k])/2
        plt.plot(C2[n],L5,"red")
        plt.plot(C2[n],L6,"green")
        plt.plot(C2[n],np.sqrt(L5**2+L6**2),"black")"""