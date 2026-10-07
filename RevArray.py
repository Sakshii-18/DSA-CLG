n = int(input("Enter size :"))
arr = []


for i in range(n):
    a = int(input("Enter array Element :"))
    arr.append(a)
    
# for j in range(len(arr),0,-1):
#    print(arr[j])

start = 0
end = len(arr)-1

for i in range(start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        
        start +=1
        end -= 1
print(arr)

        
    