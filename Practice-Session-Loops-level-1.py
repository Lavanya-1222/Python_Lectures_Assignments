# 1. Print numbers from 1 to 10 using a while loop.  
# i=1
# while(i<=10):
#     print(i,end=" ")
#     i+=1

# 2. Print all even numbers between 1 and 20 using a while loop.  
# i=1
# while(i<=20):
#     print(i,end=" ")
#     i+=1


# 3. Find the sum of numbers from 1 to 50 using a while loop. 
# i=1
# sum=0
# while(i<=50):
#     sum+=i
#     i+=1
# print("Sum:",sum)


# 4. Print the multiplication table of 5 using a while loop. 
# i=1
# while(i<=10):
#     print(f'5 X {i} = {5*i}')
#     i+=1


# 5. Reverse a given string using a while loop.  
# s=input("enter string ")
# i=0
# r=''
# while(i<len(s)):
#     r=s[i]+r
#     i+=1
# print(r)


# 6. Print the first 10 natural numbers using a for loop and range().  
# for i in range(1,11):
#     print(i,end=" ")


# 7. Print all odd numbers from 1 to 15 using a for loop and range(). 
# for i in range(1,16):
#     if i%2!=0:
#      print(i,end=" ")
 

# 8. Calculate the factorial of a number using a for loop and range().
# n=int(input("enter a no "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# 9. Print the square of numbers from 1 to 10 using a for loop and range(). 
# for i in range(1,11):
#     print(i**2,end=" ")


# 10. Generate a list of the first 10 multiples of 3 using a for loop and range().
# for i in range(1,11):
#     print(3*i)


# 11. Iterate over a list of names and print each name using a for loop.  
# names=list(map(str,input("enter names in list ").split(" ")))
# for i in names:
#     print(i)


# 12. Find the sum of all elements in a list using a for loop. 
# sum=0
# nums=list(map(int,input("Enter elements in list ").split(" ")))
# for i in nums:
#     sum+=i
# print("Sum",sum)


# 13. Print only the vowels from a given string using a for loop. 
# s=input("Enter string ")
# for i in s:
#     if i in 'aiouAIOUEe':
#       print(i,end=" ")


# 14. Count the occurrences of a specific character in a string using a for loop.
# s=input("enter string ")
# chr=input("enter chrecter ")
# for i in s:
#     if i==chr:
#         print(i,s.count(i))
#         break

# 15. Print all keys of a dictionary using a for loop.  
# d={'A':10,'G':90,'f':100}
# for i in d:
#     print(i)


# 16. Print all values of a dictionary using a for loop.  
# d={'A':10,'G':90,'f':100}
# for i in d:
#     print(d[i])

# 17. Iterate over a list of tuples and print each tuple's elements using a for loop.  
# n=int(input("enter a no.of tuples in list "))
# l=[]
# for i in range(n):
#     a=tuple(map(int,input("Enter elements in tuple ").split(" ")))
#     l.append(a)
# print(l)
# for i in l:
#     for j in i:
#         print(j,end=" ")
#     print()

# 18. Iterate over a list of numbers and print "even" for even numbers and "odd" for odd numbers.  
# l=list(map(int,input("Enter elements in list ").split(" ")))
# for i in l:
#     if i%2==0:
#         print(i,"Even")
#     else:
#         print(i,"Odd")

# 19. Print the reverse of a given list using a for loop.
# l=list(map(int,input("Enter elements in list ").split(" ")))
# r=[]
# for i in range(len(l)-1,-1,-1):
#     print(l[i])


# 20. Check if a given word is a palindrome using a for loop.
# word=input("enter a word ")
# rev=''
# for i in range(len(word)-1,-1,-1):
#     rev+=word[i]
# print(rev)
# if rev==word:
#     print("Palindrom")
# else:
#     print("Not Palindrom")



# s=input("enter string ")
# r=""
# for i in s:
#    r=i+r
# if r==s:
#    print("Palindrome")
# else:
#    print("Not Palindrom")


# Additional:    
# Print numbers from 10 to 1 in reverse order using a while loop.
# i=10
# while(i>=1):
#     print(i,end=" ")
#     i-=1

# Print all multiples of 4 from 1 to 40 using a while loop.
# i=1
# while(i<=40):
#     print(4*i,end=" ")
#     i+=1


# Find the product of numbers from 1 to 10 using a while loop.
# pro=1
# i=1
# while(i<=10):
#     pro*=i
#     i+=1
# print("Product",pro)

# Print the Fibonacci series up to 10 terms using a while loop.
# n1=0
# n2=1
# print(n1,n2,end=" ")
# i=1
# while(i<=8):
#     c=n1+n2
#     print(c,end=" ")
#     n1=n2
#     n2=c
#     i+=1
    
# Print a given string in reverse order using a for loop.
# s=input("enter string ")
# r=""
# for i in s:
#     r=i+r
# print(r)


# Print numbers from 1 to 20, skipping multiples of 3, using a for loop.
# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)


# Count the number of words in a given sentence using a for loop.
# s=input("Enter string ")
# c=0
# for i in s:
#     if i==" ":
#         c+=1
# print("Count",c+1)


# Check if a given number is prime using a for loop.
# p=1
# n=int(input("enter no "))
# for i in range(2,n):
#     if n%i==0:
#         p=0
# if p==0:
#     print(n,"Not Prime")
# else:
#     print(n,'prime')


# Find the largest number in a list using a for loop.
# l=list(map(int,input("enter elements in list ").split(" ")))
# max=0
# for i in l:
#     if i>max:
#         max=i
# print("largest element",max)