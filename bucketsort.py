# -*- coding: utf-8 -*-
"""bucketsort

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T5DaR64Lx6INSijAQsP_Fei8EPoiE-H7
"""

import math
from insertionsort import insertionSort

def bucketSort(A) :
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n) :
        B[math.floor(n * A[i])].append(A[i])
    A.clear()
    for i in range(n) :
        insertionSort(B[i])
        A.extend(B[i])