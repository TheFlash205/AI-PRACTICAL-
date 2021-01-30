"""
Python program to display all the prime numbers within a range
"""

start , end = (int(x) for x in input('please define the starting point and end point of the range like <start-stop>: '
                                     ).split('-'))


def isPrime(num):
    try_list = [1]

    for x in range(2 , num):
        if num % x == 0:
            try_list.append(x)
    try_list.append(num)

    if len(try_list) == 2:
        prime = True
    else:
        prime = False
    try_list.clear()
    return prime

for x in range(start , end+1):
    if isPrime(x):
        print(x)