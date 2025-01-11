# Section A: Theory  

# 1. Explain the difference between if, elif, and else statements in Python.  

# 2. What is a nested loop? Provide an example of when you might use one.  

# 3. Define the term "function" in Python and explain its advantages.  

# 4. What is the purpose of the return statement in a function?  

# 5. Explain the use of lambda functions in Python. How are they different from regular functions?  

# 6. What is a Higher-Order Function (HOF)? Provide two examples.  

# 7. Describe the difference between while loops and for loops.  

# 8. Explain the purpose of the break and continue statements in loops.  

# 9. What are default arguments in functions? Provide an example.  

# 10. How can a function return multiple values in Python?  

# Section B: Correct the Error  
# 1.   
# if x=10:  
#        print("x is 10") 
# ANS:
# x=10
# if x==10:
#     print(x) 
# output:
# 10


# 2.   
#    for i in range(10)  
#        print(i)  
# ANS:
# for i in range(10):
#     print(i)  
# 
#   
# 3.   
#    def greet(name)  
#        return "Hello" + name  
# def greet(name):
#     return "Hello"+ name
# print(greet("lavanya"))
# output:Hellolavanya


# 4.   
# numbers = [1, 2, 3, 4, 5]  
# print(numbers[5]) 
 
# output:
# print(numbers[4])
# list index out of range  


# 5.   
# lambda x, y: x + y  
# print(lambda(5, 10))  

# ANS:
# output:
# invalid Syntax
# print((lambda x, y: x + y)(5,10)) 
# 15 


# 6.   
#    def add(a, b):  
#        print(a + b  
# ANS:
# sysntax Error
# def add(a,b):
#     print(a+b)
# add(10,20)
# output:
# 30


# 7.   
# while True:  
#        print("Looping...")  
# continue  
# ANS: syntax Error continue not properly in loop 


# 8.   
# hof = map(lambda x: x * 2, [1, 2, 3, 4])  
# print(hof[0])  

# ANS:
# map oject not subscriptable 
# hof = list(map(lambda x: x * 2, [1, 2, 3, 4]))
# print(hof[0])

     
# 9.   
# def multiply(x, y = 2):  
#        return x * y  
# print(multiply())  
# ANS:
# TypeError: missing 1 argument
# def multiply(x, y = 2):  
#        return x * y  
# print(multiply(10))


# 10.   
# result = lambda x: x  2  
# print(result 5)  
# ANS
# result = lambda x: x * 2
# print(result(5)) 
      

# Section C: Write a Program

#1 Write a program to find the largest of three numbers using conditional statements.
# n1=int(input("Enter no1: "))
# n2=int(input("Enter no2: "))
# n3=int(input("Enter no3: "))
# if n1>n2 and n1>n3:
#     print(n1,"is greater")
# elif n2>n3 and n2>n1:
#     print(n2,'greater')
# else:
#     print(n3,'greater')
# output:
# Enter no1: 10
# Enter no2: 20
# Enter no3: 30
# 30 greater   


#2 Write a program to print all prime numbers between 1 and 50 using a loop.
# list=[]
# for i in range(2,51):
#     f=1
#     for j in range(2,i):
#         if i%j==0:
#             f=0
#     if f==1:
#         list.append(i)
# print(list)
# output:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        

#3 Create a function that takes a list of numbers and returns the sum of its elements.
# l=[10,20,30,40,1,2,3,4]
# sum=0
# for i in l:
#     sum+=i
# print("Sum=",sum)
# output: 110


#4 Write a lambda function to calculate the square of a given number.
# x=int(input("Enter no "))
# print((lambda x: x**2)(x))
# output:
# 100


#5 Implement a program to check whether a given number is a palindrome using a loop.
# n=int(input("Enter no "))
# r=0
# n1=n
# while(n!=0):
#     d=n%10
#     r=r*10+d
#     n=n//10
# print(r)
# if n1==r:
#     print("Palindrom")
# else:
#     print("Not palindrom") 
# output:
# Enter no 1221
# 1221
# Palindrom


#6 Write a function that takes two arguments and returns the greater of the two.
# n1=int(input("Enter no1 "))
# n2=int(input('Enter no2 '))
# if n1>n2:
#     print(n1,'Greater')
# else:
#     print(n2,'greater')
# output:
# Enter no1 12
# Enter no2 23
# 23 greater


#7 Create a Higher-Order Function that applies a given function to each element in a list.
# list=[1,2,3,4,5]
# def func(list):
#     return sum(list)
# def HOF(fun,list):
#     return fun(list)
# print(HOF(func,list))
# output:
# 15


#8 Write a program to calculate the factorial of a number using recursion.
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))
# output:
# 120


# #9 Create a function that filters out odd numbers from a list using filter and a lambda function.
# list=[1,20,3,40,5,7]
# list=filter(lambda x:x%2!=0,list)
# print(tuple(list))
# output:
# (1, 3, 5, 7)


#10 Write a program to count the number of vowels in a given string using loops and conditionals.
# v='aioueAIOUE'
# s=input("Enter string ")
# c=0
# for i in s:
#    if i in v:
#       c+=1
# print(c)
# output:
# Enter string lavanya
# 3