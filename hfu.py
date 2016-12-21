
import sys

def hackon(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n>3:
        return ( 1*hackon(n-1) + 2*hackon(n-2) + 3*hackon(n-3) )

def main():
    n = int(raw_input())
    for i in range(1,n+1):
    	val = hackon(i)
    	print i
    	if (val%2 == 0):

    		print "even"
    	else:
    		print "odd"	

if __name__ == "__main__":
    main()        
