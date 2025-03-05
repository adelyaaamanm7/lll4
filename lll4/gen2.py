def evennums(n):
    for i in range(n + 1):
        if (i ** 2) % 2 == 0:
            yield str(i ** 2)

n = int(input())
print(",".join(evennums(n)))


