n = int(input("ener size of n :"))
arr = []
even = 0
odd =0

for i in range(n):
    a = int(input("Enter Number : "))
    arr.append(a)
    
    if(a%2 == 0):
        even = even+1
    else:
        odd = odd+1
        
print("Even : ",even)
print("Odd : ",odd)