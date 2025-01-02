# Write a Python program to remove duplicates from a list and sort the result.
# l=[1,2,3,1,2,3,10]
# l=set(l)
# l=list(l)
# l.sort()
# print(l)
# output:
# [1, 2, 3, 10]

#2 Create a tuple with mixed data types and find the index of a specific element.
# t=(1,2,0.5,'Elv',12,True)
# print(t.index(12))
# output:
# 4


#3 Write a Python program to merge two dictionaries and handle duplicate keys by summing their values.
# d1={'a':23,'b':45}
# d2={'b':4,'c':90}
# print(d1)
# print(d2)
# d={}
# for k in d1.keys():
#     if k in d2.keys():
#         d.update({k:d1[k]+d2[k]})
#         d2.pop(k)
#     else:
#         d.update({k:d1[k]})
# for k in d2.keys():
#     d.update({k:d2[k]})

# print(d)
# output:
# {'a': 23, 'b': 45}
# {'b': 4, 'c': 90}
# {'a': 23, 'b': 49, 'c': 90}


#4 Create a list of squares of even numbers from 1 to 20 using a list comprehension.
# print([i**2 for i in range(1,21) if i%2==0])
# output:
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


#5 Write a program to check if a given number is present in a set using conditionals.
# n=3
# s={1,2,3,5,65,12,11}
# print(n in s)
# output:
# True


#6 Generate a dictionary with keys as numbers from 1 to 5 and values as their cubes using a dictionary comprehension.
# d={i:i**3 for i in range(1,6)}
# print(d)
# output:
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


#7 Write a program to print a right-angled triangle pattern of numbers up to n using loops.
# n= int(input('Enter no: '))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# output:
# Enter no: 5
# * 
# * *
# * * *
# * * * *
# * * * * *


#8 Create a function that accepts a tuple of numbers and returns the maximum and minimum values.
# t=tuple(map(int,input("Enter nos: ").split()))
# print("Minimum: ",min(t),"Maximum: ",max(t))
# output:
# Enter nos: 1 2 3 10
# Minimum:  1 Maximum:  10


#9 Write a Python program to find the union and intersection of two sets.  
# s1=set(map(int,input('Enter elements for set1: ').split()))
# s2=set(map(int,input("Enter elements set2: ").split()))
# print(s1.intersection(s2))
# output:
# Enter elements for set1: 1 2 3 4 10 20
# Enter elements set2: 10 20 30 40
# {10, 20}


#10 Create a nested conditional program to check if a number is divisible by 2, 3, or both.
# n=int(input("Enter no: "))
# if(n%2==0):
#     if(n%3==0):
#         print("Number is divisible by both")
#     else:
#         print("Number is divisiblee by 2 only")
# else:
#     if(n%3==0):
#       print("number is divible by 3 only")
# output:
# Enter no: 15
# number is divible by 3 only  
# Enter no: 2
# Number is divisiblee by 2 only 
# Enter no: 18
# Number is divisible by both  


#11 Write a program to generate a pattern where each row contains the same number as the row number. For example:
# 1  
# 2 2  
# 3 3 3  
# n=int(input('Enter no: '))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# output:
# 1 
# 2 2
# 3 3 3


# Define a function that accepts a list and returns a new list with only the unique elements from the original list.
# l=list(map(int,input("Enter elements: ").split()))
# def unique(l):
#     u=[]
#     for i in l:
#         if i not in u:
#             u.append(i)
#     return u
# print(unique(l))
# output:
# Enter elements: 1 2 3 1 2 3 4 5 6 1 2 
# [1, 2, 3, 4, 5, 6]


# Using a set comprehension, generate a set of all even numbers from 1 to 50.
# s={i for i in range(1,51) if i%2==0}
# print(s)
# output:
# {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50}


# Write a nested loop program to create a multiplication table from 1 to 10.
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,'X',j,'=',(i*j))
#     print()      

# Define a function that accepts a dictionary and a key, and removes the key-value pair if it exists, otherwise returns the dictionary unchanged.
# n=int(input('Enter no of elemnets in dictionary:'))
# d={}
# for i in range(n):
#     key=input("Enter key: ")
#     value=int(input('enter value: '))
#     d.update({key:value})
# print(d)
# k=input("Enter key which you want to remove: ")
# def task(d,k):
#     if k in d.keys():
#         d.pop(k)
#     return d
# print(task(d,k))
# output:
# Enter no of elemnets in dictionary:5
# Enter key: laa
# enter value: 10
# Enter key: mira
# enter value: 20
# Enter key: kira
# enter value: 30
# Enter key: pira
# enter value: 40
# Enter key: opi
# enter value: 50
# {'laa': 10, 'mira': 20, 'kira': 30, 'pira': 40, 'opi': 50}
# Enter key which you want to remove: kira
# {'laa': 10, 'mira': 20, 'pira': 40, 'opi': 50}