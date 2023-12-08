def main():
    c = ['A', 'K', 'Q', 'T'] + list(range(9, 1, -1)) + ['J']
    d = {str(k): v for k, v in zip(c, range(len(c)))}
    S = {k: [] for k in '54F321H'}
    with open('input.dat') as f:
        H = {l.split()[0]: int(l.split()[1]) for l in f}
    T = lambda h: set(list(h))
    for h, _ in H.items():
        R, n = [h], h.replace('J', '')
        if h.count('J') == 5: S['5']+=R; continue
        g = sorted(list(set(h.count(k) for k in T(n))))
        if g.count(g[-1]) == 1:
            m = h.replace('J', sorted(n, key=lambda k: n.count(k))[-1])
        else: m = h.replace('J', sorted(n, key=lambda k: d[k])[0])
        l = len(T(m))
        if l == 1: S['5']+=R
        elif l == 2:
            if any([m.count(k)==4 for k in T(m)]): S['4']+=R
            else: S['F']+=R
        elif l == 3:
            if any([m.count(k)==3 for k in T(m)]): S['3']+=R
            else: S['2']+=R
        elif l == 4: S['1']+=R
        elif l == 5: S['H']+=R
    F = []
    for k in S:
        F += sorted(S[k], key=lambda h: tuple(d[h[i]] for i in range(5)))
    print(sum([(len(H)-i)*H[''.join(h)] for i, h in enumerate(F)]))
if __name__ == '__main__':
    main()