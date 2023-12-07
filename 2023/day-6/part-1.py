from math import *
from re import findall as F
def main():
    e = lambda s: list(map(int, F('\d+', s)))
    with open('input.dat') as f:
        T, S = (e(l) for l in f.read().splitlines())
    D = lambda t, s: sqrt(t*t - 4*s)
    r = lambda t, s: (floor(abs((-t + D(t, s)) / 2))+1, ceil(abs((-t - D(t, s)) / 2)))
    print(prod([len(range(*r(t, s))) for t, s in zip(T, S)]))
if __name__ == '__main__':
    main()