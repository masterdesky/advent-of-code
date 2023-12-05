from re import *
def main():
    s = lambda p, M: sub(p, '.', M).splitlines()
    with open('input.dat') as f:
        D, K = s('[^\d\n]', L:=f.read()), s('[\d]', L)
    h = ['.'*(w:=len(D[0])+2)]
    p = lambda M: ''.join(h+[f'.{l}.' for l in M]+h)
    d, k = p(D), p(K)
    S = [(m.start(), m.end()) for m in finditer('[^.]+', d)]
    C = [i=='1' for i in sub('[^.]', '1', k)]
    c = lambda i: any([C[i+j] for j in[-w-1,-w,-w+1,-1,1,w-1,w,w+1]])
    print(sum([int(d[slice(*r)]) for r in S if any([c(i) for i in range(*r)])]))
if __name__ == '__main__':
    main()