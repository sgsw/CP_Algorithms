import random
INF = 1 << 64


def probablyPrimeFermat(n, itr=5):
    """
    Primality tests by FermatTest
    """
    if n < 4:
        return (n == 2 or n == 3)
    for i in range(itr):
        a = 2 + random.randint(1, INF) % (n - 3)
        if pow(a,n - 1,n) != 1:
            return False
    return True


def check_composite(n,a,d,s):
    x = pow(a,d,n)
    if x == 1 or x == n - 1:
        return False
    for r in range(1,s):
        x = x * x % n
        if (x == n - 1):return False
    return True

def MillerRabin(n,itr = 10):
    """
    Primality tests by MillerRabin
    """
    if n < 4:
        return (n == 2 or n == 3)
    s,d = 0,n - 1
    while (d & 1 == 0):
        d >>= 1
        s += 1
    for _ in range(itr):
        a = 2 + random.randint(1,INF) % (n - 3)
        if check_composite(n,a,d,s):
            return False
    return True