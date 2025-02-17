# 1. WAP to add multiple number, ask user to take input as their need, press 0 to terminate inputting after that calculate sum of that inputted number
# n=int(input("Enter number if want to exit pres 0 "))
# sum=0
# while(n!=0):
#     sum+=n
#     n=int(input("enter number  "))
# print("Sum:",sum)


# 2. Write a function to find the sum of all prime numbers below a given integer n. Implement this using a for loop, checking for primality within each iteration.
# n=int(input("enter a no "))
# sum=0
# for i in range(2,n):
#     p=1
#     for j in range(2,i):
#         if i%j==0:
#             p=0
#             break
#     if p==1:
#         sum+=i
# print("Sum:",sum)


# 3. Implement a program to print all possible combinations of characters from two strings. Use a nested for loop to generate each combination.
# s1=input("enter a  string1 ")
# s2=input("enter string 2 ")
# for i in s1:
#     for j in s2:
#         print(i+j,end=" ")


# 4. Given a list of strings, write a function to find the most common character across all strings using iterative loops.
# l="".join(list(map(str,input("enter elements ").split(" "))))
# print(l)
# d={i:l.count(i) for i in l}
# max=0
# chr=''
# for k,v in d.items():
#     if v>max:
#         chr=k
#         max=v

# print("Most Common Charecter is",chr,max)



# 5. Write a python program to multiply all numbers in the list.
# l=list(map(int,input("enter elements ").split(" ")))
# mul=1
# for i in l:
#     mul*=i
# print("Multiplication",mul)


# 6. Implement a program to merge two sorted lists without using built-in functions. Use loops to traverse and compare elements from both lists.
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3=[]
# for i in list1:
#     list3.append(i)
# for j in list2:
#     list3.append(j)
# print(list3)


# 7. Given a list of integers, write a program to find all pairs of numbers that add up to a target sum. Implement this with a nested for loop.
# l=list(map(int,input("enter elements ").split(" ")))
# sum=int(input("enter target sum "))

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==sum:
#             print((l[i],l[j]),end=" ")
    

# 8. WAP to take input first and last no and display all even numbers between them and find sum and count.
# start=int(input("enter start index "))
# end=int(input("enter end index "))
# sum=0
# count=0
# for i in range(start,end):
#     if i%2==0:
#         sum+=i
#         count+=1
#         print(i,end=" ")
# print("Sum:",sum)
# print("Count:",count)


# 9. Given a number n, implement a for loop to find all divisors of n. Return them in a sorted list.
# n=int(input("enter no "))
# l=[]
# for i in range(1,n):
#     if n%i==0:
#         l.append(i)
# print(l)


# 10. Write a program that calculates the Fibonacci sequence up to the n-th term using a while loop, where n is the input.
# n=int(input("enter n "))
# n1=0
# n2=1
# print(n1,n2,end=" ")
# for i in range(n-2):
#     c=n1+n2
#     print(c,end=" ")
#     n1=n2
#     n2=c


# 11. Implement a program that prints all the prime numbers up to a given number n using a for loop.
# n=int(input("enter a no "))
# sum=0
# for i in range(2,n+1):
#     p=1
#     for j in range(2,i):
#         if i%j==0:
#             p=0
#             break
#     if p==1:
#         print(i,"Prime")


# 12. Given a string, write a program to reverse it using a while loop without using Python's built-in string reversal methods.
# s=input("Enter string ")
# i=len(s)-1
# r=''
# while(i>=0):
#     r+=s[i]
#     i-=1
# print("Reveresed string:",r)


# 13. Implement a function that checks whether a given number is a palindrome. Use a for loop to iterate over the digits of the number.
# n=(input("enter number "))
# r=''
# for i in n:
#     r=i+r
# if r==n:
#     print("palindrome")
# else:
#     print("Not Palindrome")


# 14. Write a program that prints all the prime numbers in the range [a, b], where a and b are given as inputs, using a  loop.
# a=int(input("enter a "))
# b=int(input("enter b "))
# for i in range(a,b+1):
#     p=1
#     for j in range(2,i):
#         if i%j==0:
#             p=0
#             break
#     if p==1:
#         print(i,"Prime")


# 15. Given a string of digits, write a program to check if it contains all digits from 0 to 9, using a loop to count each digit's occurrence.
# d={}
# s=input("enter string of digits")
# if s.isdigit():
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
# print(d)


# 15. WAP to print the square of each even number from inputted number.
# n=int(input("enter no "))
# while(n!=0):
#     if (n%10)%2==0:
#         print((n%10)**2)
#     n//=10


#  16. Count how many even and odd numbers are in a given list.
# l=list(map(int,input("enter elemnts ").split(" ")))
# d={'Even':0,'Odd':0}
# for i in l:
#     if i%2==0:
#         d['Even']+=1
#     else:
#         d['Odd']+=1
# print(d)


# 17. WAP to print numbers in reverse order from n to 1 using a loop.
# n=int(input("enter no "))
# for i in range(n,0,-1):
#     print(i,end=" ")


#   18.  WAP to print the cube of each odd number from the inputted number.
# n=input("enter no ")
# for i in n:
#     if int(i)%2!=0:
#         print(int(i)**3)


# 19. WAP to find the largest and smallest numbers in a list using a loop.
# l=list(map(int,input("enter elements ").split(" ")))
# min=l[0]
# max=0
# for i in l:
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
# print("Minimum",min,"Maximum:",max)


# 20.Write a program that converts an input string to match this pattern.
# Input: "python"
# Output: "pYtHoN"
# s=input("enter string ")
# r=''
# for i in range(len(s)):
#     if i%2!=0:
#         r+=s[i].upper()
#     else:
#         r+=s[i]
# print(r)

# 21
# l=list(map(int,input("enter elements ").split(" ")))
# n=int(input('enter no '))
# sum=0

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if abs(l[i]-l[j])<=n:
#             print((l[i],l[j]),end=" ")

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if abs(l[i]-l[j])<=n:
#             print((l[i],l[j]))
           
# 22.
# s=input("enter string ")
# c=0
# for i in s:
#     if i=='(':
#         c+=1
#     elif i==')':
#         c-=1
# if c!=0:
#     print("Not Balanced")
# else:
#   print("Balanced")


# Additionals
# s=input("enter string ") # a3b2c1
# d={}# {a:3,b:2,c:1}
# for i in s:# a a a b b c
#     if i in d: 
#         d[i]+=1
#     else:
#         d[i]=1 
# r=''
#{a:3,b:2,c:1}
# for i in d:
#     r+=i+str(d[i])
# print(r)

# 1
# 2 6->4
# 3 7 10->4 3
# 4 8 11 13-> 4 3 2 
# 5 9 12 14 15->4 3 2 1 


for i in range(1,7): 
    c=5
    for j in range(1,i+1):
       if j==1:
           r=i
           print(r,end=" ")
           
       else:
           r=r+c
           print(r,end=" ")
           c=c-1
        
    print()

