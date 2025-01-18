# Section A: Theory (10 Questions)

# 1. What is difference between mutable data type and immutable data type.
# 2. What is floor division.
# 3. explain Break, Continue, Pass statement in python.
# 4. What is difference between for loop and while loop.
# 5. What is dynamically typed langugae.
# 6. What is built in data types in python.
# 7. what is dictionary comprehension? give an example.
# 8. Difference between Shallow copy and Deep copy.
# 9. What is difference between append() and extend() methods.
# 10. What are python modules?
# 11. Explain all file processing modes.

# Section B: Correct the Code (10 Questions)

# 1.Fix the code to display the correct sum of x and y 
x = "10"  
y = 20  
print(int(x)+y)  

# 2.  Fix the code to close the file properly
# file = open("example.txt", "r")  
# file.write("Hello, World!")  
# file.close() 
# print("File written successfully!")  
# ANS:
# file = open("example.txt", "w")  
# file.write("Hello, World!")  
# file.close() 
# print("File written successfully!")  


# 3. Fix this code to properly handle division by zero:
# def divide(a, b):
#      return a / b
# print(divide(10, 0))

# ANS
# def divide(a, b):
#     try:
#       return a / b
#     except:
#        return 'Divison by zero is not possible'
# print(divide(10, 0))


# 4. Fix this code to count the number of vowels in a string:
# def count_vowels(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string:
#         if char not in vowels:
#             count += 1
#     return count

# print(count_vowels("hello"))
# ANS:
# def count_vowels(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("hello"))


# 5. Fix the function to calculate the area of a rectangle
# def calculate_area(length, breadth):  
#     area = length * breadth  
#     print("The area of the rectangle is: ", area)  
# calculate_area(10)  
# ANS:
# def calculate_area(length, breadth=10):  
#     area = length * breadth  
#     print("The area of the rectangle is: ", area)  
# calculate_area(10)  
# ANS:
# The area of the rectangle is:  100


# 6.  Fix this code to handle both integers and strings in a list
# data = [1, 2, "three", 4]  
# total = 0  
# for item in data:  
#     total += item  
# print(total) 
# ANS: 
# data = [1, 2, "three", 4]  
# total = 0  
# for item in data:  
#     try:
#         total += int(item)
#     except:
#         print("Entered string insted of number",item)  
# print(total)  
# output:
# Entered string insted of number three
# 7


# 7.
# data = [1, "banana", 3, "apple", 2]
# data.sort()  
# print(data)
# ANS:
# data=[1,'banana',3,'apple',2]
# try:
#     data.sort()
# except:
#     print("only collections of  intergers or string can be sorted ")
# output:
# only collections of  intergers or string can be sorted 



# 8. Fix this code to handle both integers and strings in a list
# data = [1, 2, "three", 4]  
# total = 0  
# for item in data:  
#     total += item  
# print(total)  
# ANS: 
# data = [1, 2, "three", 4]  
# total = 0  
# for item in data:  
#     try:
#         total += int(item)
#     except:
#         print("Entered string insted of number",item)  
# print(total)  
# output:
# Entered string insted of number three
# 7


# 9.
# def factorial(n):
#     result = 1
#     for i in range(n):
#         result *= i
#     return result
# print(factorial(5))
# ANS:
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
# print(factorial(5))
# output:120

# 10. Fix this nested loop structure to create a diamond pattern correctly:
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(1, n):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
	

# Section C: Write Code For (10 Questions)

# 1. Write a python program to swap two variables without temp variable.
# n1=int(input("Enter no1 "))
# n2=int(input("Enter no2 "))
# print("befor swap",n1,n2)
# n1=n1+n2
# n2=n1-n2
# n1=n1-n2
# print("After swap",n1,n2)
# output:
# Enter no1 10
# Enter no2 20
# befor swap 10 20
# After swap 20 10


# 2. Write a python program to check if number is positive, negative, zero.
# n1=int(input("enter no "))
# if n1==0:
#     print("Zero")
# elif n1>0:
#     print("Number is positive")
# else:
#     print("Number is negative")
# output:
# enter no -19
# Number is negative


# 3. Write a Python function to return the Second maximum number from list.
# lst=[10,20,40,50,60,3,5,6]
# l=list(set(lst))

# for i in range(len(l)):
#     for j in range(len(l)-1):
#         t=0
#         if l[j]>l[j+1]:
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
# new_lst=l[::-1]
# print(new_lst[1])
# output:
# 50


# 4. Write a Python program to print the first 10 numbers of the Fibonacci sequence using a loop.
# n1=0
# n2=1
# print(n1,end=" ")
# print(n2,end=" ")
# for i in range(8):
#     c=n1+n2
#     print(c,end=" ")
#     n1=n2
#     n2=c
# output:
# 0 1 1 2 3 5 8 13 21 34 


# 5. Write a Python program that opens a file, reads the first line, and then appends a new line to the file.
# with open('lect.txt','r') as f:
#   print(f.readline())
# with open('lect.txt','a') as f:
#   f.write("I am new line")
#   f.close()
# # output:
# # Hello World


# 6. Write a Python program using a loop that prints a multiplication table for a given number.
# n=int(input("Enter no "))
# for i in range(1,11):
#     print(n,'X',i,'=',n*i)
# output:
# Enter no 2
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18
# 2 X 10 = 20


# 7. Write a Python function that accepts a string and returns the number of vowels in the string.
# v='aioueAIOUE'
# s=input("Enter string ")
# c=0
# for i in s:
#     if i in v:
#         c+=1
# print(c)
# output:
# Enter string samarthe
# 3


# 8. Write a Python program to print the following half-diamond star pattern:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# n=int(input("enter no "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print('*',end="")
#     print()


# 9. Write a Python program to print a list of prime numbers between 200-250.

# for i in range(200,250):
#     p=1
#     for j in range(2,i):
#         if i%j==0:
#             p=0
#     if p==1:
#         print(i)
# output:
# 211
# 223
# 227
# 229
# 233
# 239
# 241


# 10. Write a Python program that checks if a given number is a perfect number (a number is perfect if it is equal to the sum of its proper divisors).
# n=int(input("Enter no "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
    
# if sum==n:
#     print('Perfect number')
# else:
#     print('Not a perfect number')
# output:
# Enter no 23
# Not a perfect number
# Enter no 28
# Perfect number
# Enter no 6
# Perfect number