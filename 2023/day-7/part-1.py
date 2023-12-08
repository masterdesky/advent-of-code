def main():
    c = ['A', 'K', 'Q', 'J', 'T'] + list(range(9, 1, -1))
    d = {str(k): v for k, v in zip(c, range(len(c)))}
    S = {k: [] for k in '54F321H'}
    with open('input.dat') as f:
        H = {l.split()[0]: int(l.split()[1]) for l in f}
    T = lambda h: set(list(h))
    for h, _ in H.items():
        R, l = [h], len(T(h))
        if l == 1: S['5']+=R
        elif l == 2:
            if any([h.count(k)==4 for k in T(h)]): S['4']+=R
            else: S['F']+=R
        elif l == 3:
            if any([h.count(k)==3 for k in T(h)]): S['3']+=R
            else: S['2']+=R
        elif l == 4: S['1']+=R
        elif l == 5: S['H']+=R
    F = []
    for k in S:
        F += sorted(S[k], key=lambda h: tuple(d[h[i]] for i in range(5)))
    print(sum([(len(H)-i)*H[''.join(h)] for i, h in enumerate(F)]))
if __name__ == '__main__':
    main()