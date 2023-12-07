from re import findall as F
def main():
    e = lambda f: set(map(int, F(r'\d+', f[0])))
    with open('input.dat') as f:
        w = [len(e(F(r':\s(.*?)\s\|', l))&e(F(r'\|.*$', l))) for l in f.read().splitlines()]
    l, n = len(w), [1,]*len(w)
    for i in range(l):
        s = slice(j:=i+1, j+c if j+(c:=w[i]) <= l else None)
        n[s] = [x+n[i] for x in n[s]]
    print(sum(n))
if __name__ == '__main__':
    main()