# Section A: Theory Questions 

# 1. What is a list in Python? Explain how it differs from a tuple.  
# 2. How does Python handle memory management in terms of garbage collection?  
# 3. Describe the difference between == and is operators in Python.  
# 4. Explain the concept of mutable and immutable objects in Python with examples.  
# 5. What is the purpose of a dictionary in Python? How is it different from a list?  
# 6. What are the basic loop structures in Python? How do for and while loops differ?  
# 7. What is the output of the following Python expression? Explain the result:
   
# print(len("Hello") + 10 - 3)
# output:12
# here len method returns the count of letters in string hence
# it returns 4 +10-3 =12

# 8. What do the terms "key" and "value" represent in a Python dictionary? 
# value: in dicionary represents any type of data like int,string,float set,list
# key:in dictionary reperesnts the unque value(string, number, or tuple with immutable elements) which can be extracted the value
 
# 9. How do you access elements from a tuple? Can you change the elements of a tuple?  
# 10. Describe what is meant by a set in Python. How does a set differ from a list?



#  Section B: Code Output / Correction Questions 

# 1. What will be the output of the following code?
   
# a = [1, 2, 3, 4]
# a[1] = 10
# print(a)
   
# ANS:[1,10,3,4]
   
# 2. The following code contains an error. Identify and correct it.
   
# nums = {1, 2, 3, 4, 5}
# nums.add([6, 7])
# print(nums)

# ANS: unhashable type:list
   

# 3. What will be the output of this code?
   
# num = 10
# while num > 0:
#     print(num)
#     num -= 2
   
# ANS:10
# 8
# 6
# 4
# 2

# 4. Correct the following code to make sure it adds the item to the dictionary:
   
student = {"name": "John", "age": 20}
student["marks"] = 80
# print(student)
# ANS: no eny correction is needed

# 5. What will be the output of this code?
   
# tuple1 = (1, 2, 3, 4)
# tuple2 = (5, 6)
# print(tuple1 + tuple2)
# output:(1,2,3,4,5,6)

# 6. The following code contains an error. Find and correct it.
   
# data = [5, 10, 15, 20]
# if 10 in data:# :colon is very important
#        print("Found")
   

# 7. What will be the output of this code?
   
# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)
# ANS:[1,2,3,4]
   

# 8. The following code is incorrect. Correct the error in the while loop.
   
# num = 0
# while num < 5:
#        print("Python")
# ANS: infinite loop
   

# 9. What will be the output of the following code?
   
# x = 5
# if x < 10:
#        print("Smaller")
# else:
#        print("Larger")
# output:Smaller
   

# 10. The following code throws an error. Identify and correct it.
   
#    nums = {1, 2, 3}
#    nums.remove(4)
#    print(nums)
   



#  Section C: Program Writing 

# Write Python programs for the following topics:

# 1. List: Write a Python program that takes a list of numbers from the user and calculates the sum of all even numbers in the list.
# l=list(map(int,input("Enter numbers").split(" ")))
# print(l)

# output:[10, 20, 30, 4, 50, 60]

# 2. Set: Write a Python program that takes two sets and returns their union, intersection, and difference.
s1={1,2,3,5,8,9,10,11,4}
s2={10,20,30,3,5,8}
print(s1.intersection(s2))
# output:{8, 10, 3, 5}
print(s1.union(s2))
# output:{1, 2, 3, 4, 5, 8, 9, 10, 11, 20, 30}
print(s1.difference(s2))
# output:{1, 2, 4, 9, 11}

# 3. Tuple: Write a Python program to find the index of the first occurrence of an element in a tuple.
# t=(345,1,2,3,4,90,2,1,34,1)
# print(t.index(1))
# output:1

# 4. Dictionary: Write a Python program that creates a dictionary with keys as names of students and values as their scores, and then prints the student with the highest score.
# d={'abhi':20,'boob':89,'cipra':90,'dipa':45}
# m=max(d.values())
# for i,v in d.items():
#     if v==m:
#         print(i,v)
#         break;

# output:cipra 90

# 5. Conditionals: Write a Python program that takes a number as input and checks whether it is positive, negative, or zero.
# a= int(input("enter number"))
# if a>0:
#     print(f"{a} is positive")
# elif a<0:
#     print(f'{a} is negative')
# else:
#     print(f"{a} is zero")
# output: 0 is Zero

# 6. Loops: Write a Python program that prints all numbers from 1 to 20, but for multiples of 3 print "Fizz" and for multiples of 5 print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".

# for i in range(1,20):
#     if(i%3==0):
#         print('Fizz')
#     elif(i%5==0):
#         print("Buzz")
#     elif(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     else:
#         print(i)

# output:1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz
# 16
# 17
# Fizz
# 19

# 7. List: Write a Python program that reverses a list 
# without using the reverse() method.
# l=[10,20,30,40,50,1,2,3]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

# output:[3, 2, 1, 50, 40, 30, 20, 10]

# 8. Set: Write a Python program that removes duplicates from a list 
# by converting it to a set and then back to a list.
# l=[1,2,3,1,2,3,4,5,67,10,20,67,89]
# l=set(l)
# l=list(l)
# print(type(l),l)
# output:<class 'list'> [1, 2, 3, 4, 5, 67, 10, 20, 89]

# 9. Tuple: Write a Python program to convert a tuple into a list 
# and a list into a tuple.
# t=(10,20,30,40,506)
# l1=list(t)
# print(type(l1),l1)
# list1=[10,20,30,40]
# t1=tuple(list1)
# print(type(t1),t1)

# output:<class 'list'> [10, 20, 30, 40, 506]
# <class 'tuple'> (10, 20, 30, 40)

# 10. Numeric: Write a Python program that calculates the factorial of a number using a for loop.
# n=int(input("enter no "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# output:enter no 5
# 120