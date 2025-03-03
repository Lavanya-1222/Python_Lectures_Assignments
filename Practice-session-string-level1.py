# 1. How do you create an empty string in Python?
s=str()
print(s)
# 2. How do you concatenate two strings in Python?
s1='lavanya'
s2='codenera'
print(s1+s2)
# 3. How do you find the length of a string in Python?
s='codenera'
l=len(s)
print(l)
# 4. How do you access the first character of a string in Python?
s='codenera'
print(s[0])
# 5. How do you access the last character of a string in Python?
s='codenera'
print(s[-1])
# 6. How do you slice a string to get the first three characters in Python?
s='codenera'
print(s[0:3])
# 7. How do you check if a substring exists within a string in Python?
s='codenerA'
print('ene' in s)
# 8. How do you convert a string to uppercase in Python?
print(s.upper())
# 9. How do you convert a string to lowercase in Python?
print(s.lower())
# 10. How do you replace a substring within a string in Python?
s='codenera lavanya'
print(s.replace('lavanya','john'))
l=len('lavanya')
for i in range(len(s)):
    if s[i]=='l':
        # print(s[])
        if s[i:l+i]=='lavanya':
            print(True)
            break


# 11. How do you split a string into a list of words in Python?
s='lavanya nagesh miranam'
l=[]
word=''
print(s.split(" "))
for i in range(len(s)):
    if s[i]==" " or i==(len(s)-1):
        if i==(len(s)-1):
            l.append(word+s[i])
        else:
            l.append(word)
        word=""
    else:
        word+=s[i]
print(l)
# 12. How do you join a list of words into a single string in Python?
s=['lavanya', 'nagesh', 'miranam']
print(" ".join(s))

# 13. How do you remove whitespace from the beginning and end of a string in Python?
s='               lavanya miranam         '
print(s.strip())
# 14. How do you find the index of the first occurrence of a substring in a string in Python?
s='lavanyalavanyamiranamnageshkiravo'
print(s.find('ra'))
# 15. How do you count the occurrences of a substring in a string in Python?
s='lavanyalavanyamiranamnageshkiravo'
print(s.count('an'))
# 16. How do you check if a string starts with a certain substring in Python?
s='lavanyalavanyamiranamnageshkiravo'
print(s.startswith('lava'))
# 17. How do you check if a string ends with a certain substring in Python?
s='lavanyalavanyamiranamnageshkiravo'
print(s.endswith('ravo'))
# 18. How do you repeat a string multiple times in Python?
s='lavanya'
print(s*2)
# 19. How do you reverse a string in Python?
s='lavanya'
print(s[::-1])
# 20. How do you check if a string is a palindrome in Python?
s='mom'
if s[::-1]==s:
    print('Palindrom')
else:
    print("Not")

# 21. How do you convert a string to a list of characters in Python?
s='lavanaya'
print(list(s))
# 22. How do you remove all instances of a specific character from a string in Python?
s='lavanya'
r=''
for i in s:
    if i!='a':
        r+=i
print(r)
        

# 23. How do you remove all non-alphabetic characters from a string in Python?
s='lavanyan1234ALPHA'
r=''
for i in s:
    if i.isalpha():
        r+=i
print(r)
# 24. How do you find all the unique characters in a string in Python?
s='lavanya'
r=''
for i in s:
    if i not in r:
        r+=i
print(r)
# 25. How do you find the most frequent character in a string in Python?
s='lavanyamiranam'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
mx=0
chr=''
for k,v in d.items():
    if v>mx:
        mx=v
        chr=k
print(chr)

# 26. How do you find the least frequent character in a string in Python?
s='lavanyamiranam'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
min=d[str(s[0])]
c=''
for k in d:
    if d[k]<=min:
        min=d[k]
        c=k
print(c)
# 27. How do you swap the case of all characters in a string in Python?
s='LvKIvTAopP23@#$'
r=''
print(s.swapcase())
for i in s:
    if i.isupper():
        r+=i.lower()
    else:
        r+=i.upper()
print(r)
# 28. How do you convert a string to title case in Python?
s='mrs mark has  some fruits for charity'
print(s.title())
# 29. How do you check if a string is a valid number in Python?
s='23456'
print(s.isdigit())

# 30. How do you format a string to include variable values in Python?
name='john'
age=78
print(f'{name} is {age} old')