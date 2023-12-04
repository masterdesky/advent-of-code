import re
def main():
    C, N = ['red', 'green', 'blue'], [12, 13, 14]
    with open('input.dat') as f:
        r = lambda l, c: re.findall(rf'(\d+)\s*{c}', l)
        m = lambda l, c: max([int(n) for n in r(l, c)])
        B = lambda l: [a > b for a, b in zip([m(l, c) for c in C], N)]
        # Could be replaced with `int(re.findall(r'(\d+):', l)[0]) for l`
        print(sum(i+1 for i, l in enumerate(f) in f if not any(B(l))))
if __name__ == '__main__':
    main()