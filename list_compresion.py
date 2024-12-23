# Write a program to take a list of integers from the user and return a new list containing only the even numbers using list comprehension.
# l=list(map(int,input("Enter list elements: ").split(" ")))

# l1=[i for i in l if i%2==0]
# print(l1)
# output:
# Enter list elements: 10 2 3 4 5 6
# [10, 2, 4, 6]

# Write a program to check if a given string is a palindrome (case-insensitive).

# s=input('Enter String: ')
# r=s[::-1]
# if(s==r):
#     print("Palindrom")
# else:
#     print("Not Palindrom")
# output:
# Enter String: mou
# Not Palindrom
# Enter String: moom
# Palindrom

# Accept two lists of integers from the user and return a list containing the intersection of the two lists (common elements).
# l1=list(map(int,input("Enter list elements: ").split(" ")))
# l2=list(map(int,input("Enter list elements: ").split(" ")))
# l1=set(l1)
# l2=set(l2)
# l3=list(l1.intersection(l2))
# print(l3)

# output:
# [3, 4]


# Create a dictionary from a user-provided list of strings where the keys are the strings and the values are their lengths.
# l1=list(map(str,input("Enter names in list elements: ").split(" ")))
# d={x:len(x)for x in l1}
# print(d)
# output:
# {'lavanya': 7, 'samarth': 7, 'saranya': 7, 'sharda': 6, 'chandrakala': 11, 'nagesh': 6, '': 0}

# Write a program to check if all characters in a given string are unique.
# s=input("Enter String: ")
# s1=set(s)
# if(len(s)==len(s1)):
#     print("Unique")
# else:
#     print("Duplicated")

# output:
# Enter String: lavanya
# Duplicated
# PS C:\Lavanya_Code\Python_Lectures_Assignments> python list_compresion.py
# Enter String: abclv 
# Unique


# Write a program that accepts a tuple of integers and creates a new tuple containing only the odd numbers from it.
# t=(1,2,3,4,5,610,24)
# t2=tuple(i for i in t if i%2!=0)
# print(t2)

# output:
# (1, 3, 5)


# Take a sentence as input and return the count of each word in the sentence using a dictionary.
# s=input("Enter sentance: ")
# l=s.split(" ")
# d={i:l.count(i) for i in l}
# print(d)
# output:
# {'hello': 2, 'am': 1, 'lavanya': 2, 'all': 1}


# Write a program to remove all duplicates from a list while maintaining the original order.
# l=[10,20,30,40,50,10,20,30,30,70]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)
# output:
# [10, 20, 30, 40, 50, 70]


# Create a program to take a list of numbers and return the product of all elements that are divisible by 3 using a loop.
# l=list(map(int,input("Enter Element: ").split(" ")))
# l2=[i for i in l if i%3==0]
# print(l2)

# output:
# Enter Element: 10 20 3 8 9 12 15
# [3, 9, 12, 15]


# Write a program to count how many vowels are present in a user-input string.
# s=input("Enter String: ")
# v='aioueAIOUE'
# c=0
# for i in s:
#     if i in v:
#         c+=1
# print("Vowels",c)
# output:
# Vowels 6


# Create a program that takes a list of integers as input and generates a new list containing their squares using list comprehension.
# l=list(map(int,input("Enter Element: ").split(" ")))
# l2=[i**2 for i in l]
# print(l2)
# output:
# Enter Element: 1 2 3 4
# [1, 4, 9, 16]


# Write a program to check if two strings are anagrams of each other (case-insensitive).
s1=input('Enter String1: ')
s2=input('Enter String2: ')
if(len(s1)==len(s2)):
    if str(sorted(s1))==str(sorted(s2)):
       print("strings are anagram")
    else:
        print("Not")
else:
    print("Not")
# # output:
# Enter String1: abc
# Enter String2: bca
# strings are anagram
# PS C:\Lavanya_Code\Python_Lectures_Assignments> python list_compresion.py
# Enter String1: codenra
# Enter String2: nracode 
# strings are anagram
# PS C:\Lavanya_Code\Python_Lectures_Assignments> python list_compresion.py
# Enter String1: code
# Enter String2: con
# Not
# PS C:\Lavanya_Code\Python_Lectures_Assignments> python list_compresion.py
# Enter String1: code
# Enter String2: dode
# Not

# Accept a tuple of strings from the user and sort it alphabetically.
# t=tuple(map(str,input("Enter String: ").split(" ")))
# print(sorted(t))
# output:
# Enter String: lava abc hiy zyz
# ['abc', 'hiy', 'lava', 'zyz']


# Create a program to find the second-largest number in a user-input list of integers.
# t=set((map(int,input("Enter Elements: ").split(" "))))
# l=list(t)
# l.sort(reverse=True)
# print(l[1])
# output:
# Enter Elements: 10 20 34 56 78 89
# 78


# Write a program that accepts a string and a character, then finds all the positions of that character in the string.
# s=input("Enter String: ")
# c=input("enter Charecter: ")
# l=[]
# for i in range(len(s)):
#     if s[i]==c:
#         l.append(i)
# print(l)  
# output: 
# Enter String: lavanya
# enter Charecter: a
# [1, 3, 6]    


# Write a program that accepts a nested list of integers and flattens it into a single list using nested loops.
# l=[10,20,[10,30],67,90,[1,2,3]]
# l2=[]
# for i in l:
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#     else:
#         l2.append(i)
# print(l2)
# output:
# [10, 20, 10, 30, 67, 90, 1, 2, 3]


# Write a program to take a string as input and generate all unique substrings of the string using sets.
# s=set(input("enter string: ").split(" "))
# print(s)
# output:
# {'nuya', 'lava', 'am'}

# Accept a list of tuples where each tuple contains a string and an integer. Sort the list based on the integer values in descending order.
l=[('lava',24),('abc',80)]

# print(d)