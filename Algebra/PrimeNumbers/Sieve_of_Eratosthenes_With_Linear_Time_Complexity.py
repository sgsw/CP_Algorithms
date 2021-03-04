def fast_sieve(M):
    lp = [0]*(M + 1)
    pr = []
    for i in range(2, M + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        for p in pr:
            if p > lp[i] or i*p > M:
                break
            lp[i*p] = p
    return lp