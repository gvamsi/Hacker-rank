#!/bin/python
# Week of Code 27 Challenge 1
import sys
import math

n = int(raw_input().strip())
p = int(raw_input().strip())
value = 0
if ( p == 1 ):
	print 0
elif ( p == n ):
	print 0
else:
	if ( (n%2) == 0 ):
		value = min( math.floor(p/2) , (math.ceil(n-p+1)/2) )
	else:
		value = min( math.floor(p/2) , math.floor(n-p)/2 )
	print int(value)