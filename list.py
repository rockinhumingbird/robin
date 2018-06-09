# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:36:18 2018

@author: soviv
"""
#Write a function that takes a list of integers and returns the sum of those items in the list that are not divisible by 33
def listsum(numList):
    theSum = 0
    for i in numList:
        if (i% 3) != 0:
            theSum = theSum + i
        else:
            theSum
    return theSum
print(listsum(list(range(123)) + list(range(77))))

print(listsum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))

"""
Mutating Lists.
"""

print("Updating Items")
print("==============")

lst = list(range(5))
print(lst)

lst[1] = -7
lst[3] = 17
print(lst)

print("")
print("Adding Items")
print("============")

lst.append(42)
print(lst)

lst.insert(2, 75)
print(lst)

lst2 = [-56, 27, 8]
lst.extend(lst2)
print(lst)
lst.append(lst2)
print(lst)

print("")
print("Removing Items")
print("==============")

lst.pop()
print(lst)
lst.pop(3)
print(lst)


"""
Simple task list.
"""

def new(tasklist, task):
    """Add new task"""
    tasklist.append(task)
    
def remove_by_num(tasklist, tasknum):
    """Remove by number"""
    if tasknum > 0 and tasknum <= len(tasklist):
        tasklist.pop(tasknum - 1)

def remove_by_name(tasklist, taskname):
    """Remove by name"""
    if taskname in tasklist:
        tasklist.remove(taskname)
    
def printlist(tasklist):
    """Print task list"""
    print("========================")
    num = 1
    for task in tasklist:
        print(num, task)
        num += 1
    print("========================")
        
def run():
    """Manipulate task list"""
    tasks = []
    new(tasks, 'Teach Class')
    printlist(tasks)
    
    new(tasks, 'Buy some ties')
    new(tasks, 'Learn Python')
    printlist(tasks)
    
    new(tasks, 'Build new task list')
    printlist(tasks)
    
    remove_by_num(tasks, 1)
    printlist(tasks)
    remove_by_num(tasks, 2)
    printlist(tasks)
    
    remove_by_name(tasks, 'Buy some ties')
    printlist(tasks)

def new(tasklist, task):
    """Add new task"""
    tasklist.append(task)
    
"""
Tuple examples.
"""

# Lists and tuples are both sequences
print("Sequences")
print("=========")
lst = [1, 5, 7, 3]
tup = (1, 5, 7, 3)

print(lst, tup)
print(lst[2])
print(tup[2])
print(tup[:2])
print(tup[2:3])

# Tuples are immutable
lst[0] = 9
print(lst)
# tup[0] = 9
# print(tup)

print("")
print("Tuple Methods")
print("=============")

print(tup.index(7))
print(tup.count(4))

print("")
print("Iteration")
print("=========")

for item in tup:
    print(item)

print("")
print("Conversion")
print("==========")

lst2 = [8, 6, 4, 8, 2]
print(lst2)
tup2 = tuple(lst2)
print(tup2)
# tup2[3] = 7
lst3 = list(tup2)
print(lst3)
lst3[2] = 7
print(lst2, tup2, lst3)