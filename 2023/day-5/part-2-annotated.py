from re import findall as F
def main():
    r = range
    e = lambda s: list(map(int, F(r'\d+', s)))
    with open('input.dat') as f: L = f.read().splitlines()
    S, I = e(L[0]), [i for i, l in enumerate(L) if len(l.split())==2]
    S = [[r(s, s+e)] for s, e in zip(S[::2], S[1::2])]
    M = [[e(k) for k in L[i+1:j-1]] for i, j in zip(I, I[1:]+[len(L)])]
    O = lambda a, b: r(max(a[0], b[0]), min(a[-1], b[-1])+1)
    # Iterating over the "big steps", the list of map batches
    for B in M:
        # Propagating the seeds through a single batch of maps.  This S
        # array will be transformed into the input of the next batch in
        # each iteration.
        for i, R in enumerate(S):
            # Collect the list of ranges for the next batch. All these
            # ranges here belong to the `i`th seed in the original input.
            S[i] = []
            # Iterating over all the ranges belonging to the `i`th seed
            for s in R:
                # Collect ranges that underwent "cell division". We only
                # keep track of the number ranges that weren't matched
                # by any of the maps in the current batch. The next map
                # in the batch will be matched against these ranges.
                # By default it is the `s` range itself.
                K = [s]
                # Iterating over all the maps in the current batch
                for m in B:
                    # Collect the list of ranges that were trimmed down
                    # by an overlap with the current map. We collect
                    # these ranges in a temporary list `T` and then
                    # replace the `K` list with these collected ranges.
                    T = []
                    # Iterating over all the ranges that can be matched
                    # against the current map. These ranges are either
                    # the `s` range itself or the ranges that were
                    # trimmed down by the previous maps in the batch.
                    for k in K:
                        # Match a range against the current map.
                        o = O(k, r(m[1], m[1]+m[2]))
                        # If there's no overlap, we skip this range, we
                        # keep it intact.
                        if len(o) == 0:
                            T += [k]
                            continue
                        if len(a:=r(k[0], o[0])) > 0: T += [a]
                        if len(b:=r(o[-1]+1, k[-1]+1)) > 0: T += [b]
                        p = m[0]-m[1]
                        o = r(o[0]+p, o[-1]+p+1)
                        S[i] += [o]
                    K = T
                S[i] += K
    print(min([min([k[0] for k in s]) for s in S]))
if __name__ == '__main__':
    main()