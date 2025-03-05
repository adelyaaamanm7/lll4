def check2(nums):
    sequence = "007"
    numstr = ""
    for num in nums:
        numstr += str(num)
    return sequence in numstr
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Contains 007:", check2(numbers))