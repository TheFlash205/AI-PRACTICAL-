"""
An online shopping portal gives a discount of 10% if the user orders more than 20 quantities of chocolates
assuming that one piece costs ₹10, take input of number of quantities ordered and print the payable amount.
"""

num = int(input('Enter the amount of chocolates that you want to buy: '))
if num > 20:
    cost = (num * 10)/10
    print(f'amount to be paid: ₹{int(cost)}')
else:
    cost = (num * 10)
    print(f'amount to be paid: ₹{int(cost)}')