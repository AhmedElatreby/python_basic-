"""  
Data sorting is any process that arranging data such as alphabetical or numerical into meanful order in oreder to make it easier to undersatnd to or visualise.
# Whey sorting data is important?
- It is easier to search through
- Remove or merge duplicates
- Compare to large sets of items and find out where they differ
"""

from random import randint
import timeit  # to cal time

if __name__ == "__main__":
    nts = [2, 9, 77, 10, 5, 66, 71, 0, 1, 6, 8, 9, 1, 3, ]
    print(sorted(nts))  # sorted is a bulitin function that used to sort values
    print("=================")


# build a function to calculate the time of the sort function
def run_sorting(algorithm, nts1):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({nts1})"
    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)
    print(f"Quickest execution time: {min(time)}")

# create a function bubbleSort


def bubbleSort(nts1):
    nts1_len = len(nts1)
    for i in range(nts1_len):
        for p in range(nts1_len - i - 1):
            if nts1[p] > nts1[p + 1]:
                nts1[p], nts1[p + 1] = nts1[p + 1], nts1[p]
    return nts1


# use randint finction to genaret random numbers between 0 - 100
if __name__ == "__main__":
    # to sort 10000 number took (9.883... secouns)
    nts1 = [randint(0, 10000) for i in range(10000)]
    run_sorting(algorithm="bubbleSort", nts1=nts1)
    # print(bubbleSort(nts1))
