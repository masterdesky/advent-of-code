import sys
class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)
def A(L, M, x):
    if x < 0 or x >= len(L) or L[x] != 1:
        return
    L[x] = -1
    for dx in M:
        A(L, M, x+M[dx])
def main():
    P = {'|':('U','D'),'-':('L','R'),'L':('U','R'),
         'J':('L','U'),'7':('L','D'),'F':('R','D')}
    with open('input.dat') as f:
        L, R, C = ''.join((T:=f.read().split('\n'))), len(T), len(T[0])
    S = L.index('S')
    M, D = {'U':-C,'R':1,'D':C,'L':-1}, {k: v for k, v in zip('UDLR', 'DURL')}
    F = [(D[d], S+M[d]) for d in M if D[d] in P[L[S+M[d]]]]
    T = [(D[F[1][0]], S), F[0]]
    s = lambda i, p: p[1] if i==p[0] else p[0]
    while (t:=T[-1]) != T[0]:
        d = s(t[0], P[L[t[1]]])
        T.append((D[d], t[1]+M[d]))
    I = set([i for _, i in T][:-1])
    L = [0 if i in I else 1 for i in range(len(L))]
    with recursionlimit(5000):
        A(L, M, 0)
    L = ['F' if c==-1 else c for c in L]
    with open('flood.dat', 'w') as f:
        f.write('\n'.join([''.join([str(L[i*C+j]) for j in range(C)]) for i in range(R)]))
if __name__ == '__main__':
    main()