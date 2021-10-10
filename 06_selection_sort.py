from random import randint
import timeit  # to cal time

# build a function to calculate the time of the sort function


def run_sorting(algorithm, nts):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({nts})"
    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)
    print(f"Quickest execution time: {min(time)}")


nts = [4, 2, 3, 1]


def selectiontion_sort(nts):

    n = len(nts)

    for i in range(n):
        idx = i
        for p in range(n):
            idx = i
            for p in range(i + 1, n):
                if nts[p] < nts[idx]:
                    idx = p

            nts[i], nts[idx] = nts[idx], nts[i]


# use randint finction to genaret random numbers between 0 - 100
if __name__ == "__main__":
    nts = [randint(0, 10000) for i in range(5000)]
    run_sorting(algorithm="selectiontion_sort", nts=nts)
