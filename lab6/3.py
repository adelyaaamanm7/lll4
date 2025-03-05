def check_palindrome(word):
    word=word.casefold()
    new_word=reversed(word)
    if list(word) == list(new_word):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

mystr=input()  
check_palindrome(mystr)


