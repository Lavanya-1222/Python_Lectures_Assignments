
# 1. A Shopkeeper's Sale  
#    A shopkeeper wants to calculate the total discount on a set of products. Each product has a price and a discount percentage. The shopkeeper uses a list to store the prices and a tuple for the discount percentages. Write a program that calculates the total discount using for loops, conditional statements, and arithmetic operations.
# price=[100,200,300,500]
# dicount=(10,10,10,50)
# total_discount=0
# for i in range(len(price)):
#     total_discount+=((dicount[i]/100)*price[i])
# print("Total_Discount: ",total_discount)
# output:
# Total_Discount:  310.0


# 2. Student Marks Calculation  
#    A teacher has stored the marks of 10 students in a dictionary where the keys are the student names, and the values are their marks. Using if-else statements, write a function to determine whether each student has passed or failed based on a cutoff mark of 50. Use a for loop to print the result.

# d={'ali':35,'samarth':90,'lava':40,'saranya':80}
# for k,v in d.items():
#     if v>=50:
#         print(k,'Passed')
#     else:
#         print(k,'Fail')
# output:
# ali Fail
# samarth Passed
# lava Fail
# saranya Passed


# 3. Password Validation  
#    An online platform wants to ensure that the passwords entered by users are strong. Write a program that checks if a password contains at least one uppercase letter, one lowercase letter, and one digit. The password should be in the form of a string. Use if-elif conditions and loops to validate it.

# s=input("Enter Password ")
# up=0
# lp=0
# dp=0
# for i in s:
#     if i.isupper():
#         up=1
#     if i.islower():
#         lp=1
#     if i in ['0','1','2','3','4','5','6','7','8','9']:
#         dp=1
# if (up==1 and lp==1 and dp==1):
#     print("Passowrd is valid")
# else:
#     print("Password is not Valid") 

# output:
# Enter Password Lava@2203
# Passowrd is valid
# Enter Password Lava
# Password is not Valid
# Enter Password lava@2203
# Password is not Valid
# Enter Password LAVA2
# Password is not Valid


# 4. Temperature Conversion  
#    A scientist is working on converting temperatures between Celsius and Fahrenheit. Write a function that takes a temperature in Celsius as input and returns the equivalent temperature in Fahrenheit. Use a lambda function to perform the conversion and test it on several inputs.
# print((lambda c:c*9/5+32)(int(input("Enter Celsius: "))))

# 5.  A mathematician needs to calculate the sum of all even and odd numbers separately up to a given number, using a for loop. The input will be a number provided by the user. Write a program that prints the sum of even numbers and the sum of odd numbers using if statements within the loop.
# n=int(input("Enter no "))
# sumodd=0
# sumeven=0
# for i in range(n+1):
#     if i%2==0:
#         sumeven+=i
#     else:
#         sumodd+=i
# print("Sum_Odd",sumodd,"Sum_Even",sumeven)
# output:
# Enter no 3
# Sum_Odd 4 Sum_Even 2


# 6.  A writer is processing a list of words and needs to check if the length of each word exceeds 5 characters. Use a list comprehension to create a new list of words that are longer than 5 characters and print that list.
# l=['i','am','longer','than','wordof','fiveays','poiutt']
# l=[i for i in l if len(i)>5]
# print(l)
# output:
# ['longer', 'wordof', 'fiveays', 'poiutt']


# 7. A developer is designing a game where the highest score of players needs to be found from a list. Write a program that takes a list of player scores and finds the highest score without using the built-in max function. You need to use a loop and if-else conditions.
# l=[10,20,30,100,20,50,600]
# highscore=0
# for i in l:
#     if i>highscore:
#         highscore=i
# print(highscore)
# output:
# 600


# 8. A mathematician wants to know if a number is prime or not. Write a program that checks whether a number, entered by the user, is prime. Use a while loop to check divisibility and a conditional statement to print the result.
# n=int(input("Enter no "))
# f=0
# i=2
# while(i<n):
#     if n%i==0:
#         f=1
#         break
#     i+=1
# print("Prime") if f==0 else print("Not Prime")
# output:
# Enter no 13
# Prime
# Enter no 2
# Prime


# 9. A teacher is designing a multiplication table for her students. Write a program that takes a list of numbers and multiplies each number by a given multiplier using a for loop. The result should be stored in a new list and printed.
# l=[1,5,6]
# new_list=[]
# for i in l:
#     m=int(input("enter multiplier "))
#     new_list.append(m*i)
# print(new_list)
# output:
# enter multiplier 1
# enter multiplier 5
# enter multiplier 6
# [1, 25, 36]



# 10. A linguist is analyzing a sentence and needs to count how many vowels it contains. Write a program that takes a string input and counts how many vowels (a, e, i, o, u) it contains using a for loop and if-else conditions.

# s=input('Enter String ')
# cv=0
# for i in s:
#     if i in 'aioueAIOUE':
#         cv+=1
# print(cv)
# output:
# Enter String lavaeno
# 4


# 11. A researcher needs to calculate the sum of squares of the first 10 numbers. Write a program using a for loop to calculate and print the sum of squares of numbers from 1 to 10. Ensure you use if statements to check that the number is positive.
# sum=0
# for i in range(1,11):
#     sum+=i**i
# print(sum)
# output:
# 10405071317


# 12. A developer is working on an app and needs to reverse a string entered by the user. Write a program using a lambda function and a list comprehension to reverse a string. Print the reversed string to the user.
# l=[i for i in (lambda s: s[::-1])(input("Enter String"))]
# print(l)
# print("".join(l))
# output:
# Enter Stringlavanya
# ['a', 'y', 'n', 'a', 'v', 'a', 'l']
# aynaval




# 13. A historian is studying the Fibonacci sequence and needs to generate it up to the nth number. Write a program that uses a for loop to generate the Fibonacci sequence up to the given number. You must also handle edge cases for inputs less than 2.
# n=int(input("enter no "))
# if n==0:
#     print(1)
# if n==1:
#     print(0,1,1)
# else:
#     n1=0
#     n2=1
#     print(0)
#     print(1)
#     for i in range(n-2):
#         c=n1+n2
#         print(c)
#         n1=n2
#         n2=c
# output:
# enter no 5
# 0
# 1
# 1
# 2
# 3  


# 14.  A stock trader has a list of daily price changes, some of which are negative. Write a program that filters out the negative numbers using list comprehension and returns a list of only positive changes.
# l=[10,-10,20,-1000,500000,20,-90,-90000000]
# l=[i for i in l if i>0]
# print(l)
# output;
# [10, 20, 500000, 20]


# 15.  A student is practicing multiplication and needs to print the multiplication table for a given number. Write a program that uses nested loops to print the multiplication table of a number from 1 to 10. Each table should be printed in a structured format.
for i in range(1,11):
    for j in range(1,11):
        print(i,'X',j,'=',i*j)
    print()