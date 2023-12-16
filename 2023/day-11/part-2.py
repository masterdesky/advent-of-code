from itertools import combinations as c
r = range
def D(P, H, V, a):
    L = []
    for p, q in P:
        x1, x2, y1, y2 = p[0], p[1], q[0], q[1]
        d = abs(x1-y1) + abs(x2-y2)
        d += (a-1)*(len(set(H) & set(r(min(x1, y1), max(x1, y1))))
                    +
                    len(set(V) & set(r(min(x2, y2), max(x2, y2)))))
        L.append(d)
    return L
def main():
    T = lambda M: [list(l) for l in zip(*M)]
    with open('input.dat') as f:
        L = [list(l) for l in f.read().split('\n')]
    E = lambda L: [i for i, l in enumerate(L) if '#' not in l]
    H, V = E(L), E(T(L))
    P = list(c([(i, j) for i in r(len(L)) for j in r(len(L[0])) if L[i][j] == '#'], 2))
    print(sum(D(P, H, V, a=1_000_000)))
if __name__ == '__main__':
    main()