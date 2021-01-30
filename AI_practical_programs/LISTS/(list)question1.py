"""
Make a list by taking 10 input from user. Now delete all repeated elements of the list.
E.g.-
INPUT : [1,2,3,2,1,3,12,12,32]
OUTPUT : [1,2,3,12,32]
"""

inp = list(int(x) for x in input('input elements of the list separated by a comma like <1,2,4>: ').split(','))
print(f'\nyour list: {inp}')
new_list = list(set(inp)); new_list.sort()
print(f'your list without duplicates: {new_list}')