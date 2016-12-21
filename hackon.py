#!/bin/python

import sys


def hackon(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 0
    if n == 4:
        return 1
    if n == 5:
        return 1
    if n == 6:
        return 0  
    if n == 0:
        return 0          
          
def main():
    n,q = raw_input().strip().split(' ')
    n,q = [int(n),int(q)]
    a = [[0 for x in range(n)] for y in range(n)]
    newa = [[0 for x in range(n)] for y in range(n)]
    times = 0
    val = 0
    temp = 0
    # hackonaki matrix a
    for i in range(1,(n+1)):
        for j in range(1,(n+1)):
            #print i,j
            val = ((i*j)**2)%7
            val = int(hackon(val))
            if ( val == 0 ):
                a[i-1][j-1] = 1


    for a0 in xrange(q):
        angle = int(raw_input().strip()) 
    # your code goes here
        count = 0
        times = int(angle/90)
        times = times%4
        if times == 1:
            newa = zip(*a[::-1])
        if times == 2:
            temp = zip(*a[::-1])
            newa = zip(*temp[::-1])
        if times == 3:
            temp = zip(*a[::-1])
            temp = zip(*temp[::-1])
            newa = zip(*temp[::-1])  
        if times == 0:
            newa = a    
        for i in range(n):
            for j in range(n):
                if (a[i][j] != newa[i][j]):
                    count +=1
        print count

if __name__ == "__main__":
    main()        
        
    