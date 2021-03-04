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


def LCE(a, b, m):
    """
    solve a*x = b (modulo m) and get x = y (modulo M) then return (x,M) if solved otherwise INF,INF
    """
    x, y, d = extgcd(a, m)
    if b % d != 0:
        return INF, INF
    return x*b//d, abs(m//d)