def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")

user_input = input("Enter a string: ")
count_upper_lower(user_input)
