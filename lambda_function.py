#1 Write a Python program to create a list and slice the first three elements.
# a=list(map(int,input("Enter Elements for list(Space_seprated): ").split()))
# (lambda a:print(a[:3]))(a)


#2 Create a tuple and demonstrate how to concatenate two tuples.
# t=tuple(map(int,input("Enter nos: ").split()))
# t2=t+(10,20,30)
# print(t2)
# output:
# Enter nos: 101 102 103 104
# (101, 102, 103, 104, 10, 20, 30)


#3 Write a program to check if a given number is even or odd using an if-else statement.
# (lambda n: print("Even") if n%2==0 else print('Odd'))(int(input("Enter No: ")))
# output:
# Enter No: 4
# Even
# Enter No: 3
# Odd


#4 Create a dictionary of 5 items and use a loop to print all keys and values.
# d={'lav':4,'kaira':89,'mira':90,'rahul':24}
# for i,v in d.items():
#     print(i,v)
# output:
# lav 4
# kaira 89
# mira 90
# rahul 24


#5 Write a function to calculate the product of two numbers provided by the user.
# (lambda n1,n2:print(n1*n2))(int(input("Enter n1: ")),int(input('Enter n2: ')))
# output:
# Enter n1: 12
# Enter n2: 12
# 144


#6 Use a lambda function to check if a number is divisible by 3.
# (lambda n: print("Number is  divisible by 3")if n%3==0 else print("Number is not divisible by 3"))(int(input("enter no: ")))
# output:
# enter no: 9
# Number is  divisible by 3
# enter no: 5
# Number is not divisible by 3


#7 Demonstrate slicing to extract the last three elements from a list and a tuple.
# slicing is used to extract  a part of list or tuple 
# (lambda l,t:print((l[-3:],t[-3:])))(list(map(int,input("Enter Elements: ").split())),tuple(map(int,input("Enter Tople elements: ").split())))
# output:
# ([102, 103, 104], (30, 40, 50))


#8 Write a Python program that uses nested if-else to determine if a given year is a leap year.
# lambda n: "Positive" if n>0 else 

#9 Create a set and demonstrate how to find the intersection of two sets.
# with help of intersection function you can find intersection of two sets
# s1={1,2,3,4}
# s2={3,7,8,9,0}
# print(s1.intersection(s2))
# output:
# {3}


#10 Use a for loop to calculate the sum of all numbers in a user-defined list.
# (lambda l: sum(l))(list(map(int,input('Enter Elements: ').split())))


#11 Write a Python function to check if a given string is a palindrome.
# (lambda n:print("palidrome") if n==n[::-1] else print("Not palindrome"))(input("Enter string: "))
# output:
# Enter string: woow
# palidrome
# Enter string: lavanya
# Not palindrome


#12 Use a lambda function to sort a dictionary by its values.
d={1:23,2:56,3:90,4:7,5:1}
print(sorted(d.items(),key=lambda v:v[1]))


#13 Write a program to iterate over a tuple and display only the elements at even indices.
# t=tuple(map(int,input("Enter elements: ").split()))
# l=[]
# print(tuple(t[i] for i in range(len(t)) if i%2==0))


#14 Create a program using if-elif-else to assign grades based on user input (90+ = A, 80–89 = B, etc.).
# n=int(input("Enter grades: "))
# if n>=90:
#     print('A')
# elif(n>=80 and n<=89):
#     print('B')
# elif(n>=40 and n<=79):
#     print('C')
# else:
#     print('Fail')
# output:
# Enter grades: 98
# A
# Enter grades: 32
# Fail

#15 Combine a list and a tuple into a single list and remove duplicate elements using a set.
# l=[10,20,30,10,30]
# t=(20,30,40,10)
# l=list(t)+l
# l=set(l)
# print(l)
# output:
# {40, 10, 20, 30}