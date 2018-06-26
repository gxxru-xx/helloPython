import sys
import math

def primes(x , y):
    l = [2] # list of prime numbers
    for n in range(3,y+1,2): # iterations over odd numbers
        isprime = True
        for e in l:
            if n % e == 0:
                isprime = False
                break
        if(isprime):
            l.append(n)

    return [e for e in l if e >= x]



test = int(sys.stdin.readline())


for j in range(test):
    lower, upper = map(int, sys.stdin.readline().split())
    pirmes = primes(lower, upper)
    for x in pirmes:
        print(x)
    print()
