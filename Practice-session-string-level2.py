# 1. Reverse a String: Write a function to reverse a string without using Python's built-in functions.
# s=input("enter string ")
# print(s[::-1])

# 2. Check if a String is Palindrome: Implement a function to check if a string reads the same forward and backward.
# s=input("enter string ")
# if s==s[::-1]:
#     print("Palindrom")
# else:
#     print("not Palindrom")

# 3. Count Vowels in a String: Write a function to count the number of vowels in a given string.
# s=input("enter string ")
# c=0
# for i in s:
#     if i in 'aioueIOUE':
#         c+=1
# print("no of Vowel:",c)

# 4. Check for Anagram: Write a function to check if two strings are anagrams of each other.
# s1=input("enter string1 ")
# s2=input("enter string2 ")
# if len(s1)==len(s2):
#     f=1
#     for i in s1:
#         if i not in s2:
#             f=0
#             break
#     if f==1:
#         print("Angrams")
#     else:
#         print("Not Angrams")
# else:
#     print("Not anagrams")

# 5. First Non-Repeating Character: Write a function to find the first non-repeating character in a string.
# s=input("enter string ")
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# chr=''
# for i in d:
#     if d[i]==1:
#         chr=i
#         break
# print("!st non reapating charecter ",chr)

# 6. Remove Duplicates: Implement a function that removes duplicate characters from a string while preserving the order.
# l=input("enter string ")
# r=''
# s=set()
# for i in l:
#     if i not in s:
#         r+=i
#         s.add(i)
# print(r)
# 7. Count Substring Occurrences: Write a function to count the occurrences of a substring in a given string.
# s=input("enter string ")
# sub=input("enter sub string ")
# print(s.count(sub))

# 8. Compress a String: Write a function to compress a string with counts of repeated characters (e.g., "aaabb" becomes "a3b2").
# s=input("enter sting ")
# r=''
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for i,v in d.items():
#     r=r+i+str(v)
# print(r)

# 9. Check if String Contains Only Digits: Write a function to check if a string contains only numeric digits.
# s=input("enter string ")
# if s.isdigit():
#     print("true")
# else:
#     print("false")
# 10. Longest Common Prefix: Write a function to find the longest common prefix among an array of strings.
# l=list(map(str,input("enter string elements ").split(" ")))
# # ['flower', 'fly', 'flit

