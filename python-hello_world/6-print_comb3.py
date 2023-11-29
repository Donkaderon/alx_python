for i in range(10):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end="")
        if i != 8 or j != 9:
            print(", ", end="")

print()

for i in range(0, 9):
    for j in range(i+1, 10):
        print("{:d}{:d}".format(i, j), end=', ')

print ()