n = int(input("Enter size :"))
arr = []
newArr = []

for i in range(n):
    a = int(input("Enter Number : "))
    arr.append(a)

for i in range(len(arr)):
    if i not in newArr:
        newArr.append(arr[i])
print(newArr)
        
        