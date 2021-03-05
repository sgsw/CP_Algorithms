import math
from collections import defaultdict
INF = 1 << 64


def discrete_logarithm(a, b, m):
    """
    constraints:
        gcd(a,m) == 1

    find the smallest non_negative integer x: a^x = b (modulo m) if exists otherwise INF
    """
    assert math.gcd(a,m) == 1
    M = math.ceil(math.sqrt(m))
    baby_step = defaultdict(int)
    lbase, lpow, rpow = pow(a, M, m), 1, b
    for i in range(1, M + 1):
        rpow = a * rpow % m
        baby_step[rpow] = i
    for i in range(1, M + 1):
        lpow = lpow * lbase % m
        if lpow in baby_step:
            return  i * M - baby_step[lpow] 
    return INF