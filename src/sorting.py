
class Sort(object):

    # Bubble sort (in place)
    # compare two items, swap them if out of
    # order.  keep doing it for each pair of items
    def bubble(self, A, ascending=True):
        if len(A) > 0:
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    if ascending:
                        if A[i] > A[j]: #swap them
                            temp = A[i]
                            A[i] = A[j]
                            A[j] = temp
                    else:
                        if A[i] < A[j]: #swap them
                            temp = A[i]
                            A[i] = A[j]
                            A[j] = temp
            return A
        else:
            print('empty array')


    # Selection sort (in place)
    # find the minimum in the array, put it in the
    # first spot.  find the next minimum, put it
    # in the second spot, and so on ...
    def selection(self, A, ascending=True):
        if len(A) > 0:
            def smallest(B, start):
                s = B[0]
                p = start
                for j in range(1,len(B)):
                    if B[j] < s:
                        s = B[j]
                        p = start + j
                return s, p
            
            def largest(B, start):
                s = B[0]
                p = start
                for j in range(1,len(B)):
                    if B[j] > s:
                        s = B[j]
                        p = start + j
                return s, p
            
            for i in range(0, len(A)-1):
                subarr = A[i:]
                if ascending:
                    key, pos = smallest(subarr, i)
                else:
                    key, pos = largest(subarr, i)
                temp = A[i]
                A[i] = key
                A[pos] = temp
            return A
        else:
            print('empty array')


    # Insertion sort (in place)
    # like sorting a set of cards in your hand
    # go from left to right
    # pick the current card and insert it at the
    # appropriate location on the sorted left side
    def insertion(self, A, ascending=True):
        if len(A) > 0:
            for i in range(1, len(A)):
                ref = A[i]
                j = i-1
                if ascending:
                    while j >= 0 and ref < A[j]:
                        A[j+1] = A[j]
                        j = j-1
                else:
                    while j >= 0 and ref > A[j]:
                        A[j+1] = A[j]
                        j = j-1
                A[j+1] = ref
            return A
        else:
            print('empty array')


    # Merge sort
    # merge two sorted pile of cards
    # both pile are face up
    # pick the card which is the smallest of two pile
    # keep repeating until all pile are merged
    def merge(self, A, l, m, h, ascending):
        
        n1 = m - l + 1
        n2 = h - m 
        L = [0]*n1 
        R = [0]*n2 

        for i in range(0 , n1): 
            L[i] = A[l + i] 
      
        for j in range(0 , n2): 
            R[j] = A[m + 1 + j] 
      
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2 :
            if ascending:
                if L[i] <= R[j]: 
                    A[k] = L[i] 
                    i += 1
                else: 
                    A[k] = R[j] 
                    j += 1
            else:
                if L[i] >= R[j]: 
                    A[k] = L[i] 
                    i += 1
                else: 
                    A[k] = R[j] 
                    j += 1
            k += 1
        
        while i < n1: 
            A[k] = L[i] 
            i += 1
            k += 1

        while j < n2: 
            A[k] = R[j] 
            j += 1
            k += 1

    def msort(self, A, l, h, ascending):
        if l < h:
            m = int((l+h)/2)
            self.msort(A, l, m, ascending)
            self.msort(A, m+1, h, ascending)
            self.merge(A, l, m, h, ascending)

    def mergesort(self, A, ascending=True):
        if len(A) > 0:
            self.msort(A, 0, len(A)-1, ascending)
            return A
        else:
            print('empty array')


    # Quick sort
    # Partition the array into two parts such that
    # all elements in the first part are less than pivot
    # element, and the all elements in the other are
    # greater.  Repeat this for both partitions
    def partition(self, A, l, h, ascending):
        x = A[h]
        i = l - 1
        j = l
        while j < h:
            if ascending:
                if A[j] <= x:
                    i += 1
                    temp = A[j]
                    A[j] = A[i]
                    A[i] = temp
            else:
                if A[j] >= x:
                    i += 1
                    temp = A[j]
                    A[j] = A[i]
                    A[i] = temp
            j += 1
        A[h] = A[i+1]
        A[i+1] = x
        return i+1

    def qsort(self, A, l, h, ascending):
        if l < h:
            m = self.partition(A, l, h, ascending)
            self.qsort(A, l, m-1, ascending)
            self.qsort(A, m+1, h, ascending)

    def quicksort(self, A, ascending=True):
        if len(A) > 0:
            self.qsort(A, 0, len(A)-1, ascending)
            return A
        else:
            print('empty array')