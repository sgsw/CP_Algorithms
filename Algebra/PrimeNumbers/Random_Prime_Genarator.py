import random
INF = 1 << 64


def check_composite(n, a, d, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for r in range(1, s):
        x = x * x % n
        if (x == n - 1):
            return False
    return True


def MillerRabin(n, itr=10):
    """
    Primality tests by MillerRabin
    """
    if n < 4:
        return (n == 2 or n == 3)
    s, d = 0, n - 1
    while (d & 1 == 0):
        d >>= 1
        s += 1
    for _ in range(itr):
        a = 2 + random.randint(1, INF) % (n - 3)
        if check_composite(n, a, d, s):
            return False
    return True

def random_prime_generator(L,R):
    """
    return primeList in [L,R].
    """
    res = []
    for i in range(L,R + 1):
        if MillerRabin(i,itr = 20) == True:
            res.append(i)
    return res