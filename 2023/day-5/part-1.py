from re import findall as F
def main():
    e = lambda s: list(map(int, F(r'\d+', s)))
    with open('input.dat') as f: L = f.read().splitlines()
    S, I = e(L[0]), [i for i, l in enumerate(L) if len(l.split())==2]
    M = [[e(k) for k in L[i+1:j-1]] for i, j in zip(I, I[1:]+[len(L)])]
    for i, s in enumerate(S):
        for m in M:
            for r in m:
                if s in range(r[1], r[1]+r[2]):
                    s += r[0]-r[1]
                    break
        S[i] = s
    print(min(S))
if __name__ == '__main__':
    main()