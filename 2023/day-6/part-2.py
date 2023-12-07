from math import *
from re import findall as F
def main():
    with open('input.dat') as f:
        t, s = (int(''.join(F('\d+', l))) for l in f.read().splitlines())
    D = lambda t, s: sqrt(t*t - 4*s)
    print(len(range(*(floor(abs((-t + D(t, s)) / 2))+1, ceil(abs((-t - D(t, s)) / 2))))))
if __name__ == '__main__':
    main()