# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:25:06 2026

@author: Ferti
"""
import math
import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns): 
    xmin = domain[0] 
    xmax = domain[1] 
    step = (xmax - xmin) / (ns - 1) 
    xs = []
  
    for i in range(ns):
        x = xmin + i*step 
        xs.append(x)
    
    ys = []
   
    for x in (xs): 
        y = eval(fun_str) 
        ys.append(y)
     
    print("x             y")
    print("---------------")

    for i in range(ns):
        print("{:+.4f} {:+.4f}".format(xs[i], ys[i]))
        
    plt.plot(xs, ys)
    
    plt.show()
