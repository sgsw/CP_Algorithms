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


def modinv(a, m):
    """
    return x = a^-1 (modulo m) if such x exists otherwise INF
    """
    x, y, d = extgcd(a, m)
    if d != 1:
        return INF
    return x