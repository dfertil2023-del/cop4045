# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import matplotlib.pyplot as plt 

while True:
    a_input = input("Enter a: ")
    if a_input == "":
        break
    a = float(a_input)
    
    b_input = input("Enter b: ")
    b = float(b_input)
    
    c_input = input("Enter c: ")
    c = float(c_input)
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("no real solutions")
        xpot = (-b)/(2*a)
        xmin = xpot - 2
        xmax = xpot + 2 
    elif discriminant == 0:
        x1 = -b/(2*a)
        xmin = x1 - 2
        xmax = x1 + 2
        print("one real solution:", x1)
    elif discriminant > 0:
        x1 = ( -b - math.sqrt(discriminant))/(2*a) 
        x2 = ( -b + math.sqrt(discriminant))/(2*a)
        print("two real solutions:", x1, x2)
        
        xmin = min(x1, x2) - 2
        xmax = max(x1, x2) + 2
        
    xs = []
    ys = []
    step = (xmax - xmin)/(149)
    for i in range(150):
        x = xmin + i*step
        xs.append(x) 
        y = a*x**2 + b*x + c
        ys.append(y)
    plt.clf()   
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Qadratic Function")
    plt.show()