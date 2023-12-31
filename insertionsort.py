# -*- coding: utf-8 -*-
"""insertionsort

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OHixTu8lSEDRnpoe3S60SdI-G-6KmRjf
"""

def insertionSort(A) :
    for i in range(1, len(A)) :
        loc = i - 1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc] :
            A[loc + 1] = A[loc]
            loc -= 1
        A[loc + 1] = newItem