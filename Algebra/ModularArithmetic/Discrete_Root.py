import random
import math
from collections import defaultdict
INF = 1 << 64


def primitive_root_genarator(p):
    """
    constraints:
        p is prime and smaller than 1e12
    return one of the primitive_root modulo p
    """
    assert p < int(1e12)
    phi, v = p - 1, p - 1
    prime = []
    for i in range(2, phi + 1):
        if i*i > phi:
            break
        if v % i == 0:
            prime.append(i)
            while v % i == 0:
                v //= i
    if v > 1:
        prime.append(v)
    while True:
        r = random.randint(1, p - 1)
        if all(pow(r, phi//elem, p) != 1 for elem in prime):
            return r


def discrete_logarithm(a, b, m):
    """
    constraints:
        gcd(a,m) == 1

    find the smallest non_negative integer x: a^x = b (modulo m) if exists otherwise INF
    """
    assert math.gcd(a, m) == 1
    M = math.ceil(math.sqrt(m))
    baby_step = defaultdict(int)
    lbase, lpow, rpow = pow(a, M, m), 1, b
    for i in range(1, M + 1):
        rpow = a * rpow % m
        baby_step[rpow] = i
    for i in range(1, M + 1):
        lpow = lpow * lbase % m
        if lpow in baby_step:
            return i * M - baby_step[lpow]
    return INF


def discrete_root(k, a, p):
    """
    constraints:
        p is prime and smaller than 1e12

    let g = primitive_root modulo p
    solve x^k = a (modulo p) and return such x by tuple (y,M) ,when given x in the form of x = x0 * M^i  otherwise (INF,INF)
    """
    assert p < int(1e12)
    if a % p == 0:
        return 0,INF
    g = primitive_root_genarator(p)
    gk = pow(g, k, p)
    y0 = discrete_logarithm(gk, a, p)
    if y0 == INF:
        return INF, INF
    assert pow(gk,y0,p) == a % p
    M = (p - 1)//math.gcd(p - 1,k)
    x0 = pow(g,y0 % M, p)
    M = (p - 1)//math.gcd(p - 1,k)
    return x0,pow(g,M,p)