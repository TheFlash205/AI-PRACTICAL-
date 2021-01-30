"""
Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [0, 40]
Compare each element of array1 and array2
[ True False False True False]
"""

import numpy as np

arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([0, 40])
print(f'answer: {np.in1d(arr1, arr2)}')
