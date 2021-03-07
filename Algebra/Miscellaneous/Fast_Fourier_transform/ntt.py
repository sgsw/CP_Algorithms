import random
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
    x, y, d = extgcd(a, m)
    return x
 
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
        r = random.randint(1,p - 1)
        if all(pow(r,phi//elem,p) != 1 for elem in prime):
            return r
 
 
 
def ntt(a,inverse,p,g):
    """
    constraints:
        len(a) == 2^k
        all coeffitients are integer values.
    return a*b % p
    """
    n = len(a)
    w,wn = 1,g
    if inverse:
        wn = modinv(wn,p)
    if n == 1:
        return
    n//=2
    a0 = [a[i<<1] for i in range(n)]
    a1 = [a[(i<<1)|1] for i in range(n)]
    ntt(a0,inverse,p,g = g*g % p)
    ntt(a1,inverse,p,g = g*g % p)
    for i in range(n):
        a[i] = (a0[i] + w*a1[i]) % p
        a[i + n] = (a0[i] - w*a1[i]) % p
        w = w * wn % p
    return 
  
def modulo_multiply(a,b,p):
    """  
    constraint:
        coefficients are all integer values
    return a*b modulo p
    slower than usual fft
    """
    n = 1<< (len(a) + len(b) - 1).bit_length()
    lena,lenb = len(a),len(b)
    a = a + [0]*(n - lena)
    b = b + [0]*(n - lenb)
    n = len(a)
    g = primitive_root_genarator(p)
    ord,phi = 0,p - 1
    while phi % 2 == 0:
        ord += 1
        phi//=2
    assert  (1<<ord) % len(a) == 0
    w,wn = 1,pow(g,(p - 1)//len(a),p)
    ntt(a,False,p,wn)
    ntt(b,False,p,wn)
    for i in range(n):      
        a[i] = a[i]*b[i] % p
    ntt(a,True,p,wn)
    inv2 = modinv(n,p)
    for i in range(n):
        a[i] = a[i]*inv2 % p 
    return a[:lena + lenb - 1]