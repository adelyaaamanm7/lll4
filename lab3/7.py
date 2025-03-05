def check(nums):
    numstr = ""
    for num in nums:
        numstr += str(num)
    return "33" in numstr
numbers = [int(x) for x in input("Enter numbers : ").split()]
print("Contains 33:", check(numbers))