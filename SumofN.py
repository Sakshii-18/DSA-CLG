n = int(input("Enter a size : "))
arr = []
sum =0

for i in range(n):
    a = int(input("Enter number : "))
    arr.append(a)
    sum += a
print(arr)
print("sum : ",sum)
    