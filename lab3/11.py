def palindromecheck(word):
    word2 = ''.join(reversed(word))
    return word == word2
word = input()
if palindromecheck(word) :
    print("Yes")
else: 
    print("No")