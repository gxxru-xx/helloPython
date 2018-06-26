import sys
from math import sqrt

def smallPrimes(x , y):
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

def primes(n):
    ps, sieve = [], [True] * (n)
    for p in range(2, n):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return ps


def primesRange(lo, hi, delta):
    def qInit(p):
        return ((lo + p + 1) / -2) % p

    def qReset(p, q):
        return (q - delta) % p

    output, sieve = [], [True] * delta
    ps = primes(int(sqrt(hi)))[1:]
    qs = []
    for x in ps:
        qs.append(int(qInit(x)))

    while lo < hi:
        for i in range(0, delta):
            sieve[i] = True
        for p, q in zip(ps, qs):
            for i in range(q, delta, p):
                sieve[i] = False
        qs = map(qReset, ps, qs)
        for i, t in zip(range(0, delta), range(lo + 1, hi, 2)):
            if sieve[i]: output.append(t)
        lo += (2 * delta)
    return output


test = int(sys.stdin.readline())

for j in range(test):
    lower, upper = map(int, sys.stdin.readline().split())
    if upper-lower < 100:
        pirmes = smallPrimes(lower, upper)
    else:
        pirmes = primesRange(lower, upper, int(sqrt(upper-lower)))

    for x in pirmes:
        print(x)

    print()
