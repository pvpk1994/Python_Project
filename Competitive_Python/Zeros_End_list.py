'''
Zeros- End list
Author: Pavan Kumar Paluri
Source: Self
'''

# my_list = [3, 0, 0, 1, 5, 7, 0, 3, 0, 5, 2, 6, 0, 1, 2, 3, 0, 2, 0, 4, 5, 0, 1, 0, 0, 0]
my_list = [0, 3, 0, 1, 0, 0]
new_list = []

for val in my_list[:]:
    if val == 0:
        # my_list.pop()
        new_list.append(val)
'''
for val_new in my_list:
    if val_new == 0:
        # my_list.pop(my_list.index(val_new))
        my_list.remove(val_new)
'''
'''
Cannot modify a list at the same time while iterating over it...
'''
# Using shallow copy
for num in my_list[:]:  # iterate over shallow copy
    if num == 0:
        my_list.pop(my_list.index(num))

for val in new_list:
    my_list.append(val)

print(my_list)