# 
# All posile substrings
s='abc'

for i in range(len(s)):
    for j in range(i+1):
        print(s[j],end="")
    print()