import re
def p(m, l):
    l = re.sub('|'.join(m.keys()), lambda x: str(m[x.group()]), l)
    return re.sub('[^\d]', '', l)
def main():
    n = 'zero one two three four five six seven eight nine'
    m = lambda n: {w: n for n, w in enumerate(n)}
    m1, m2 = m(n.split()), m(n[::-1].split()[::-1])
    with open('input.dat') as f:
        print(sum(int(p(m1, l)[0] + p(m2, l[::-1])[0]) for l in f))
if __name__ == '__main__':
    main()