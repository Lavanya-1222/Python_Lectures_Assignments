#1 Write a program that takes a list of integers as input and returns a dictionary with keys as the integers and values as their squares.
# l=list(map(int,input("Enter Elements ").split(" ")))
# d={i:i**2 for i in l}
# print(d)
# output:
# Enter Elements 1 2 3 4
# {1: 1, 2: 4, 3: 9, 4: 16}


#2 Use f-strings to display a personalized greeting message using variables for the name and age of a user.
# def greeting (name,age):
#     print(f"Welcomt {name} your {age} old.")
# greeting('lavanya',24)
# output:
# Welcomt lavanya your 24 old.


#3 Write a program to check if a string is a palindrome using slicing and conditional statements.
# s=input("Enter String ")
# if s==s[::-1]:
#     print("Palindrom")
# else:
#     print("Not Palindrom")
# output:
# Enter String moom
# Palindrom


#4 Create a function that accepts a list of tuples (name, score) and returns the names of students who scored above 75.
# l=[('sam',20),('lavanya',40),('priya',76),('ajay',90)]
# for i in l:
#     if i[1]>75:
#         print(i[0]) 
# output:
# priya
# ajay


#5 Generate a multiplication table (1-10) for a number using nested loops.
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"X",j,i*j)
#     print()


#6 Implement a function that calculates the sum of all even numbers in a list using a list comprehension.
# l=sum([i for i in [10,20,30,40,11,13] if i%2==0])
# print(l)
# output:
# 100


#7 Write a program to remove duplicates from a list and display the result as a set.
# l=[1,2,3,1,2,3,4,5]
# l=set(l)
# print(l)
# output:
# {1, 2, 3, 4, 5}


#8 Using enumerate, iterate over a list of fruits and print the index and the fruit name in an f-string format.
# fruits=['apple','Mango','banana']
# for v,i in enumerate(fruits):
#     print(f'{v} {i}')
# output:
# 0 apple
# 1 Mango
# 2 banana


#9 Create a program to count the frequency of each character in a string and store it in a dictionary.
# s=input("Enter String ")
# d={i:s.count(i) for i in s}
# print(d)
# output:
# Enter String lavanya
# {'l': 1, 'a': 3, 'v': 1, 'n': 1, 'y': 1}


#10 Write a program that checks if a number is prime using a user-defined function.
# n=int(input("Enter no "))
# p=0
# for i in range(2,n):
#     if n%i==0:
#         p=1
# if p==1:
#     print(n,"Not prime")
# else:
#     print(n,"Prime")
# output:
# Enter no 11
# 11 Prime


#11 Write a recursive function to calculate the factorial of a number, and then use it in a program to find the sum of factorials of numbers in a list.
# def fact(n):
#     if n==1 or 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))
# for i in [5,6,7,8,9,10]:
#     print(i,fact(i))
# output:
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880
# 10 3628800


#12 Using comprehensions, create a dictionary where keys are numbers from 1 to 10, and values are their cubes only if the number is odd.
# print({i:i**3 for i in range(1,11) if i%2!=0})
# output:
# {1: 1, 3: 27, 5: 125, 7: 343, 9: 729}



#13 Implement a higher-order function that takes a list of numbers and a lambda function, then applies the lambda to filter out non-prime numbers.



#14 Create a function that returns a nested dictionary representing the Fibonacci series up to n levels. The keys should be the position, and the values should be the Fibonacci numbers.
# 0 1  1 2 3 5 8 11
# d={0:{}}
# n=int(input("Enter no "))
# for i in range(1,n+1):
#     t={}
#     if i==2:
#         t.update({2:[0,1]})
#         d.update({i:t})

#     elif i==1:
#         t.update({1:[0]})
#         d.update({i:t})
#     elif i>2:
#          tl=[0,1]
#          n1=0
#          n2=1
         
#          for j in range(i-2):
#           c=n1+n2
#           tl.append(c)
#           n1=n2
#           n2=c
#          t.update({i:tl})
#          d.update({i:t})
# print(d)
# output:
# {0: {}, 1: {1: [0]}, 2: {2: [0, 1]}, 3: {3: [0, 1, 1]}, 4: {4: [0, 1, 1, 2]}, 5: {5: [0, 1, 1, 2, 3]}, 6: {6: [0, 1, 1, 2, 3, 5]}, 7: {7: [0, 1, 1, 2, 3, 5, 8]}, 8: {8: [0, 1, 1, 2, 3, 5, 8, 13]}}

        
#15 Write a program to sort a list of tuples (name, age) by age using the sorted function and a lambda.
# l=[('lava',24),('samarth',26),('saranya',1),('arya',2)]
# print(sorted(l,key=lambda x:x[1]))
# output:
# # [('saranya', 1), ('arya', 2), ('lava', 24), ('samarth', 26)]


# #16 Implement a program that reads a string, reverses it, and counts the frequency of vowels and consonants using comprehensions and sets.
s=input("Enter string ")
s=s[::-1]
v='AIOUEaioue'
cc=0
vc=0

l=['vc' if i in v else 'cc' for i in s]
print(l)
for i in l:
    if i=='vc':
        vc+=1
    else:
        cc+=1
print('vowel-count:',vc,'Constant-count',cc)




# #17 Create a recursive function to generate all subsets of a given set, represented as a list.


#18 Write a function using recursion and nested conditionals to solve the Tower of Hanoi problem and display all moves.

#19 Using f-strings and enumerate, generate a report card displaying a student's marks in each subject, the total, and the average.


#20 Implement a program that merges two dictionaries into one, resolving key conflicts by keeping the higher value using a loop and conditionals.
# d1={'a':10,'b':30}
# d2={'b':30,'f':5}
# d3={}

# for k,v in d1.items():
#     if k in d2.keys():

#         if v>d2[k]:
#             d3.update({k:v})
#             d2.pop(k)
#         else:
#             d3.update({k:d2[k]})
#             d2.pop(k)
#     else:
#             d3.update({k:v})
           
# for k,v in d2.items():
#     d3.update({k:v})
# print(d3)
# output:
# {'a': 10, 'b': 30, 'f': 5}  
# {'a': 10, 'b': 40, 'f': 5} after changing b in d1 to 40  
    

#21 Create a nested comprehension to generate a multiplication table (1-10) stored in a dictionary of lists, where each key is the multiplier.
# d={1:[1,2,3,4,5,6,]}
# d={i:[i*j for j in range(1,11)] for i in range(1,11)}
# print(d)
# {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 4: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], 5: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], 6: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], 7: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], 8: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80], 9: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90], 10: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}



#22 Write a program that finds all Armstrong numbers in a range using a lambda and a higher-order function.



#23 Implement a program to generate Pascal’s Triangle up to n levels using recursion and nested lists.

#24 Write a function to solve a Sudoku puzzle using recursion and backtracking.

#25 Create a program that takes a dictionary of items with prices and calculates the total cost, including a discount based on user-defined conditions.
d={'mixer':200,'t-shirt':300}
#26 Write a program that implements a nested loop and recursion to generate and print all magic squares of a given size n.

#27 Develop a recursive function that solves the N-Queens problem and prints all possible solutions as a list of tuples (row, column).

#28 Write a program to compress and decompress a string using run-length encoding and recursion.

#29 Implement a Python script that evaluates a mathematical expression given as a string (e.g., 3 + 5 * (2 - 1)) using recursion and the operator module.

#30 Build a mini calculator for sets (union, intersection, difference) that takes input as strings, parses the operations, and uses higher-order functions to execute the operations dynamically.
