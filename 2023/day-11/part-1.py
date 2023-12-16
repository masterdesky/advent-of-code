from itertools import combinations as c
r = range
def E(L):
    H = [i for i, l in enumerate(L) if '#' not in l]
    for i, k in zip(H, iter(r(len(H)))): L.insert(i+k, ['.',]*len(L[0]))
    return L
def main():
    T = lambda M: [list(l) for l in zip(*M)]
    with open('input.dat') as f:
        L = [list(l) for l in f.read().split('\n')]
    L = E(L)        # Row expansion
    L = T(E(T(L)))  # Column expansion
    P = list(c([(i, j) for i in r(len(L)) for j in r(len(L[0])) if L[i][j] == '#'], 2))
    D = [abs(p[0]-q[0]) + abs(p[1]-q[1]) for p, q in P]
    print(sum(D))
if __name__ == '__main__':
    main()