"""
Write a program to find the product of all elements of a list.
sample list: [1,2,3,12,32]
output: 2304
"""

inp = list(int(x) for x in input('input elements of the list separated by a comma like <1,2,4>: ').split(','))
print(f'\nyour list: {inp}')

''' Method 1 '''

ans = 1
for x in inp:
    ans *= x
print(ans)

''' Method 2 '''

import math
print(math.prod(inp))