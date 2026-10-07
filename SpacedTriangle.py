n = 6

for i in range(1, n + 1):

    for j in range(n, i, -1):
        print(end=" ")

    for k in range(1, i + 1):

        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()