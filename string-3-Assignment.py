# 1. Reverse a String
# Write a function that takes a string as input and returns the string reversed, 
# without using Python's built-in reverse method or slicing.
s='lavanya world'
r=''
for i in s:
    r=i+r
print(r)

# output:
# dlrow aynaval

# 2. Count Vowels and Consonants
# Write a function that counts the number of vowels and consonants in a given string.
s='lavanyaworlde'
v='aioueAIOUE'
vc=0
cc=0
for i in s:
    if i in v:
        vc+=1
    else:
        cc+=1
print("Vowel_Count:",vc)
print("constant_Count:",cc)

# output:
# Vowel_Count: 5
# constant_Count: 8

# 3. Palindrome Check
# # Write a function that checks whether a given string is a palindrome (i.e., it reads the same backward and forward).
# s=input('Enter String: ')
# r=s[::-1]
# if(s==r):
#     print("Palindrom")
# else:
#     print("Not Palindrom")

# output:
# Enter String: woow
# Palindrom
# Enter String: woooe
# Not Palindrom
# Enter String: mom
# Palindrom

# 4. String Compression (Optional)
# Write a function that compresses a string by counting consecutive characters. For example, "aaabbbcc" should be compressed to "a3b3c2".
# s=input("enter string ")
# sc=''
# c=1
# for i in range(len(s)-1):#12-11-10
#     if s[i]==s[i+1]:          
#         c=c+1
        
#     else:
#         sc=sc+s[i]+str(c)
#         c=1
# sc=sc+s[i+1]+str(c)
# print(sc)
        
# output:
# enter string: aaabbccddd
# a3b2c2d3             
# enter string: aaabbbcc
# a3b3c2
# enter string aaabbccdde
# a3b2c2d2e1

# 5. Find All Unique Characters in a String
# Write a function that returns a list of all unique characters in a string, keeping the order of their first occurrence.
s='lavanya'
# s=set(s)
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(l)
# output:
# ['l', 'a', 'v', 'n', 'y']
      

# 6. Remove Duplicates from a String
# # Write a function that removes duplicate characters from a string while maintaining the order of the first occurrence.
# s='lavanya'
# r=''
# for i in s:
#     if i not in r:
#         r+=i
# print(r)

# r2=''
# for i in s:
#     if i.count<2:
#         r2+=i
# print(r2)
# output:
# lavny

# 7. String Interleaving
# Write a function that checks if one string is an interleaving of two others. For example, "abc" and "def" can interleave to form "adbcef".
# a b c  d e f 
# a d b c e f

# 8. Find Longest Substring Without Repeating Characters
# Write a function that finds the length of the longest substring in a given string without repeating characters.
# l='i am lavanya leaveslo in solapur'.split(" ")
# max=''
# for i in l:
#     if len(i)>len(max):
#         max=i
# print(max)



# 9. Count the Number of Occurrences of a Substring
# Write a function that counts the number of times a substring appears in a string, ignoring case.

# s=input("Enter string: ").upper()
# sub=input('Enter substring: ')
# l=s.split()
# print(l.count(sub.upper()))
# output:
# Enter string: lava mira lava mirana lava ki
# Enter substring: lava
# 3


# 10. Extract Digits from a String
# Write a function that extracts all digits from a given string and returns them as an integer.
# s=input("Enter String:" )
# r=''
# for i in s:
#     if i.isdigit():
#         r+=i
# print(int(r))
# output:
# Enter String:lavanya 234 556
# 234556

# 11. Capitalize the First and Last Character
# Write a function that capitalizes the first and last character of each word in a string. For example, "hello world" should become "HellO WorlD".
# s=input("Enter string: ")
# l=s.split(" ")
# r=''
# for i in l:
#      r=r+i[0].upper()+i[1:len(i)-1]+i[-1].upper()+" "
# print(r)
# output:    
# Enter string: hello world
# HellO WorlD  
# Enter string: hello wolrd of USA
# HellO WolrD OF USA 

# 12. String Rotation
# Write a function that checks if one string is a rotation of another. For example, "abc" and "cab" are rotations of each other.
# dabc
# cdab
# bcda
# abcd

s1='abcd'
# s2='dcab'#false
s2='dabc'
s=s1
f=0
for i in range(len(s1)):
    s=s[-1]+s[0:len(s)-1]
    if s==s2:
        f=1
        break
if f==1:
    print(True)
else:
    print(False)

# output:
# True 


# 13. Replace All Occurrences of a Substring
# Write a function that replaces all occurrences of a substring in a string with another substring.
# s=input("Enter String: ")
# sub1=input("Enter old sub string: ")
# sub2=input("Enter new substring: ")
# print(s.replace(sub1,sub2))

# l=s.split(" ")
# r=''
# for i in l:
#     if i==sub1:
#         r+=sub2+" "
#     else:
#         r+=i+" "
# print(r)

# output:
# Enter String: hello guyes welcome guyes in our new guyes event
# Enter old sub string: guyes
# Enter new substring: samarth
# hello samarth welcome samarth in our new samarth event
# hello samarth welcome samarth in our new samarth event

# 14. String Without Spaces
# Write a function that removes all spaces from a string.
# s='   bbbhhnni      '
#method 1# print(s.strip())

# method2
# s='lavanya   lava nuytttt lloeoe     '
# r=''
# for i in s:
#   if i!=" ":
#     r+=i
# print(r)


# output:
# bbbhhnni
# lavanyalavanuyttttlloeoe

# 15. Print a String in Reverse Word Order
# Write a function that takes a string and prints the string with the words in reverse order, while keeping each word intact. For example, "I love Python" should become "Python love I".
s="I love Python"
l=s.split(" ")
r=' '
for i in l:
    r=i+" "+r
print(r)
