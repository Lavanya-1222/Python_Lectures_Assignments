#1 Write a program that accepts two numbers from the user and displays their sum, product, and division using f-strings.
# n1=int(input("Enter Num1: "))
# n2=int(input("Enter Num2: "))
# print("Sum: ",n1+n2)
# output:
# Enter Num1: 2
# Enter Num2: 2
# Sum:  4


#2 Take a list of integers from the user and print only the unique elements using a set.
# l=list(map(int,input("Enter elements: ").split(" ")))
# l=set(l)
# print(l)
# output:
# Enter elements: 1 2 3 1 2 3 4 5 6 7 8
# {1, 2, 3, 4, 5, 6, 7, 8}


#3 Write a program to generate the following pattern for a given input n:

# 1  
# 12  
# 123  
# 1234  
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")
# output:
# 1
# 12
# 123
# 1234


#4 Take a dictionary as input where keys are student names and values are their scores. Print the name of the student with the highest score.
# n=int(input("Enter no. of students: "))
# d={}
# for i in range(n):
#    name=input("Enter name: ")
#    score=int(input("Enter no: "))
#    d.update({name:score})
# print(d)


# m=max(d.values())
# for k,v in d.items():
#    if(v==m):
#       print(k,v)
#       break
# output:
# Enter no. of students: 3
# Enter name: lavanya
# Enter no: 56
# Enter name: samarth
# Enter no: 80
# Enter name: priya
# Enter no: 45
# {'lavanya': 56, 'samarth': 80, 'priya': 45}
# samarth 80


#5 Write a program to check if a given number is a prime number or not using conditional statements.
# n=int(input("Enter no: "))
# f=1
# for i in range(2,n):
#    if (n%i==0):
#       f=0
#       break
# if(f):
#    print(n,"Prime")
# else:
#    print(n,"Not Prime")
# output:
# Enter no: 24
# 24 Not Prime
# Enter no: 13
# 13 Prime
# Enter no: 2
# 2 Prime


#6 Create a program that accepts a list of strings and counts how many times each string appears in the list.
# l=list(map(str,input("Enter Strings: ").split(" ")))
# print(l)
# d={}
# for i in l:
#        d.update({i:l.count(i)})
# print(d)
# output:
# {'lavanya': 2, 'samarth': 2, 'priya': 1, 'raj': 1}


#7 Write a program to print the union and intersection of two sets given by the user.
# s1=set(list(map(int,input("Enter Elements in s1: ").split(" "))))
# s2=set(list(map(int,input("Enter Elements in s2: ").split(" "))))
# print("Intersection:",s1.intersection(s2))
# print("Union: ",s1.union(s2))
# output:
# Enter Elements in s1: 1 2 3
# Enter Elements in s2: 2 3 4
# Intersection: {2, 3}
# Union:  {1, 2, 3, 4}


#8 Write a program to take a number as input and print its multiplication table up to 10 using a loop.
# n=int(input("Enter no: "))
# for i in range(1,11):
#     print(n,'X',i,'=',n*i)
# output:
# Enter no: 5
# 5 X 1 = 5 
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50


#9 Take a string as input, reverse it using a string method, and check if it is a palindrome.
# there is no function for string to reverse 
# s=input("Enter String: ")
# r="".join(reversed(s))

# if s==r:
#  print('palindrome')
# else:
#  print('not palindrom')

# output:
# Enter String:
# lavanya
# not palindrom
# palindrome


#10 Create a tuple of integers provided by the user, and then find and print the maximum and minimum values.
# t=tuple(map(int,input("enter elements: ").split(" ")))
# print("Maiximum:",max(t),"Minimum:",min(t))
# output:
# enter elements: 10 20 30 40 1 2 3 5678
# Maiximum: 5678 Minimum: 1


#11 Write a program to print the first n Fibonacci numbers, where n is provided by the user.
# n=int(input("Enter Number: "))
# n1=0
# n2=1
# print(n1,n2,end=" ")
# for i in range(2,n):
#     c=n1+n2
#     print(c,end=" ")
#     n1=n2
#     n2=c
# output:
# Enter Number: 5
# 0 1 1 2 3 


#12 Take a number as input and check if it is an Armstrong number
# n=int(input('Enter Number: '))
# r=0
# nu=n
# while(n!=0):
#     c=n%10
#     n=n//10
#     r+=c**3
# if r==nu:
#    print("Armstrong")
# else:
#     print("Not Armstrong")

# output:
# Enter Number: 121
# Not Armstrong
# Enter Number: 153
# Armstrong
# for i in range(len(n)):
       

#13 Write a program that accepts a list of numbers and uses list comprehension to print only the even numbers.
# l=[1,20,30,40,1,2,4,89]
# l2=[i for i in l if i%2==0]
# print(l2)
# output:
# [20, 30, 40, 2, 4]


#14 Write a program using nested loops to generate the following pattern for a given input n:
# markdown

#     *
#    ***
#   *****


#15 Take a string as input and count the number of vowels in it using a combination of string methods and list comprehension.
# s=input("Enter String: ")
# v='aioueAIOUE'
# c=0
# for i in s:
#     if i in v:
#         c+=1
# print(c)
# output:
# Enter String: lavanya
# 3


#16 Write a program that accepts a sentence from the user and returns a dictionary where the keys are words and the values are their lengths.
# s=input("Enter String: ")
# l=s.split(" ")
# d={i:len(i) for i in l }
# print(d)
# output:
# Enter String: hello all am lavanya
# {'hello': 5, 'all': 3, 'am': 2, 'lavanya': 7}


#17 Create a list of integers from 1 to 20 using list comprehension and then create another list containing only the squares of even numbers from the original list.
# l=[i for i in range(1,11)]
# l2=[i**2 for i in l if i%2==0]
# print(l2)
# output:
# [4, 16, 36, 64, 100]


#18 Write a program that takes a sentence as input, converts it to title case, and removes any extra spaces using string methods.
# l=input("Enter String: ")
# t=l.title()
# print(t.strip())
# output:
# Enter String:                          hello all welcome to py 
# Hello All Welcome To Py


#19 Write a program to count the frequency of each character in a string, ignoring spaces, and print the result as a dictionary.
# s=input("Enter string: ").strip()
# d={k:s.count(k) for k in s}
# print(d)
# output:
# Enter string:        lavanya
# {'l': 1, 'a': 3, 'v': 1, 'n': 1, 'y': 1}


#20 Use list comprehension to flatten a 2D list entered by the user into a 1D list.
# l=[10,[20,30],40,50,[60]]
# l2=[]
# for i in l:
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#     else:
#         l2.append(i)
# print(l2)
# output:
# [10, 20, 30, 40, 50, 60]