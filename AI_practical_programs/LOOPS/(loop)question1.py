"""
Print multiplication table of given number
"""

inp = int(input('Enter the number whose multiplication table you want to see: '))

num , prod = 1 , 1

while num <= 10:
    prod = inp * num
    print(f'{inp} x {num} = {prod}')
    num += 1