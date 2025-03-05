def squares(a,b):
    for num in range(a, b + 1):
        yield num ** 2

a, b = map(int, input("Enter two numbers (a b): ").split())
for square in squares(a, b):
    print(square)