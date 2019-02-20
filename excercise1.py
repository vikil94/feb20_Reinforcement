#
# Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.
#
# Test it to make sure it works.

def sum_odd(list):
    sum = 0
    for num in range(0,len(list)):
        if list[num] % 2 == 1:
            sum += list[num]
    return sum


this_list = [333, 221, 220, 540, 671, 591, 2209, 431134]

print(sum_odd(this_list))
