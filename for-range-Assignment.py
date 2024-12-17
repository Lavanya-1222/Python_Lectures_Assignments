
# For-range()-AssignmentFor-range()-Assignment
# 1-Given a list of numbers, return the largest number in the list without using the max() function.
# l=[10,20,30,1,2,3,90,67,5]

# max=0
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
# print(max)
# output:90

# 2- Given a list of integers, create a new list containing the square of each number in the original list.
# l=[1,2,3,4,5,10,11]
# r=[]
# for i in range(len(l)):
#     r.append(l[i]**2)
# print(r)

# 3- Given a tuple of numbers, return the sum of all the even numbers in the tuple.
# t=(10,20,30,33,2,3,1,4,24)
# sum=0
# for i in range(len(t)):
#     if(t[i]%2==0):
#         sum+=t[i]
# print(sum)
# output:90

# 4- Create a program that checks if a given tuple is sorted in ascending order.
# t=(1,2,3,4,5)
# t2=(1,2,3,10,4,5)
# print(t==tuple(sorted(t)))
# print(t2==tuple(sorted(t2)))
# output:
# True
# False

# 5- Write a program that removes all duplicate elements from a given list and returns the result as a set.
# l=[10,20,30,1,2,3,10,20,3,8]
# s=set()

# for i in range(len(l)):
#     if l[i] not in s:
#         s.add(l[i])
# print(s)
# output:
# {1, 2, 3, 8, 10, 20, 30}

# 6- Given two sets, find and return the intersection of both sets.
# s={1,2,3,6,7,8}
# s2={1,2,3,4,10,8}
# s3=set()
# for i in s:
#     if i in s2:
#         s3.add(i)
# print(s3)
# output:{8, 1, 2, 3}

# 7- Given a dictionary, return a list of all the values in the dictionary.
# d={1:20,2:30,3:67,4:89}
# print(list(d.values()))
# output:
# [20, 30, 67, 89]

# 8- Given a dictionary of student names and their grades, find the student with the highest grade.
# d={'a':20,'b':89,'c':90,'d':45}
# m=max(d.values())
# for i,v in d.items():
#     if v==m:
#         print(i,v)
#         break;

# output:c 90

# # 9- Write a program that takes a number as input and checks if it is divisible by both 2 and 5.
# n=100
# if n%2==0 and n%5==0:
#     print(True)
# else:
#     print(False)
# output:True

# 10- Given a number, print whether it is positive, negative, or zero using conditional statements.
# a= int(input("enter number"))
# if a>0:
#     print(f"{a} is positive")
# elif a<0:
#     print(f'{a} is negative')
# else:
#     print(f"{a} is zero")
# output:
# enter number20
# 20 is positive
# enter number-2
# -2 is negative
# enter number0
# 0 is zero

# 11- Write a program that checks if a given number is divisible by 3 or 5. If it is divisible by both, print "Divisible by both".
# n=15
# if n%3==0 and n%5==0:
#     print("Divisible by both")
# else:
#     print("not Divisible by both")
# output:Divisible by both

# 12- Given a number, check if it is a multiple of 3 and also check if it is greater than 10 using nested conditionals.
# n=30
# if(n%3==0)and n>10:
#     print("True")

# 13- Write a program that prints the Fibonacci sequence up to the nth number using a while loop.
# a=0
# b=1
# print(0)
# print(1)
# for i in range(1,8):
#     c=a+b
#     print(c)
#     a=b
#     b=i
# output:0
# 1
# 1
# 2
# 3
# 5
# 7
# 9
# 11



# 14- Write a program that takes an integer n and prints all numbers from 1 to n that are divisible by 3 using a while loop.
# n=40
# i=3
# while(i<=n):
#     if(i%3==0):
#         print(i,end=' ')
#     i+=1
# output:3 6 9 12 15 18 21 24 27 30 33 36 39 


# # 15- Given a list of numbers, use a for loop to find the sum of all numbers in the list.
# l=[10,20,30,12,3,410,90]
# sum=0
# for i in l:
#     sum+=i
# print(sum)
# output:575

# 16- Write a program that prints the first n even numbers using a for loop.
# n=10
# for i in range(1,n):
#     if(i%2==0):
#         print(i)

# output:2
# 4
# 6
# 8

# 17- Write a program that prints the squares of numbers between 1 and 10 using the range() function in a loop.
# for i in range(1,10):
#     print(i**2,end=" ")
# output:1 4 9 16 25 36 49 64 81 

# 18- Write a program that counts how many numbers between 100 and 500 are divisible by both 4 and 6 using range().
c=0
# for i in range(100,500):
#     if(i%4==0 and i%6==0):
#         c+=1
# print(c)
# output:33

# 19- Given a list of numbers, check if there is any number that appears more than once using conditionals, loops, and sets. 
# l=[0,20,1,1,1,2,3,3,4,4,5,5,89,10,30,30,49,80]
# s=set()
# for i in l:
#     if l.count(i)>=2:
#         s.add(i)
# print(s)

# output:{1, 3, 4, 5, 30}

# 20- Using the range() function, 
# write a program that prints all numbers between 10 and 50 that are divisible by 7.
# for i in range(10,50):
#     if i%7==0:
#         print(i)
# output:14
# 21
# 28
# 35
# 42
# 49