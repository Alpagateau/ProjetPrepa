import sys
import numpy as np
import matplotlib.pyplot as plt
import time

M = []
explored = []

MAX = 999

def removeValues(i, j, L):
    if i < j:
        L.pop(j)
        L.pop(i)
    if j < i:
        L.pop(i)
        L.pop(j)
    return L

def funct(L):
    global M, explored, MAX
    if len(L) < 2:
        return
    if L in explored:
        print(L, " ", end="")
        return
    #half search + *
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if i == j:
                j+=1
            #addition
            n = L[i] + L[j]
            if n < MAX:
                ad = L.copy()
                removeValues(i, j, ad)
                ad += [n]
                ad.sort()
                if n not in M:
                    M += [n]
                funct(ad)
                if len(ad)>1:
                    explored += [ad]

            #multiplication
            if not L[i] == 1 and not L[j] == 1:
                n = L[i] * L[j]
                if n < MAX:
                    mu = L.copy()
                    removeValues(i,j,mu)
                    mu += [n]
                    mu.sort()
                    if n not in M:
                        M += [n]
                    funct(mu)
                    if len(mu)>1:
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
                su.sort()
                if n not in M:
                    M += [n]
                funct(su)
                explored += [su]
            
            #division
            if L[j] == 1:
                continue
            if L[j] == 0 or L[i] == 0:
                continue
            if L[i] % L[j] == 0:
                di = L.copy()
                n = di[i] // di[j]
                removeValues(i , j, di)
                di += [n]
                di.sort()
                if n not in M:
                    M += [n]
                funct(di)
                explored += [di]

t = time.time()
#7.788s 990
#funct([2,3,4,5,5,6])
funct([1,2,3,4,5,6,7])
M.sort()
print("")
print(M)
print("took ", time.time() - t, " seconds")

"""
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
"""
#environs 1/2 * exp(x)