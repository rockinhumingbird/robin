"""
Examples of creating and using anonymous functions.
"""

import random

# Easily create a list of numbers
data = list(range(10))
print("range data:", data)

def square(val):
    return val ** 2

# Square all numbers in the list
squares = list(map(square, data))
print("squares:", squares)

# Double all numbers in the list
doubles = list(map(lambda num: num * 2, data))
print("doubles:", doubles)

# Create a list of random numbers (list comprehension)
randnums = [random.randrange(2, num+3) for num in range(10)]
print("random numbers:", randnums)

# Create a list of tuples
tups = list(map(lambda num1, num2: (num1, num2), data, randnums))
print("tuples:", tups)

# Create a list of the min values in the tuples
mins = list(map(lambda pair: min(pair[0], pair[1]), tups))
print("minimums:", mins)

# Create a list only of tuples where the second item is less than the first
newtups = list(filter(lambda pair: pair[1] < pair[0], tups))
print("filtered:", newtups)
"""
More advanced sorting examples.
"""

import random

# Easily create a shuffled list of numbers
data = list(range(10))
random.shuffle(data)
print("shuffled data:", data)

# Sort the list of numbers
data.sort()
print("ascending sort:", data)
data.sort(reverse=True)
print("descending sort:", data)

# Create a list of tuples
datatups = [(item, random.randrange(3, 15)) for item in data]
print("data tuples:", datatups)

# Sort the list
datatups.sort()
print("sorted data tuples:", datatups)

datatups.sort(key=lambda pair: pair[1])
print("sorted by second item:", datatups)

datatups.sort(key=lambda pair: pair[0] * pair[1], reverse=True)
print("sorted by product:", datatups)

# Shuffle it again
random.shuffle(datatups)
print("shuffled tuples:", datatups)

# Use sorted to sort the list
newdata = sorted(datatups, key=lambda pair: pair[1], reverse=True)
print("tuples after sorted:", datatups)
print("returned from sorted:", newdata)


def convert_list2dict(gpalist):
    """
    Input: gpalist - list of (student name, gpa) tuples
    Output: a dictionary mapping student names to their gpa
    """
    result = {}
    for item in gpalist:
        result[item[0]] = item[1]
    return result


"""
Converting the average daily temperatures for several planets 
from Kelvin to Farenheit --- Version 0
"""


# Initialize emperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
mercury_result = (mercury - 275.15) * 9 / 5 + 32
venus_result = (venus - 275.15) * 9 / 5 + 32
mars_result = (mars - 275.15) * 9 / 5 + 32

# Print
print("The daily average temperature on Mercury is", mercury_result, "Farenheit")
print("The daily average temperature on Venus is", venus_result, "Farenheit")
print("The daily average temperature on Mars is", mars_result, "Farenheit")

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit


"""
Converting the average daily temperatures for several planets 
from Kelvin to Farenheit --- Version 1
"""


# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
mercury = 440
venus = 737
mars = 210

# Compute temperature in Farenheit
def compute_temp(temp):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    return (temp - 275.15) * 9 / 5 + 32

mercury_result = compute_temp(mercury)
venus_result = compute_temp(venus)
mars_result = compute_temp(mars)

# Print out results
print("The daily average temperature on Mercury is", mercury_result, "Farenheit")
print("The daily average temperature on Venus is", venus_result, "Farenheit")
print("The daily average temperature on Mars is", mars_result, "Farenheit")

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit

"""
Converting the average daily temperatures for several planets 
from Kelvin to Farenheit --- Version 4
"""


# Initialize temperatures for various planets
# http://www.smartconversion.com/otherInfo/Temperature_of_planets_and_the_Sun.aspx
MERCURY_KELVIN = 440
VENUS_KELVIN = 737
MARS_KELVIN = 210

# Compute temperature in Farenheit
def kelvin_to_celsius(temp_kelvin):
    """
    Given a floaring point temperature temp in Kelvin,
    return the corresponding temperature in Celsius
    """
    return temp_kelvin - 275.15

def kelvin_to_farenheit(temp_kelvin):
    """
    Given a floating point temperature temp in Kelvin,
    return the corresponding temperature in Farenheit
    """
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    return temp_celsius * 9 / 5 + 32

mercury_farenheit = kelvin_to_farenheit(MERCURY_KELVIN)
venus_farenheit = kelvin_to_farenheit(VENUS_KELVIN)
mars_farenheit = kelvin_to_farenheit(MARS_KELVIN)

# Print out results
def print_temp_farenheit(planet, temp_farenheit):
    """
    Print out the average daily temps in Farenheit
    """
    print("The daily average temperature on", planet, "is", temp_farenheit, "Farenheit")
    
print_temp_farenheit("Mercury", mercury_farenheit)
print_temp_farenheit("Venus", venus_farenheit)
print_temp_farenheit("Mars", mars_farenheit)

# Output
##The daily average temperature on Mercury is 328.73 Farenheit
##The daily average temperature on Venus is 863.33 Farenheit
##The daily average temperature on Mars is -85.27 Farenheit