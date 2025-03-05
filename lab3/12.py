def histogram(list):
    for num in list:
        print('*' * num)  

numbers = [int(x) for x in input("Enter numbers : ").split()]
histogram(numbers)
