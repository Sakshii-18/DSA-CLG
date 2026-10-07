num = int(input("Enter a number : "))
arm = 0
pow = len(str(num))
temp = num

while num >0:
    arm += (num%10)**pow
    num //= 10
if arm == temp:
    print("Armstrong")
else:
    print("Not Armstrong")