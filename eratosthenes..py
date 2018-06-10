# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:43:43 2018

@author: soviv
"""



"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""



def Eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i ** 2, n + 1, i):
                IsPrime[j] = False
    return {x for x in range(2, n + 1) if IsPrime[x]}

if __name__ == "__main__":
    print (Eratosthenes(201))