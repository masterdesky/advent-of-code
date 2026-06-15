def main():
    with open('input.dat') as f:
        S, A = [list(l) for l in zip(*[l.split() for l in f.read().split('\n')])]
    A = [['#'*int(n) for n in a.split(',')] for a in A]
    [print(f'{s}: {a}') for s, a in zip(S, A)]
if __name__ == '__main__':
    main()