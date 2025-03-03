# 1. Write a Python program to reverse a string without using any built-in functions.
# s=input("enter string ")
# r=''
# for i in s:
#     r=i+r
#     print(r)
# print(r)
# 2. Check if a given string is a palindrome.
# s=input("enter string ")
# r=s[::-1]
# if r==s:
#     print("Plaindrom")
# else:
#     print("Not palidrom")
# 3. Count the number of vowels in a string.
# s=input("enter string ")
# c=1
# for i in s:
#     if i in 'aioueAIOUE':
#         c+=1
# print(c)
# 4. Find the frequency of each character in a string.
# d={}
# s=input("enter string ")
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# 5. Write a program to replace all occurrences of a substring in a string.
# s=input("Enter string ")
# sub=input("enter substring ")
# sub1=input("enter substring to be replaced ")
# print(s.replace(sub,sub1))


# 6. Find the longest substring without repeating characters.
# s='hexptyllomruni'
# cur_sub=''
# lon_str=''
# se=set()


# for i in s:
#     if i not in se:
#         cur_sub+=i
#         se.add(i) 
#     else:
#         if len(cur_sub)>len(lon_str):
#             lon_str=cur_sub
#             cur_sub=''
#             se=set()

# if len(cur_sub)>len(lon_str):
#             lon_str=cur_sub
# print(lon_str)

        
        

# l=s.split(" ")
# # print(l)
# ml=0
# sub=''
# for i in l:
#     f=1
#     for j in i:
#         if i.count(j)>1:
#             f=0
#             break
#     if f==1:
#         if len(i)>ml:
#             ml=len(i)
#             sub=i

# print("Longest substring is",sub)

# 7. Write a program to check if two strings are anagrams of each other.
# s1=input("enter string1 ")
# s2=input("enter string2 ")
# if len(s1)==len(s2):
#     f=1
#     for i in s1:
#         if i not in s2:
#             f=0
#             break
#     if f==1:
#         print("Strings are anagrams ")
#     else:
#         print("Not anagrams")
# else:
#     print("Not anagrams")


# 8. Convert the first character of each word in a string to uppercase.
# s=input("Enter string ")
# print(s.title())

# 9. Remove all special characters from a string and keep only alphanumeric characters.
# s=input("enter string ")
# r=''
# for i in s:
#     if i.isalpha():
#         r+=i
# print(r)
# # 10. Write a program to find the number of words in a string.
# s=input("enter string ")
# l=s.split(" ")
# c=0
# for i in l:
#     if len(i)>=2:
#         c+=1
# print("No.of words are",c)

# without using split
# l=[]
# word=''
# for i in s:
#     if i!=' ':
#         word+=i
#     else:
#         l.append(word)
#         word=''
# l.append(word)
# print(l)
# print("Words in list",len(l))