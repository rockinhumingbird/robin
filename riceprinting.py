# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 12:07:23 2018

@author: soviv
"""
"""
Simple string literal examples.
"""
# Strings are enclosed in quotes
name = 'ZoeRatatouille'
university = "Hofstra"

print(name)
print(university)

# Multiline strings use triple quotes
address = '''hOFSTRA University
'''

# First Fig by Edna St. Vincent Millay
poem = """My candle burns at both ends;
  It will not last the night;
But ah, my foes, and oh, my friends---
  It gives a lovely light!
"""

print("")

print("Address")
print("=======")
print(address)

print("First Fig")
print("=========")
print(poem)


# Characters \t=tab
chars = "abc'DEF*&$"
print(chars)
chars2 = '\t"abc"\ndef\''
print(chars2)

# String "arithmetic"
print("Concatenating strings")
name_and_uni = name + " " + university
print(name_and_uni)

print("")
print("")
print("Repeating strings")
lots_o_rice = university * 4
print(lots_o_rice)

# Using str
num = 3.87
strnum = str(num)
print("number: " + strnum)
# print("number: " + num)

"""
String indexing examples.
"""

phrase = "Python is great!"

# first character subsstring
print(phrase[0])

# fourth character
fourth = phrase[1]
print(fourth)
print(type(phrase))
print(type(fourth))

# length of string
phraselen = len(phrase)
print(phraselen)

# last character
print(phrase[phraselen - 1])
print(phrase[-1])

# thirteenth from last (fourth) character
print(phrase[-13])

# Out of bounds
#print(phrase[phraselen])
#print(phrase[-20])

# Indices
# string = "abcde"
# character   a  b  c  d  e
# pos index   0  1  2  3  4
# neg index  -5 -4 -3 -2 -1



"""
String searching examples.
"""

sentence = "When I tell you pick up the " + \
           "left rock, it will be the " + \
           "right one, and then only " + \
           "the right rock will be left."

# Finding strings within strings
print("Finding you")
#find first left from left
firstyou = sentence.find("you")
print(firstyou, sentence[firstyou])
#rfind=backwards from the string 
lastyou = sentence.rfind("you")
print(lastyou, sentence[lastyou])

print("")
print("Finding rights")
firstright = sentence.index("right")
print(firstright, sentence[firstright])
lastright = sentence.rindex("right")
print(lastright, sentence[lastright])

print("")
print("Finding Zoe")
firstzoe = sentence.find("Zoe")
print(firstzoe)
# firstzoe = sentence.index("Zoe")
# print(firstzoe)

# Counting strings within strings
print("")
print("Counting substrings")
print("Number of lefts:", sentence.count("left"))
print("Number of apples:", sentence.count("apple"))

# Checking start/ends
print("")
print(sentence.startswith("When"))
print(sentence.endswith("The end."))


"""
Slicing strings.
"""

word = "everything"

# Selecting substrings
print(word[1:5])
print(word[5:9])

# Open ended slices
print(word[5:])
print(word[:4])

# Using negative indices
print(word[-3:])
print(word[2:-3])

# Indexing past the end
print(word[8:20])
print("$" + word[22:29] + "^")

# Empty slices
print(word[6:6])
print(word[4:2])

country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)
mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)
name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)
num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)