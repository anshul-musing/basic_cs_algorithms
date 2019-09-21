import numpy as np
import time
import sys
sys.setrecursionlimit(20000)
from src.sorting import Sort


def testSortValidity():
    np.random.seed(707)
    test = np.arange(100)
    a = np.random.choice(test, 10, replace=False)
    print('original array')
    print(a)

    t = Sort()

    print('bubble sort')
    print(t.bubble(a, ascending=True))
    print(t.bubble(a, ascending=False))
    
    print('\nselection sort')
    print(t.selection(a, ascending=True))
    print(t.selection(a, ascending=False))
    
    print('\ninsertion sort')
    print(t.insertion(a, ascending=True))
    print(t.insertion(a, ascending=False))
    
    print('\nmerge sort')
    print(t.mergesort(a, ascending=True))
    print(t.mergesort(a, ascending=False))
    
    print('\nquicksort')
    print(t.quicksort(a, ascending=True))
    print(t.quicksort(a, ascending=False))


def testSortTime():
    np.random.seed(707)
    test = np.arange(-50000, 50000)
    a = np.random.choice(test, 10000, replace=False)
    np.random.shuffle(a)
    print('Original array size: ' + str(len(a)))
    print('Original array sorted? ' + str(all(sorted(a) == a)))

    t = Sort()

    s = time.time()
    abub = t.bubble(a)
    print('\nArray sorted now? ' + str(all(sorted(abub) == abub)))
    print('bubble sort time: ' + str(time.time() - s) + ' sec')

    s = time.time()
    asel = t.selection(a)
    print('\nArray sorted now? ' + str(all(sorted(asel) == asel)))
    print('selection sort time: ' + str(time.time() - s) + ' sec')

    s = time.time()
    ains = t.insertion(a)
    print('\nArray sorted now? ' + str(all(sorted(ains) == ains)))
    print('insertion sort time: ' + str(time.time() - s) + ' sec')

    s = time.time()
    amrg = t.mergesort(a)
    print('\nArray sorted now? ' + str(all(sorted(amrg) == amrg)))
    print('merge sort time: ' + str(time.time() - s) + ' sec')

    s = time.time()
    aqck = t.quicksort(a)
    print('\nArray sorted now? ' + str(all(sorted(aqck) == aqck)))
    print('quick sort time: ' + str(time.time() - s) + ' sec')


if __name__ == '__main__':

    # Test different sorting algorithms
    print('Testing sort validity ...')
    testSortValidity()
    
    print('\nTesting sort time ...')
    testSortTime()
