#1 Write a Python program to create a list of numbers from 1 to 10 and print it.
# l=[i for i in range(1,11)]
# print(l)
# output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#2 Check if a given string is a palindrome (reads the same backward as forward).
# r=input('Enter String:')
# if(r==r[::-1]):
#     print('Palindrom')
# else:
#     print('Not Palindrom')
# output:
# Enter String:laba
# Not Palindrom
# Enter String:mom
# Palindrom


#3 Write a Python program to count the occurrences of each character in a given string using a dictionary.
# s=input("Enter strin: ")
# d={i:s.count(i) for i in s}
# print(d)


#4 Create a set of unique vowels from a user-provided string.
# s=input('enter string: ')
# v='aioueAIOUE'
# s1=set()
# for i in s:
#     if i in v:
#         s1.add(i)
# print(s1)
# output:
# enter string: lavanya
# {'a'}


#5 Use a conditional statement to check whether a number entered by the user is even or odd.
# n=int(input("Enter no: "))
# print('even') if n%2==0 else print('ODD')
# output:
# Enter no: 8
# even
# Enter no: 5
# ODD


#6 Write a Python program to print the first 10 Fibonacci numbers using a loop.
# n=int(input("enter no: "))
# n1=0
# n2=1
# print(n1,n2)
# for i in range(n-2):
#     c=n1+n2
#     print(c)
#     n1=n2
#     n2=c
# output:
# enter no: 5
# 0 1
# 1
# 2
# 3


#7 Create a dictionary where keys are numbers from 1 to 5, and values are their squares. Iterate over this dictionary to print each key-value pair.
# d={k:k**2 for k in range(1,6)}
# for k in d.items():
#     print(k)

# output:(1, 1)
# (2, 4)
# (3, 9)
# (4, 16)
# (5, 25)


#8 Use nested loops to generate the following pattern:
# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# for i in range(4):
#     for j in range(1,i+2):
#         print(j,end=" ")
#     print()
# output:
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4


#9 Write a function to calculate the factorial of a number using recursion.
# n=int(input("Enter no: "))
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n))
# output:
# Enter no: 5
# 120


#10 Write a Python program to find the second largest number in a list using loops (without using built-in functions).
# l=[10,20,30,30,40,40]
# l=list(set(l))
# for i in range(len(l)-1):
#     t=0
#     if l[i]<l[i+1]:
#         t=l[i]
#         l[i]=l[i+1]
#         l[i+1]=t
# print(l[1])
# output:
# 20


#11 Use enumerate to print the index and value of each item in a tuple.
# t=(10,20,30,40)
# for i,x in enumerate(t):
#     print(i,x)
# output:
# 0 10
# 1 20
# 2 30
# 3 40


#12 Implement a program that checks whether a given number is a prime number using a loop and nested conditional statements.
# n=int(input("enter no: "))
# f=0
# for i in range(2,n):
#     if n%i==0:
#         f=1
# if f==1:
#     print("Not Prime")
# else:
#     print("Prime")
# output:
# enter no: 6
# Not Prime
# Prime


#13 Write a Python program to merge two dictionaries and sum the values of common keys.
# d1={'a':23,'b':45}
# d2={'b':4,'c':90}
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
# {'a': 23, 'b': 49, 'c': 90}


#14 Write a program to generate Pascal's triangle up to a given number of rows using nested loops.
n=int(input("enter no: "))


#15 Create a lambda function to filter out even numbers from a list of integers.
l=[10,20,30,40,50]
# print((lambda k:for k in l k if k%2==0 )(l))




#16 Write a Python program to reverse the words in a sentence using list comprehensions and string manipulation.
# s='i am python'
# l=s.split(" ")
# r=" ".join([l[x] for x in range(len(l)-1,-1,-1)])
# print(r)
# output:python am i


#17 Write a recursive function to compute the sum of all elements in a nested list (e.g., [[1, 2, [3, 4]], 5]).

#18 Use a nested loop to create the following pattern:
# *  
# * *  
# * * *  
# * *  
# *  

#19 Implement a program that creates a dictionary from a string where each word is a key, and its value is the frequency of the word.
# l='am python  am python javascript included'
# d={i:l.count(i) for i in l.split(" ")}
# print(d)
# output:
# {'am': 2, 'python': 2, '': 41, 'javascript': 1, 'included': 1}

#20 Write a Python program that takes a list of tuples, sorts them based on the second element of each tuple using a lambda function, and prints the result.
l=[(10,20),(30,40),(50,1),(60,2)]
print(sorted(l,key=lambda l:l[1]))
pr