from re import findall as F
def main():
    r = range
    e = lambda s: list(map(int, F(r'\d+', s)))
    with open('input.dat') as f: L = f.read().splitlines()
    S, I = e(L[0]), [i for i, l in enumerate(L) if len(l.split())==2]
    S = [[r(s, s+e)] for s, e in zip(S[::2], S[1::2])]
    M = [[e(k) for k in L[i+1:j-1]] for i, j in zip(I, I[1:]+[len(L)])]
    O = lambda a, b: r(max(a[0], b[0]), min(a[-1], b[-1])+1)
    for B in M:
        for i, R in enumerate(S):
            S[i] = []
            for s in R:
                K = [s]
                for m in B:
                    T = []
                    for k in K:
                        o = O(k, r(m[1], m[1]+m[2]))
                        if len(o) == 0: T += [k]; continue
                        if len(a:=r(k[0], o[0])) > 0: T += [a]
                        if len(b:=r(o[-1]+1, k[-1]+1)) > 0: T += [b]
                        p = m[0]-m[1]
                        o = r(o[0]+p, o[-1]+p+1)
                        S[i] += [o]
                    K = T
                S[i] += K
    print(min([min([k[0] for k in s]) for s in S]))
if __name__ == '__main__':
    main()