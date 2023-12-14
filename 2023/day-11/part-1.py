def main():
    with open('input.dat') as f:
        L, R, C = ''.join((T:=f.read().split('\n'))), len(T), len(T[0])
    print(L)
if __name__ == '__main__':
    main()