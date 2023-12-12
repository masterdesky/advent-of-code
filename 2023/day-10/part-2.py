def FF(L, M, x):
    Q = [x]
    while Q:
        x = Q.pop(0)
        if x < 0 or x >= len(L) or L[x] != 1: continue
        L[x] = -1
        for dx in M:
            y = x + M[dx]
            if 0 <= y < len(L) and L[y] == 1: Q.append(y)
def RC(E, i, C):
    c, xp, yp = 0, i%C, i//C
    for e in E:
        x1, y1, x2, y2 = e[0]%C, e[0]//C, e[1]%C, e[1]//C
        if (yp < y1) != (yp < y2) and \
            xp < x1 + (x2-x1)*(yp-y1)/(y2-y1):
            c += 1
    return c%2 != 1
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
    I = [i for _, i in T]
    L = [0 if i in set(I) else 1 for i in range(len(L))]
    FF(L, M, 0)
    L = [0 if c==-1 else c for c in L]
    E = [(i, j) for i, j in zip(I, I[1:])]
    for i in [i for i in range(len(L)) if L[i] == 1]:
        if RC(E, i, C): L[i] = 0
    #with open('flood.dat', 'w') as f:
    #    f.write('\n'.join([''.join(map(str, L[i*C:(i+1)*C])) for i in range(R)]))
    print(sum(L))
if __name__ == '__main__':
    main()