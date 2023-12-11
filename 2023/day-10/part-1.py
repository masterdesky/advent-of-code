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
    print((len(T)-1)//2)
if __name__ == '__main__':
    main()