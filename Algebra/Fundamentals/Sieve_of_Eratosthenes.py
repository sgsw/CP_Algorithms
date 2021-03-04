from math import sqrt


def PRIME_SIEVE(M):
    """
    return PRIME_LIST[0,M]
    """
    isprime = [True]*(M + 1)
    isprime[0] = isprime[1] = False
    for i in range(2, M + 1):
        if i*i > M:
            break
        if isprime[i]:
            for j in range(i*i, M + 1, i):
                isprime[j] = False
    return isprime


def segment_SIEVE(L, R):
    """
    return PRIME_LIST[L,R]
    """
    assert 1 <= L <= R
    sqrtR = int(sqrt(R))
    vec = PRIME_SIEVE(sqrtR)
    primes = []
    for i in range(sqrtR + 1):
        if vec[i]:primes.append(i)
    isprime = [True]*(R - L + 1)
    for p in primes:
        for i in range(max(p*p,(L + p - 1)//p * p),R + 1,p):
            isprime[i - L] = False
    if L == 1:
        isprime[0] = False
    return isprime
