import math
from random import randint

def RSA_key():
    p = simple_number()
    q = simple_number()
    print(p, q)
    n = p*q
    fi = fi_n(p, q)
    e = find(p, q)
    d = find_d(e, fi)
    return (e, n), (d, n)

def simple_number():
    start = randint(2, 10000)
    for i in range(start, start + 1000000):
        for j in range(2, int((start + 1000000)**0.5)):
            if i % j == 0:
                break
            else:
                return i


def fi_n(p, q):
    return (p-1)*(q-1)

def find(p, q):
    end = fi_n(p, q)
    start = randint(2, end-1)
    for e in range(start, end + 1):
        if math.gcd(e, end) == 1:
            return e

def find_d(e, fi):
    for d in range(1, 498938975225):
        if (e*d-1)%fi == 0:
            return d


