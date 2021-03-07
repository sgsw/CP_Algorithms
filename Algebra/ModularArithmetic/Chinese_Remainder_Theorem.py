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


def CRT(rem_list, mod_list, MOD=INF):
    """
    constraint: 
        gcd(pi,pj) = 1 if i!= j

    return pair of (y,M) :x == y (modulo M)
    which satisfies x = rem_list[i] (modulo mod_list[i])
    """
    K = len(mod_list)
    assert len(rem_list) == len(mod_list)
    X = [0]*(K)
    res = 0
    fact = 1
    for i in range(K):
        X[i] = rem_list[i]
        for j in range(i):
            X[i] = extgcd(mod_list[j], mod_list[i])[0] * (X[i] - X[j])
            X[i] %= mod_list[i]
        res = (res + X[i] * fact) % MOD
        fact = (fact * mod_list[i]) % MOD
    return (res, fact)


def pair_CRT(rem_pair, mod_pair):
    """
        let (b1,b2) = rem_pair,(m1,m2) = mod_pair

        return pair of (y,M) : x == y (modulo M)
        which satisfies x = b_i (modulo m_i) for 1 <= i <= 2
    """
    assert len(rem_pair) == len(mod_pair) == 2
    d = math.gcd(mod_pair[0], mod_pair[1])
    if (rem_pair[0] - rem_pair[1]) % d != 0:
        return INF, INF
    s = (rem_pair[1] - rem_pair[0])//d
    M = mod_pair[0]*mod_pair[1]//d
    x = (rem_pair[0] + s*mod_pair[0] *
         extgcd(mod_pair[0]//d, mod_pair[1]//d)[0]) % M
    return x, M