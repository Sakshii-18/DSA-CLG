num = int(input("Enter a num : "))
sum = 0

while num>0:
    sum = sum*10+(num%10)
    num //= 10
if num == sum:
    print("Number is Palindrome")
else:
    print("Number isn't Palindrome")