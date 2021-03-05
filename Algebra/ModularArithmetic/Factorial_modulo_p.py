def factmod(n, p):
    """
    constraints:
        p is relatively small.

    find pair (ord,q) : n! = (p^ord) * q
    """
    fact = [1]*(p)
    for i in range(1, p):
        fact[i] = fact[i - 1] * i % p
    ord, q = 0, 1
    while n > 1:
        parity = n//p
        if parity % 2 == 1:
            q = p - q
        q = q * fact[n % p] % p
        n //= p
        ord += n
    return ord, q