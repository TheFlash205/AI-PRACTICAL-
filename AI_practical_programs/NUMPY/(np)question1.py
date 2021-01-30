"""
Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees.
Centigrade values are stored into a NumPy array.
Sample Array [0, 12, 45.21 ,34, 99.91]
"""

import numpy as np

sample_array = [0, 12, 45.21 ,34, 99.91]
sample_array = np.array(sample_array)
print(f'answer: {(5*sample_array/9 - 5*32/9)}')

