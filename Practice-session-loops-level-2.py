# Level 2
# 1. Write a program that prints all the prime numbers from 1 to 100 using a for loop.
# for i in range(1,101):
#     p=1
#     for j in range(2,i):
#         if i%j==0:
#             p=0

#     if p==1:
#         print(i,end=" ")


# 2. Create a program that prints the sum of all even numbers from 1 to n using a for loop.
# n=int(input("Enter no "))
# sum_even=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even+=i
# print(sum_even)
    

# 3. Write a program using a while loop to calculate the factorial of a number.
# n=int(input("enter no "))
# i=1
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print("Factorial of ",n,"is",fact)


# 4. Implement a program that prints a sequence of numbers where each number is the sum of the two previous numbers, starting with 0 and 1, using a while loop.
# n1=0
# n2=1
# n=int(input("Enter no "))
# i=1
# while(i<=n-2):
#     c=n1+n2
#     print("Sum=",c)
#     n1=n2
#     n2=c
#     i+=1


# 5. Write a program that counts the number of digits in a given number using a while loop.
# n=int(input("Enter no "))
# c=0
# while(n!=0):
#     c+=1
#     n=n//10
# print("Count",c)

   
# 6. Create a program that prints the first n Fibonacci numbers using a for loop.
# n=int(input("Enter a no "))
# n1=0
# n2=1
# print(n1,n2,end=" ")
# for i in range(n-2):
#     c=n1+n2
#     print(c,end=" ")
#     n1=n2
#     n2=c


# 7. Implement a program that checks if a number is a palindrome using a while loop.
# n=int(input("enter no "))
# n1=n
# r=0
# while(n!=0):
#     d=n%10
#     r=d+r*10
#     n=n//10
# if r==n1:
#     print(n1,"Is palindrome")
# else:
#     print(n1,"not Palindrome")


# 8. Write a program that computes the sum of all odd numbers from 1 to n using a for loop.
# n=int(input("enter no "))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#       sum+=i
# print("Sum:",sum)


# 9. Implement a program that prints every third number between 1 and 50 using a while loop.
# i=1
# while(i<=50):
#   print(i,end=" ")
#   i+=2


# 10. Write a program that prints the multiplication table of a number up to n using a for loop.
# n=int(input("enter a no "))
# for i in range(1,n+1):
#     for j in range(1,11):
#         print(f'{i} X {j} = {i*j}')


# 11. Create a program that prints the first n multiples of 5 using a for loop.
# n=int(input("enter no "))
# for i in range(1,n+1):
#     print(5*i,end=" ")


# 12. Write a program that calculates the sum of digits of a given number using a while loop.
# n=int(input("enter no "))
# sum=0
# while(n!=0):
#     sum+=n%10
#     n//=10
# print("Sum-of-Digits",n,"=",sum)


# 13. Create a program that finds the sum of all numbers in a list that are divisible by 2 using a for loop.
# l=list(map(int,input("enter elements ").split(" ")))
# sum=0
# for i in l:
#     if i%2==0:
#         sum+=i
# print("sum:",sum)


# 14. Implement a program that removes all negative numbers from a list using a for loop.
# l=list(map(int,input("enter elements ").split(" ")))
# r=l
# for i in l:
#     if i<0:
#         r.remove(i)
# print(r)
# print(l)


# 15. Write a program that prints all numbers divisible by both 3 and 5 between 1 and n using a while loop.
# n=int(input("enter no "))
# i=1
# while(i<=n):
#     if i%3==0 and i%5==0:
#         print(i,end=" ")
#     i+=1


# 16. Create a program that prints the reverse of a given string using a while loop.
# s=input("enter s string ").split(" ")
# i=len(s)-1
# r=[]
# while(i>=0):
#     r.append(s[i])
#     i-=1
# print(" ".join(r))


# 17. Write a program that finds the largest number in a list using a for loop.
# l=list(map(int,input("enter element ").split(" ")))
# max=0
# for i in l:
#     if i>max:
#         max=i
# print("Largest is",max)


# 18. Implement a program that generates the squares of numbers from 1 to n using a for loop.
# n=int(input("enter no "))
# for i in range(1,n+1):
#     print(i**2,end=" ")

# 19. Write a program that prints a pattern of numbers in the following format using a for loop:
    
#     1
#     2
#     3
#     4
# for i in range(1,5):
#     print('\t',i)

    

# 20. Write a program that counts the number of vowels in a given string using a while loop.
# s=input("Enter string ")
# i=0
# c=0
# while(i<len(s)):
#     if s[i] in 'aioueAOIUE':
#         c+=1
#     i+=1
# print("count",c)



# Write a program to find the smallest number in a list using a for loop.
# l=list(map(int,input("enter elements ").split(" ")))
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print("Smallestnumber is",min)


# Print numbers from n to 1 in descending order using a while loop.
# n=int(input("enter no "))

# while(n>=1):
#     print(n,end=" ")
#     n-=1


# Print all elements of a list that are greater than a given number using a for loop.
# l=list(map(int,input("enter elements ").split(" ")))
# n=int(input("Enter a no "))
# for i in l:
#     if i>n:
#         print(i,end=" ")


# Count how many even and odd numbers are in a given list using a for loop.
# l=list(map(int,input("enter elements ").split(" ")))
# even_c=0
# odd_c=0
# for i in l:
#     if i%2==0:
#         even_c+=1
#     else:
#         odd_c+=1
# print("Even Count=",even_c)
# print("Odd_count=",odd_c)


# Count the number of vowels in a given string using a for loop.
s=input("enter s string ")
c=0
for i in s:
    if i in 'AIOUEaioue':
        c+=1
print("No.of Vowels",c)