

# NumericalPrograms-2-Assignment.txt

# 1.Given a list of integers, write a program to find the maximum and minimum elements in the list without using the max() and min() functions.
# l=[10,20,30,40,506,567]
# min=l[0]
# max=0
# for i in l:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
# print("min: ",min,"max:",max)

# output: min:  10 max: 567

# Write a Python program to remove all duplicate elements from a given list using a set.
# l=[1,2,3,1,2,3,12,13,14,10,20]
# l=set(l)
# print(l)
# output:{1, 2, 3, 10, 12, 13, 14, 20}

# Create a tuple with the elements (1, 2, 3, 4, 5). Write a program to convert this tuple to a list and add the number 6 to the end of the list.
# t=(1, 2, 3, 4, 5)
# t=list(t)
# t.append(6)
# print(t)
# output:[1, 2, 3, 4, 5, 6]

# # Given a dictionary of student names and their marks, write a program to calculate the average marks of all students.
# d={'a':80,'b':70,'c':60,'d':50}
# l=len(d.values())
# print("Avg",sum(d.values())/l)
# output:
# Avg 65.0

# Write a Python program to check whether a given number is even or odd.
# n=9
# if(n%2==0):
#     print('even')
# else:
#     print('Odd')
# output:Odd

# Write a program to check if a given year is a leap year or not.
# year=int(input('Enter Leap Year '))
# if(year%4==0):
#     if(year%100==0 and year%400!=0):
#         print("not Leap year")
#     else:
#         print("Leap Year")
# elif(year%400==0):
#     print("Leap Year")
# else:
#     print("not Leap Year")
# output:
# Enter Leap Year 2024
# Leap Year
# Enter Leap Year 2000
# Leap Year
# Enter Leap Year 1900
# not Leap year
# Enter Leap Year 2001
# not Leap Year
# Write a Python program to print all the even numbers from 1 to 100.
# for i in range(1,100):
#     if(i%2==0):
#         print(i,end=" ")
# output:
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 
# 30 32 34 36 38 40 42 44 46 48 50 52 54 
# 56 58 60 62 64 66 68 70 72 74 76 78 80 
# 82 84 86 88 90 92 94 96 98

# Write a program to print the multiplication table of a given number (up to 10) using a for loop.
# n=3
# for i in range(1,10):
#     print(n,'X',i,'=',n*i)
# output:
# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
# 3 X 4 = 12
# 3 X 5 = 15
# 3 X 6 = 18
# 3 X 7 = 21
# 3 X 8 = 24
# 3 X 9 = 27

# Write a program to find the factorial of a number using a while loop.
# n=5
# fact=1
# while(n>0):
#     fact*=n
#     n-=1
# print(fact)
# output:120

# Write a Python program to check whether a given number is a prime number.
# n=13
# f=1
# for i in range(2,n):
#     if(n%i==0):
#         f=0
# if(f==1):
#     print(f"{n} Prime number")
# else:
#     print(f"{n}  not Prime  number")
# output:
# 13 Prime number
# 10  not Prime  number

# Write a Python program to count how many times a specific number appears in a list.
# d={
# }
# l=[1,2,1,2,1,2,1,3,4,5,6,7,87,8,7,9,10]
# for i in l:
#     d[i]=l.count(i)
# print(d)
# output:
# {1: 4, 2: 3, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2, 
# 87: 1, 8: 1, 9: 1, 10: 1}

# Given two sets, write a Python program to find the union, intersection, and difference between the sets.
# s1={1,2,3,4,5,10,34,2,90}
# s={1,2,3,80,90,10}
# print("Difference",s1.difference(s))
# print("Inytersection",s1.intersection(s))
# print("Union",s1.union(s))

# output:Difference {34, 4, 5}
# Inytersection {1, 2, 3, 10, 90}
# Union {1, 2, 3, 4, 5, 34, 10, 80, 90}
# NumericalPrograms-2-Assignment.txt
# Displaying NumericProblem-Assignment.txt.