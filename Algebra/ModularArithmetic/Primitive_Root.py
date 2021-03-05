import random
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