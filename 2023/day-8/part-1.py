from re import findall as F
def main():
    with open('input.dat') as f:
        L = [s.strip() for s in f.read().splitlines() if s.strip()]
    T = [0 if d=='L' else 1 for d in L[0]]
    t = lambda s: tuple(f'{x.strip()}' for x in s.strip('()').split(','))
    N = {k: t(v) for k, v in (a.split(' = ') for a in L[1:])}
    s, i = 'AAA', 0
    while s != 'ZZZ':
        s = N[s][T[i%len(T)]]
        i += 1
    print(i)
if __name__ == '__main__':
    main()