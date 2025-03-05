def uniqel(lst):
    unique_list = []  
    for item in lst:  
        if item not in unique_list:
            unique_list.append(item)  
    return unique_list  


numbers = [int(x) for x in input("Enter numbers: ").split()]

print("Unique elements:", uniqel(numbers))
