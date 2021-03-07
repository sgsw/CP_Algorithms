import math
INF = 1 << 64


def extgcd(a, b):
    """
    return (x,y,d) ax + by = gcd(a,b)
    """
    if b == 0:
        return (1, 0, a)
    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y
    return s, t, d


def LDE(a, b, c):
    """
        return any/all pair(x,y) ax+by=c if exists otherwise (INF,INF)
    """
    assert a != 0 or b != 0
    x, y, g = extgcd(a, b)
    if c % g != 0:
        return (INF, INF)
    d = c//g
    return x*d, y*d
