#Author: Jasffer T. Padigdig
#Date: September 7, 2020
#Description: This code takes an n-input and sorts them in increasing order, the inputs of the users must be integers in order to sort it
#References: 
#https://www.programiz.com/dsa/merge-sort
#https://www.geeksforgeeks.org/merge-sort/
#https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm
#https://www.linkedin.com/learning/introduction-to-data-structures-algorithms-in-java/merge-sort?u=35279340
#

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


length = int(input("Please input how many items you want sorted: "))
A = []

for i in range(length):
    val = int(input(f"Please input the #{i+1} value: "))
    A.append(val)

mergeSort(A)
print(A)