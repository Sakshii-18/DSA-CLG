n = int(input("Enter a size :"))
arr = []



for i in range(1,n):
    a = int(input("Enter a numbers in array :"))
    arr.append(a)
print(arr)
   
largest = arr[0] 
slargest = arr[0]
smallest = arr[0] 
ssmallest = arr[0] 

for i in range(len(arr)):
    if(largest<arr[i]):
        slargest = largest
        largest = arr[i]
       
    elif(slargest < arr[i] and arr[i] != slargest ):
        slargest = arr[i]
    
    if(smallest>arr[i]):
        ssmallest = smallest
        smallest = arr[i]
        
    elif(slargest > arr[i] and arr[i] != slargest ):
            slargest = arr[i]
        
        
        
print("Smallest : ", smallest)
print("Second Smallest : ", ssmallest)
print("Largest : " ,largest)
print("Second Largest : " ,slargest)
        
