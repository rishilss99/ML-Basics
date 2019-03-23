import time
import sys
import numpy as np

"""To check the memory taken up by numpy arrays and lists"""


def memory():

    list1 = list(range(2000))
    arr1 = np.arange(2000)

    print("Size of list " + str(sys.getsizeof(5)*len(list1)))
    print("Size of array " + str(arr1.itemsize*arr1.size))


"""To check the speed performance of numpy arrays and lists"""


def timecheck():

    a = 100000
    l1 = list(range(a))
    l2 = list(range(a))

    st = time.time()
    res1 = l1 + l2
    print("Resulting time for lists = " + str((time.time()-st)*1000))

    arr1 = np.arange(a)
    arr2 = np.arange(a)

    st = time.time()
    res2 = arr1 + arr2
    print("Resulting time for arrays = " + str((time.time()-st)*1000))


timecheck()


