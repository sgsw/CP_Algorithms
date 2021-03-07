import math
import cmath

def fft(a,inverse):
    """
    constraints:
        size(a) = 2^k for certain k
    return fft of vector a.
    """
    n = len(a)
    if n == 1:
        return
    n//=2
    a0 = [a[i<<1] for i in range(n)]
    a1 = [a[(i<<1)|1]for i in range(n)]
    fft(a0,inverse)
    fft(a1,inverse)
    ang = -math.pi/n if inverse == True else math.pi/n
    wn = cmath.rect(1,ang)
    w = cmath.rect(1,0)
    for i in range(n):
        a[i] = a0[i] + w*a1[i]
        a[i + n] = a0[i] - w*a1[i]
        if inverse:
            a[i]/=2
            a[i + n]/=2
        w *= wn
    return 

def multiply(a,b):
    """
    constraint:
        coefficients are all integer values.
        let n = max(size(a) ,size(b)) and h = max(coefficients)
        h*h*n should be represented by 64-bit float.
    return a*b
    """
    n = 1<< (len(a) + len(b) - 1).bit_length()
    lena,lenb = len(a),len(b)
    a = a + [0]*(n - lena)
    b = b + [0]*(n - lenb)
    fft(a,False)
    fft(b,False)

    for i in range(n):
        a[i] *= b[i]
    fft(a,True)
    for i in range(n):
        a[i] = round(a[i].real)
    return a[:lena+ lenb - 1]