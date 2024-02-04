import sys
import numpy as np
import matplotlib.pyplot as plt

M = []
explored = []

def removeValues(i, j, L):
    if i < j:
        L.pop(j)
        L.pop(i)
    if j < i:
        L.pop(i)
        L.pop(j)
    return L

def funct(L):
    global M, explored
    if len(L) < 2:
        return
    if L in explored:
        return
    #half search + *
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if i == j:
                continue
            #addition
            ad = L.copy()
            n = ad[i] + ad[j]
            if n < 200:
                removeValues(i, j, ad)
                ad += [n]
                if n not in M:
                    M += [n]
                funct(ad)
                explored += [ad]

            #multiplication
            mu = L.copy()
            if not mu[i] == 1 and not mu[j] == 1:
                n = mu[i] * mu[j]
                if n < 200:
                    removeValues(i,j,mu)
                    mu += [n]
                    if n not in M:
                        M += [n]
                    funct(mu)
                    explored += [mu]
    #full search - /
    for i in range(len(L)):
        for j in range(len(L)-1):
            if i == j:
                j+=1
            #substraction
            n = L[i] - L[j]
            if n > 0:
                su = L.copy()
                removeValues(i,j,su)
                su += [n]
                if n not in M:
                    M += [n]
                funct(su)
                explored += [su]
            
            #division
            di = L.copy()
            if di[j] == 1:
                continue
            if di[j] == 0 or di[i] == 0:
                continue
            if di[i] % di[j] == 0:
                n = di[i] / di[j]
                removeValues(i , j, di)
                di += [n]
                if n not in M:
                    M += [n]
                funct(di)
                explored += [di]

funct([2,3,4,5,5])
print(M)


v = []
n = 7
for i in range(n):
    L = (np.arange(i+1)*2).tolist()
    M = [] + L
    for j in range(n):
        if j < i:
            print("##", end="")
        else: 
            print("--", end='')
    print('')
    funct(L)
    v += [len(M)]
print(v)
plt.plot(v)
plt.show()
#environs 1/2 * exp(x)