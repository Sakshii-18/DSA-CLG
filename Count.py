#Count Vowels, consonants,digits , specials characters

s = input("Enter a String : ")
v = "aeiouAEIOU"
n = "1234567890"
c = "#@!~$%^&*()_"
vcount = 0
ncount = 0
scount = 0

for i in s:
    for j in v:
        if i == j:
            vcount = vcount+1
   
    for k in n :
        if k == i:
            ncount = ncount+1
   
    for l in c:
        if l == i:
            scount = scount +1
   
print("Vowels : ",vcount)
print("Number Count : ", ncount)
print("Special Character count : ", scount)