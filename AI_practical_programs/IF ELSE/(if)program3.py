"""
Take 2 numbers as input and if both numbers are equal print area of square, else print area of rectangle
"""

# a , b = (int(x) for x in input('two numbers: ').split(' '))
# print(f'area of square: {a*b}') if a == b else print(f'area of rectangle: {a*b}')

"""
Take 3 numbers as input and find the greatest number of them
"""

# x = list(int(i) for i in input('three numbers: ').split(' ')); x.sort()
# print(f'largest number: {x[-1]}')

"""
Input a int number and check if the number is positive , negetive or 0
"""

inp = int(input('input a num: '))
print('the number is 0') if inp == 0 else print('positive') if inp > 0 else print('negetive')

