# 1-Reverse a string using a loop.
s='helloworldofUSA'
r=''
for i in s:
    r=i+r
print(r)

# output:
# ASUfodlrowolleh

# 2-Count the occurrences of a specific character in a string using a loop.
# chr='l'
# c=0
# s='helloworldofUSA'
# for i in s:
#     if i==chr:
#         c+=1
# print(c)

# output:3

# 3-Remove leading and trailing whitespaces from a string without using strip().
s='     lava     '
r=''
for i in s:
    if i!=' ':
        r+=i
print(r)

# output: lava

# 4-Replace all occurrences of a character in a string with another character using a loop.
s='helloworldofUSA'
# print(s.replace('l','P'))
# chr='R'
# r=''
# for i in s:
#     if i=='l':
#         r+=chr
#     else:
#         r+=i
# print(r)
# output:heRRoworRdofUSA

# 5-Split a sentence into words using a loop.
s='hello world of USA lavanya'
l=[]
start=0
e=0
for i in range(len(s)):
    if s[i]==' ':
        l.append(s[start:i])
        start=i+1
    elif i==len(s)-1:
        l.append(s[start:i+1])
    
print(l)

# output:
# ['hello', 'world', 'of', 'USA', 'lavanya']


# 6-Format a string with values (e.g., name and city) without using the format() method.
name='lavanya'
city='Solapur'
s='Hello '+name+' your City is '+city
print(s)

# ouput:
# Hello lavanya your City is Solapur


# 7-Print the string with escape characters (e.g., \n, \t, \r) visible, without actually executing them.
print("\\nhello\\tworld\\rlavanya\\b nb\"kk\\")
# output:
# \nhello\tworld\rlavanya\b nb"kk\

# 8-Convert all characters of a string to uppercase using a loop.
l='hello world'
s=''
for i in l:
    if i==" ":
        s+=i
    s+=chr(ord(i)-32)

print(s)
# output:
# HELLO WORLD

# 9-Convert all characters of a string to lowercase using a loop.
l='HELLO WORLD'
s=''
for i in l:
    if i==" ":
        s+=i
    s+=chr(ord(i)+32)

print(s)

# 10-Count how many words are in a string without using split().
s='Hello world of USA'
l=[]
start=0
for i in range(len(s)):
    if s[i]==' ':
        l.append(s[start:i])
        start=i+1
    if i==len(s)-1:
        l.append(s[start:i+1])
print('count:',len(l))
# output:count: 4


# 11-Remove extra spaces between words in a string.
s=' lavan mirana kee '
s2=''
for i in s:
    if i!=' ':
        s2+=i
print(s2)
# output:
# lavanmiranakee

# 12-Replace all occurrences of a substring in a string without using replace().
s='anlavanyamiraancodeneran'
s2=''
chr='an'
l=len(chr)
start=0
for i in range(len(s)):
    if chr==s[start:l+start]:
        s2+='0'
        start=l+i
    else:
        s2+=s[start]
        start=i
print(s2)
# output:
# 0lnlav0ayamira0ocodener0
