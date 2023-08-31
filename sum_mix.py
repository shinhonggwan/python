# Given an array of integers as strings and numbers, 
# return the sum of the array values as if all were numbers.

def sum_mix(arr):
    #your code here
    sum = 0
    for i in arr:
        sum += int(i)
    return sum