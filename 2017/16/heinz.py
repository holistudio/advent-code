# ChatGPT helped with prompt:
"""
Write a python function to print the i-th number in the integer 
sequence OEIS#A325994 of Heinz numbers of integer partitions 
such that not every ordered pair of distinct parts has a 
different quotient.
"""
from math import isqrt
from fractions import Fraction

# simple prime generator

def first_n_primes(n):
    """Return a list of the first n prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        r = isqrt(candidate)
        for p in primes:
            if p > r:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

_primes = first_n_primes(n=100)

# -----------------------------------------------------------------------------
# Helper: ensure we have enough primes in the cache
# -----------------------------------------------------------------------------
def _extend_primes_up_to(n):
    """
    Make sure the global _primes list contains primes at least up to value `n`.
    This is used by both factorization and by mapping a prime -> its index.
    Algorithm:
      - If our largest cached prime is already >= n, do nothing.
      - Otherwise test odd candidates by trial division against cached primes
        up to sqrt(candidate), appending primes as we find them.
    Note: this is a simple dynamic sieve-ish approach sufficient for small/medium n.
    """
    if _primes[-1] >= n:
        return
    candidate = _primes[-1] + 2
    while _primes[-1] < n:
        r = isqrt(candidate)
        is_p = True
        # test divisibility by cached primes up to sqrt(candidate)
        for p in _primes:
            if p > r:
                break
            if candidate % p == 0:
                is_p = False
                break
        if is_p:
            _primes.append(candidate)
        candidate += 2

# -----------------------------------------------------------------------------
# Factorization
# -----------------------------------------------------------------------------
def factorize(n):
    """
    Return the prime factorization of n as a list of primes with multiplicity.
    Example: 12 -> [2, 2, 3]
    Steps:
      1. Ensure primes are cached up to sqrt(n) to allow trial division.
      2. For each cached prime p, repeatedly divide n by p and record p while possible.
      3. If remainder > 1 at the end, it is a prime > sqrt(original n) — append it.
    This list of primes (with multiplicity) corresponds to the primes that multiply
    to the Heinz number; mapping each prime to its prime-index gives the partition.
    """
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
        # temp is a prime > sqrt(n) (or equal); include it once
        factors.append(temp)
    return factors

# -----------------------------------------------------------------------------
# Map a prime (e.g. 2,3,5,7) to its 1-based index (2->1, 3->2, 5->3, ...)
# -----------------------------------------------------------------------------
def prime_to_index(p):
    """
    Ensure the prime p is in the cached primes list and return its 1-based index.
    Example: prime_to_index(2) -> 1, prime_to_index(3) -> 2.
    This mapping is the heart of Heinz encoding: a part of size k corresponds
    to the k-th prime, and the Heinz number multiplies those primes.
    """
    _extend_primes_up_to(p)
    return _primes.index(p) + 1

# -----------------------------------------------------------------------------
# Convert a Heinz number to its partition (list of parts)
# -----------------------------------------------------------------------------
def partition_from_heinz(n):
    """
    Given a Heinz number n = prod_i p_{lambda_i}, recover the partition lambda.
    Steps:
      1. Factorize n -> list of primes [p_a, p_b, ...] (with multiplicity).
      2. Map each prime p_x to its prime-index (prime_to_index).
    The returned list are the partition parts (not sorted here, but the order does not matter).
    Example: n = 42 = 2 * 3 * 7 -> factorize -> [2,3,7] -> indices [1,2,4].
    """
    return [prime_to_index(p) for p in factorize(n)]

# -----------------------------------------------------------------------------
# Core test: does n belong to OEIS A325994?
# -----------------------------------------------------------------------------
def in_a325994(n):
    """
    Decide whether n is in A325994: there exist two different ordered pairs
    of distinct parts (a,b) and (c,d) (distinct by value) with the same quotient a/b = c/d.

    Step-by-step:
      1. Convert n to the partition parts via partition_from_heinz(n).
      2. If fewer than 2 parts, no ordered pair exists -> return False.
      3. Enumerate all ordered pairs of positions (i, j) with i != j.
         - We also require the two parts themselves to be distinct in value,
           so skip pairs where parts[i] == parts[j].
      4. For each valid ordered pair compute the exact rational quotient q = Fraction(parts[i], parts[j]).
         - Use Fraction to avoid floating-point equality issues and to detect exact rational equality.
      5. Keep a dictionary `seen` mapping quotient -> which ordered pair produced it first.
         - If we encounter the same quotient q again from a different ordered pair,
           then the property "every ordered pair of distinct parts has a different quotient"
           is violated and n belongs to A325994 -> return True.
      6. If no repeated quotient is found among distinct ordered pairs, return False.
    """
    parts = partition_from_heinz(n)

    # Need at least two parts (and they must be distinct in some ordered pair)
    if len(parts) < 2:
        return False

    # seen maps exact Fraction quotients to the first ordered pair that produced it
    seen = {}
    for i, a in enumerate(parts):
        for j, b in enumerate(parts):
            # skip same position (ordered pair must use two elements)
            if i == j:
                continue
            # skip pairs where the two parts are equal in value:
            # the sequence's condition requires pairs of *distinct* parts (distinct values).
            if a == b:
                continue
            # compute exact rational quotient a/b
            q = Fraction(a, b)
            # if we've already seen this numeric quotient from a different ordered pair,
            # then n satisfies "there exist two different ordered pairs with equal quotient"
            if q in seen:
                return True
            # otherwise record this quotient and the pair that produced it
            seen[q] = (i, j)
    # no repeated quotient found among ordered pairs of distinct parts
    return False

# -----------------------------------------------------------------------------
# Naive enumerator: find the nth term by scanning natural numbers
# -----------------------------------------------------------------------------
def a325994(nth):
    """
    Return the nth term of A325994 (1-based) by brute-force search.
    Steps:
      1. Start at k = 1 and test in_a325994(k).
      2. Count how many terms we have found until reaching nth.
      3. Return that k when we've found the nth term.

    Note: This is a naive approach (scans every integer). For larger nth or large
    ranges it's much faster to enumerate partitions or generate candidate Heinz numbers
    directly (or use known OEIS data / optimized factoring libraries).
    """
    count = 0
    k = 1
    while True:
        if in_a325994(k):
            count += 1
            if count == nth:
                return k
        k += 1

# demo: print first 10 terms (keeps the original demo behavior)
if __name__ == "__main__":
    for i in range(1, 11):
        print(a325994(i))
