from math import prod
def multiply_list(nums):
    return prod(nums) 
numbers = list(map(int, input().split()))
result = multiply_list(numbers)
print(result)
