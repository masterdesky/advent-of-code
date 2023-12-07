from re import findall as F
def main():
    e = lambda f: set(map(int, F(r'\d+', f[0])))
    with open('input.dat') as f:
        w=[len(e(F(r':\s(.*?)\s\|', l))&e(F(r'\|.*$', l))) for l in f.read().splitlines()]
    print(sum([2**(i-1) if i > 1 else i for i in w]))
if __name__ == '__main__':
    main()