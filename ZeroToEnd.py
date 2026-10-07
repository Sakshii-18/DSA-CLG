n = int(input("Enter size :"))
arr = []
index =0

for i in range(n):
    a = int(input("Enter a number :"))
    arr.append(a)
print(arr)

for i in arr:
    if i != 0:
        arr[index] = i
        index += 1
       

for i in range(index,len(arr)):
    arr[index] = 0
    index += 1
   
     
print(arr)




    
