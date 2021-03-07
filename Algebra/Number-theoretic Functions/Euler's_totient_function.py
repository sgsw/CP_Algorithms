def Phi(M):
    """
    return phi_function[0,M]
    """
    phi = [0]*(M + 1)
    phi[0] = 0
    phi[1] = 1
    for i in range(2, M + 1):
        phi[i] = i
    for i in range(2, M + 1):
        if phi[i] == i:
            for j in range(i, M + 1, i):
                phi[j] -= phi[j]//i
    return phi
