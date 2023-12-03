import re
def main():
    p = lambda l: re.sub('[^\d]', '', l)
    with open('input.dat') as f:
        print(sum(int(p(l)[0] + p(l)[-1]) for l in f))
if __name__ == '__main__':
    main()