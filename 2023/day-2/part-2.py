import re
from math import prod
def main():
    C = ['red', 'green', 'blue']
    with open('input.dat') as f:
        r = lambda l, c: re.findall(rf'(\d+)\s*{c}', l)
        m = lambda l, c: max([int(n) for n in r(l, c)])
        print(sum(prod(m(l, c) for c in C) for l in f))
if __name__ == '__main__':
    main()