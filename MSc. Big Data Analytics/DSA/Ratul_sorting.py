# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:44:35 2022

@author: RATUL
"""

# Insertion Sort
def insertion(A):
    n = len(A)
    for i in range(n):
        j = i
        while j > 0:
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    return A


# Selection Sort
def selection(A):
    n = len(A)
    for j in range(n):
        k = j
        i = j + 1
        while i < n:
            if A[i] < A[k]:
                k = i
            i += 1
        if k != j:
            A[j], A[k] = A[k], A[j]
    return A


# Bubble Sort
def bubble(A):
    n = len(A)
    for i in range(1, n):
        for j in range(n - i):
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]
    return A


# Heap Sort
def heapify(A, i, n):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, n)


def heapsort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, i, n)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)
    return A


# Merge Sort
def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergesort(L)
        mergesort(R)
        # merge
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


# Quick Sort
def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h
    while i < j:
        while A[i] <= pivot and i < h:
            i += 1
        while A[j] > pivot and j > l:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quicksort(A, l, h):
    if l < h:
        j = partition(A, l, h)
        quicksort(A, l, j)
        quicksort(A, j + 1, h)


# initialization
def array():
    global A
    A = []
    x = int(input("Enter the number elements in the array:  "))
    for i in range(x):
        z = int(input(f"Enter the {i+1}th element:  "))
        A.append(z)
    print("The array has been initialized.")


A = []
array()
y = 10
while y != 0:
    y = int(input("Press 1 for Insertion Sort, 2 for Selection Sort, 3 for Bubble Sort,\n"
                  "4 for Heap Sort, 5 for Merge Sort, 6 for Quick Sort,\n"
                  "7 for Traversal, 8 for re-initializing array,\n"
                  "0 to Exit:  "))
    if y == 1:
        insertion(A)
        print("Insertion Sort Executed.")
    elif y == 2:
        selection(A)
        print("Selection Sort Executed.")
    elif y == 3:
        bubble(A)
        print("Bubble Sort Executed.")
    elif y == 4:
        heapsort(A)
        print("Heap Sort Executed.")
    elif y == 5:
        mergesort(A)
        print("Merge Sort Executed.")
    elif y == 6:
        quicksort(A, 0, len(A)-1)
        print("Quick Sort Executed.")
    elif y == 7:
        print("Currently the array is:")
        print(A)
    elif y == 8:
        array()
    elif y == 0:
        print("Execution Stopped.")
        print("See You Later ^o^")
    else:
        print("Wrong Choice.")

