from re import *
def main():
    with open('input.dat') as f:
        L = [list(map(int, findall(r'-?\d+', l))) for l in f.read().splitlines()]
    N = [[] for _ in L]
    for i, l in enumerate(L):
        while any([i != 0 for i in l]) and (len(l) > 0):
            N[i].append(l[-1])
            l = [a-b for a, b in zip(l[1:], l)]
    print(sum(sum(i for i in n) for n in N))
if __name__ == '__main__':
    main()