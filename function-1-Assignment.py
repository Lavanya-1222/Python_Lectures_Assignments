# Write a Python program to find the second largest number in a list.
# l=[1,2,3,4,10,20,40,40,50,30,30]
# l=list(set(l))
# l.sort(reverse=True)
# print(l)
# print(l[1])
# output:
# 40


# Create a function that takes a string and returns a dictionary with the count of each character.
# s=input('Enter String: ')
# d={}
# for i in s:
#     d.update({i:s.count(i)})
# print(d)
# output:
# Enter String: lavanya
# {'l': 1, 'a': 3, 'v': 1, 'n': 1, 'y': 1}


#3 Write a Python program to generate and print a set of all unique vowels present in a given string.
# v='aioueAIOUE'
# s='lavanyaeu'
# u=[]
# for i in s:
#     if i in v:
#         if i not in u:
#              u.append(i)
# print(u)
# output:
# ['a', 'e', 'u']


#4 Using a list comprehension, create a list of squares of even numbers from 1 to 50.
# l=[i**2 for i in range(1,50) if i%2==0]
# print(l)


#5 Write a Python program to reverse a tuple without converting it into a list.
# t=(1,2,3,4,10,203,0)
# print(list(reversed(t)))
# output:
# [0, 203, 10, 4, 3, 2, 1]


#6 Implement a function to check if a number is prime or not.
# n=int(input("enter no: "))
# def prime_check(n):
    
#     f=1
#     for i in range(2,n):
#         if n%i==0:
#             f=0
#     if (f==0):
#         print(n,"not Prime")
#     else:
#         print(n,"Prime")
# prime_check(n) 
# output:
# enter no: 5
# 5 Prime
# enter no: 24
# 24 not Prime


#7 Write a Python program to print a pattern of stars in a pyramid shape with n rows.
# n=int(input('enter no: '))
# for i in range(1,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end="")
#     for k in range(1,i*2):
#         print('*',end="")
#     print()
# output:
# enter no: 3
#   *
#  ***
# *****

#8 Create a dictionary where keys are numbers from 1 to 10, and the values are their cubes.
# d={i:i**3 for i in range(1,11)}
# print(d)
# output:
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}

#9 Write a Python program to calculate the sum of all numbers in a list using a for loop.
# l=list(map(int,input('Enter Elements: ').split()))
# sum=0
# def sumlist(l):
#     sum=0
#     for i in l:
#         sum+=i
#     return sum
# print("Sum_Elements: ",sumlist(l))
# output:
# Enter Elements: 1 2 3 4 
# Sum_Elements:  10


#10 Create a set comprehension that contains the squares of all odd numbers from 1 to 20.
# s={i**2 for i in range(1,21) if i%2!=0}
# print(s)
# output:
# {1, 121, 225, 289, 9, 169, 361, 81, 49, 25}


#11 Implement a function that takes a list and returns a tuple with the minimum and maximum values.
# l=list(map(int,input("Enter elements: ").split()))
# def min_max_tuple(l):
#     return (min(l),max(l))
# print(min_max_tuple(l))
# output:
# Enter elements: 1 2 3 100 200 34
# (1, 200)


#12 Write a program to display the Fibonacci series up to n terms using a user-defined function.
# n=int(input("enter number: "))
# def fibo(n):
#     if n==1:
#         print(0,1)
#     else:
#         n1=0
#         n2=1
#         print(n1)
#         print(n2)
#         for i in range(n-2):
#             c=n1+n2
#             print(c)
#             n1=n2
#             n2=c
# fibo(n)
# output:
# enter number: 5
# 0
# 1
# 1
# 2
# 3
# enter number: 1
# 0 1

#13 Generate a pattern with numbers in increasing order, such as:
# 1  
# 1 2  
# 1 2 3  
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# output:
# 1 
# 1 2 
# 1 2 3


#14 Write a Python program to merge two dictionaries and handle duplicate keys by summing their values.
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


# Using a while loop, create a program that checks if a string is a palindrome.
# s=input('Enter string: ')
# r=''
# n=len(s)-1
# while(n>=0):
#     r+=s[n]
#     n-=1
# if r==s:
#     print('palindrome')
# else:
#     print('Not palindrome')
# output:
# Enter string: 1221
# palindrome
# Enter string: lavanya
# Not palindrome   