#find all occurence of substing in a given string
s = "banana"
ss = "ana"

for i in range(len(s)):
    for j in range(len(ss)):
         if s[i + j] == ss[j]:
            print(s[i + j])