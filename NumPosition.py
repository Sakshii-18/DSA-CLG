n = int(input("enter a size :"))
arr = []

for i in range(n):
    a = int(input("Enter a number : "))
    arr.append(a)
# print("Your array : ",arr)

find = int(input("enter a number to check if it's in array :"))
found = False
for i in range(0,len(arr)):
    if find == arr[i]:
        print("Number is in Array! It's Position is :", i)
        found = True
        break
    
if not found:
    print("Element not in array ")