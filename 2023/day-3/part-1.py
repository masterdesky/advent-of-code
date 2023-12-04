import re
import numpy as np
def main():
    n = lambda M: re.sub('[\d]', '1', M)
    u = lambda M: re.sub('[.]', '0', M)
    c = lambda M: re.sub('[^01\n]', '9', M)
    with open('input.dat') as f:
        M = [list(map(int, list(l))) for l in c(u(n(f.read()))).splitlines()]
        M = np.pad(np.array(M), [(1, 1), (1, 1)])
        C = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
if __name__ == '__main__':
    main()