# ChatGPT helped with prompt:
"""
Write a python function to print the i-th number in the integer 
sequence OEIS#A325994 of Heinz numbers of integer partitions 
such that not every ordered pair of distinct parts has a 
different quotient.
"""
from math import isqrt
from fractions import Fraction

# simple prime generator cache
_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def _extend_primes_up_to(n):
    if _primes[-1] >= n:
        return
    candidate = _primes[-1] + 2
    while _primes[-1] < n:
        r = isqrt(candidate)
        is_p = True
        for p in _primes:
            if p > r:
                break
            if candidate % p == 0:
                is_p = False
                break
        if is_p:
            _primes.append(candidate)
        candidate += 2

def factorize(n):
    """Return prime factorization with multiplicity as a list of primes."""
    factors = []
    temp = n
    _extend_primes_up_to(isqrt(n) + 1)
    for p in _primes:
        if p * p > temp:
            break
        while temp % p == 0:
            factors.append(p)
            temp //= p
    if temp > 1:
        factors.append(temp)
    return factors

def prime_to_index(p):
    _extend_primes_up_to(p)
    return _primes.index(p) + 1

def partition_from_heinz(n):
    """Convert Heinz number to partition (list of prime indices)."""
    return [prime_to_index(p) for p in factorize(n)]

def in_a325994(n):
    """Check if n belongs to OEIS A325994."""
    parts = partition_from_heinz(n)
    if len(parts) < 2:
        return False
    seen = {}
    for i,a in enumerate(parts):
        for j,b in enumerate(parts):
            if i == j or a == b:
                continue
            q = Fraction(a,b)
            if q in seen:
                return True
            seen[q] = (i,j)
    return False

def a325994(nth):
    """Return the nth term of A325994 (1-based)."""
    count = 0
    k = 1
    while True:
        if in_a325994(k):
            count += 1
            if count == nth:
                return k
        k += 1

# demo: first 10 terms
if __name__ == "__main__":
    for i in range(1, 11):
        print(a325994(i))
