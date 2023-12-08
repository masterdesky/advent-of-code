from math import lcm
from re import findall as F
def main():
    with open('input.dat') as f:
        L = [s.strip() for s in f.read().splitlines() if s.strip()]
    T = [0 if d=='L' else 1 for d in L[0]]
    t = lambda s: tuple(f'{x.strip()}' for x in s.strip('()').split(','))
    N = {k: t(v) for k, v in (a.split(' = ') for a in L[1:])}
    S = [k for k in N if k[-1]=='A']
    I = [0,]*len(S)
    for i, s in enumerate(S):
        while s[-1] != 'Z':
            s = N[s][T[I[i]%len(T)]]
            I[i] += 1
    print(lcm(*I))
if __name__ == '__main__':
    main()