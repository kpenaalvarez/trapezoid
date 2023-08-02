# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:39:33 2023

@author: 16617
"""
import numpy as np

def MCint(f, a, b, n):
    """
    
    Parameters
    ----------
    f : TYPE function
        f returns a float between a and b
    a : TYPE float 
        DESCRIPTION. lower limit
    b : TYPE float
        DESCRIPTION. upper limit
    n : TYPE int
        DESCRIPTION, number of random points to take in the box

    Returns
    -------
    integral of f from a to b

    """

    from random import random
 
    # random returns a random number betwee 0 and 1
    
    maxF = 2
    
    area = 0
    saveX = []
    saveY = []
    for i in range(n):
        
        #generate a random point in the boxc
        #x between a and b
        #z between 0 and maxF
        randNoX = random()*(b-a)+a
        randNoY = random()*maxF
        saveX.append(randNoX)
        saveY.append(randNoY)
        
        if randNoY <= f(randNoX): area += 1
        
    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    print(min(saveX), max(saveX))
    print(min(saveY), max(saveY))
    return(integral)

def trapz(f, a, b, n):
    h = 1/n
    x = np.linspace(a, b, (n+1))
    intsum = 0
    for i in range((n+1)):
        if i == 0 or i == n:
            intsum += f(x[i])/2
        else:
            intsum += f(x[i])
            
    intsum *= h
    return intsum
    
if __name__ == "__main__":
    
    #import numpy as np    
    #import matplotlib.pyplot as plt
    
    def f(x) :
        return x**2
    
    area = MCint(f, 0.5, 2., 500000)
    
    print(round(area, 2))    
    print(f"integ = {area: 0.2f}")
    
    area2 = trapz(f, 0, 1, 100)
    
    print(area2)

