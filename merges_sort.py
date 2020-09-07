#Author: Jasffer T. Padigdig
#Date: September 7, 2020
#Description: This code takes an n-input and sorts them in increasing order
#References: 
#https://www.programiz.com/dsa/merge-sort
#https://www.geeksforgeeks.org/merge-sort/
#https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm
#https://www.linkedin.com/learning/introduction-to-data-structures-algorithms-in-java/merge-sort?u=35279340
#
import time
import random

def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        M = A[mid:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            A[k] = M[j]
            j += 1
            k += 1
            

A = []

for i in range(0, 400):
    A.append(random.randint(1, 10000))

print(f"Number of inputs: {len(A)}")
start = time.time()
mergeSort(A)
end = time.time()
print(f"time elapsed: {end-start}")
print(f"elapsed time in milliseconds: {(end-start)*1000}")
print(" ")
print(A)