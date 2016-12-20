#!/bin/python
# Tailor Shop Hacker-rank Week of Code 27 Challenge 2
import sys
import math

n,p = raw_input().strip().split(' ')
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split(' '))
a = sorted(a)
numbuttons = []
# your code goes here
for i in range(len(a)):
        numbuttons.append( math.ceil(a[i]/float(p)) )        
sum = 0 
#print numbuttons
for i in range(0,len(numbuttons)):
    if numbuttons[i] not in numbuttons[:i]:
        numbuttons[i] = numbuttons[i]
    else:
        numbuttons[i] = numbuttons[i-1] + 1 
    sum += numbuttons[i]  
print int(sum) 