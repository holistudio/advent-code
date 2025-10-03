# ChatGPT helped with prompt:
"""
Write a python function to print the i-th number in the integer 
sequence OEIS#A325994 of Heinz numbers of integer partitions 
such that not every ordered pair of distinct parts has a 
different quotient.
"""
from math import isqrt
from fractions import Fraction

# Simple dynamic sieve/primes storage
_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def _extend_primes_up_to(n):
    """Extend global _primes list so that last prime >= n (or we have primes up to approx n)."""
    if _primes[-1] >= n:
        return
    candidate = _primes[-1] + 2
    while _primes[-1] < n:
        is_p = True
        r = isqrt(candidate)
        for p in _primes:
            if p > r:
                break
            if candidate % p == 0:
                is_p = False
                break
        if is_p:
            _primes.append(candidate)
        candidate += 2

def prime_pi(p):
    """Return index of prime p (1-based): 2->1, 3->2, etc. Assumes p is prime."""
    # ensure primes list contains p
    _extend_primes_up_to(p)
    try:
        return _primes.index(p) + 1
    except ValueError:
        # should not happen for moderate p, but try extending further
        _extend_primes_up_to(p * 2)
        return _primes.index(p) + 1

def factor_with_multiplicity(n):
    """Return list of prime factors with multiplicity, e.g. 12 -> [2,2,3]."""
    if n <= 1:
        return []
    factors = []
    # ensure primes cover up to sqrt(n)
    _extend_primes_up_to(isqrt(n) + 1)
    temp = n
    for p in _primes:
        if p * p > temp:
            break
        while temp % p == 0:
            factors.append(p)
            temp //= p
    if temp > 1:
        factors.append(temp)
    return factors

def _is_heinz_counterexample(n):
    """
    Return True if n is a Heinz number for which *not every ordered pair of distinct parts
    has a different quotient* — i.e., there exist two different ordered pairs of distinct
    prime-index parts with equal quotient.
    """
    # Get prime factors with multiplicity (these correspond to prime(y_i) in definition)
    prime_factors = factor_with_multiplicity(n)
    if not prime_factors:
        return False
    # Convert each prime factor to its prime index (y_i)
    parts = [prime_pi(p) for p in prime_factors]  # list of integers
    # For all ordered pairs (i,j) with i != j and parts[i] != parts[j], check quotient
    seen = {}  # map Fraction -> (i,j)
    L = len(parts)
    for i in range(L):
        for j in range(L):
            if i == j:
                continue
            if parts[i] == parts[j]:
                continue  # ordered pair must be of distinct parts
            q = Fraction(parts[i], parts[j])
            if q in seen:
                # ensure it's a different ordered pair (it will be, because (i,j) != seen[q])
                return True
            seen[q] = (i, j)
    return False

def print_a325994(i):
    """Compute and print the i-th term of OEIS A325994 (1-based)."""
    if i < 1:
        raise ValueError("i must be a positive integer (1-based).")
    found = 0
    n = 1
    while True:
        if _is_heinz_counterexample(n):
            found += 1
            if found == i:
                print(n)
                return
        n += 1

# Example: print first 10 terms
if __name__ == "__main__":
    for k in range(1, 11):
        print(f"a({k}) =", end=" ")
        print_a325994(k)
