
from random import randint
import timeit  # to cal time


# build a function to calculate the time of the sort function
def run_sorting(algorithm, nts):
    setup_code = f"from __main__ import {algorithm}"

    stmt = f"{algorithm}({nts})"

    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)

    print(f"Quickest execution time: {min(time)}")


nts = [4, 2, 3, 1]


def insertion_sort(nts):

    for i in range(1, len(nts)):
        current_num = nts[i]

        p = i - 1

        while p >= 0 and nts[p] > current_num:
            nts[p + 1] = nts[p]
            p -= 1
        nts[p + 1] = current_num


# use randint finction to genaret random numbers between 0 - 100
if __name__ == "__main__":
    nts = [randint(0, 10000) for i in range(5000)]
    run_sorting(algorithm="insertion_sort", nts=nts)
