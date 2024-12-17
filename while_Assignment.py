

# while-Assigmment.txt
# Text
# Class comments
# Your work
# Assigned
# Private comments
# Assignment details
# 1-Write a Python program to find the largest number in a list.[21,45,29,5,0,11,75,20]
# list=[21,45,29,5,0,11,75,20]
# i=0
# max=0
# while(i<len(list)):
#     if(list[i]>max):
#         max=list[i]
#     i+=1
# print(max)



# 2-Write a Python program that sum all even numbers in the list [21,45,29,5,0,11,75,20].
# list=[21,45,29,5,0,11,75,20]
# sum_even=0
# i=0
# while(i<len(list)):
#     if(list[i]%2==0):
#         sum_even+=list[i]
#     i+=1
# print(sum_even)
# output:20


# 3-Write a Python program to count how many times a specific element 11 appears in a 
# list=[21,11,29,5,0,11,11,20]
# i=0
# c_11=0
# while(i<len(list)):
#     if(list[i]==11):
#      c_11+=1
#     i+=1
# print(c_11)

# output:3

# 4-Write a Python program that reverses a list without using the reverse() method.
# l=[45,9,2,0,11,41,'a','w',3]
# i=len(l)-1
# r_l=[]
# while(i>=0):
#     r_l.append(l[i])
#     i-=1
# print(r_l)
# output:-[3, 'w', 'a', 41, 11, 0, 2, 9, 45]


# 5-Write a Python program to print new list with only the elements from the original list that are 
# divisible by 3.
# l=[21,11,27,5,3,11,12,20]
# new_l=[]
# i=0
# while(i<len(l)):
#     if(l[i]%3==0):
#       new_l.append(l[i])
#     i+=1
# print(new_l)
# output:[21, 27, 3, 12]

# 6-Write a Python program to find the factorial of a number using a while loop.
# n=4
# i=1
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print(fact)
# output:-24

# 7-Write a Python program that create a list of odd index numbers from a list.
# l=[21,13,29,17,0,12,13,20]
# odd_index_l=[]
# i=1
# while(i<len(l)):
#     odd_index_l.append(l[i])
#     i+=2
# print(odd_index_l)
# output:[13, 17, 12, 20]

# 8-Write a Python program to ask the user to input numbers until they enter 0, and then sum all 
# entered numbers using a while loop.
# sum=0
# n=int(input("Enter No"))
# while(n):
#     n=int(input("Enter No"))
#     sum+=n
# print(sum)
# output:
# Enter No1
# Enter No2
# Enter No3
# Enter No4
# Enter No10
# Enter No0
# 19


# 9-Write a Python program that removes all the even numbers from a list.
# l=[21,10,29,18,0,12,11,20]
# i=0
# while(i<len(l)):
#     if(l[i]%2==0):
#         l.remove(l[i])
#     i+=1
# print(l)
# output:[21, 29, 0, 11]

# 10-Write a Python program that prints a countdown from 10 to 1 using a while loop.
# i=10
# while(i>=1):
#     print(i)
#     i-=1
# output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


# 11-Write a Python program that create a list of even index numbers from a list.
# l=[21,10,29,18,0,12,11,20]
# i=0
# even_list=[]
# while(i<len(l)):
#       even_list.append(l[i])
#       i+=2
# print(even_list)
# output:[21, 29, 0, 11]

# 12-Write a Python program that checks if a given tuple contains a specific element given by user.
# l=(21,10,29,18,0,12,11,20)
# n=int(input("enter no "))
# i=0
# while(i<len(l)):
#     if(l[i]==n):
#         print("True")
#         break;
#     i+=1
# if(i==len(l)):
#     print("Not in tuple")

# output:-
# enter no 200
# Not in tuple
# enter no 12
# True


# 13-Write a Python program to covert this list into unique list 
# [1,2,3,1,2,3,1,3,2] without using inbuilt function.

# l=[1,2,3,1,2,3,1,3,2]
# unique_l=[]
# i=0
# while(i<len(l)):
#     if l[i] not in unique_l:
#        unique_l.append(l[i])
#     i+=1
# print(unique_l)

# output:-[1,2,3]

# 14-Write a Python program that prints all even numbers from 1 to 50 using a while loop.
# i=1
# while(i<=15):
#     if(i%2==0):
#         print(i,end=',')
#     i+=1
#output:  2,4,6,8,10,12,14

# 15-Write a Python program to generate a multiplication table for a number using a for loop.

# i=1
# n=int(input("enter no "))
# while(i<=10):
#     print(n,'x',i,'=',n*i)
#     i+=1

# output:enter no 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20