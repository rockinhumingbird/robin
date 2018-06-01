# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:13:40 2018
Rice University Exam2 function
@author: soviv
"""
#1
def cube_root(val):
    """
    Given number, return the cube root of the number
    """
    return val ** (1 / 3)

print (cube_root(27,0.333))

##define two variables value
def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))

#3
def project_to_distance(point_x,point_y,distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)

print (project_to_distance(2, 7, 4))

#print statements can appear anywhere in your program and print a specified value(s)
#Note that execution of your Python program continues onward to the following
#Remember that executing print statement inside a function definition does not return a value from the function.
#return statements appear inside functions. 
#The value associated with the return statement is substituted for the expression that called the function. 
#Note that executing a return statement terminates execution of 
#the function definition immediately. Any statements in the function definition following the return statement are ignored. 

def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())


#5find the max of 4 functions
def f(x):
    return x**5*(-5)+ (x**2)*67-47

max(f(0),f(1),f(2),f(3))


#The equation FV = PV (1+rate)^{periods} FV=PV(1+rate) periodsrelates the following four quantities.
def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value*(1+rate_per_period)**periods
    

print("$1000 at 2% compounded daily for 4 years yields $", future_value(500,.04,10,10))

#7equilateral triangle area
import math
def f(x):
    return x**2*math.sqrt(3)/4
f(5)

