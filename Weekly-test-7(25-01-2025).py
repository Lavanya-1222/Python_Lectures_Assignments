# Section A: Theory (10 Questions)

# 1. Explain difference between discard() and remove()?
# 2. How can you update dictionary in python, Explain the method with example.
# 3. How can you perform set operations like union, intersection and difference in python, provide the example.
# 4. Describe the difference between the map(), filter(), and reduce() functions in Python with examples.
# 5. What is the purpose of a constructor in Python classes? Provide an example of a class with a constructor that initializes a student’s name and age.  
# 6. What is the filter() function in Python? Provide an example where you filter even numbers from a list using filter().
# 7. Explain the concept of encapsulation in OOP with an example.  
# 8. How does polymorphism improve code reusability in OOP?  
# 9. What is multiple inheritance in Python? How does it work? Provide an example.
# 10. What is the purpose of the with statement when handling files in Python?


# Section B: Correct the Code (10 Questions)

# 1. The following code contains an error. Identify and correct it:
   
# def my_func(x, y):
#        return x + y
# result = my_func(5)
# print(result)
# ANS 
def my_func(x, y):
       return x + y
result = my_func(5,10)
print(result)

# 2. What will be the output of this code?
   
x = 10
for i in range(x):
       if i % 2 == 0:
           continue
       print(i)
# ANS 
# 1 3 5 7 9 


# 3. What will be the output of the following code?
def greet(name="User"):
       print("Hello, " + name)
greet("John")
greet()
# ANS 
# Hello, John
# Hello, User


# 4. What will be the output of this code?
a = (1, 2, 3)
b = list(a)
b.append(4)
print(a)
# ANS (1,2,3)


# 5. Code:  
# def greet(name):
#        print("Hello" + name)
# greet()
# ANS 
# def greet(name):
#        print("Hello" + name)
# greet('lavanya')
# output: Hellolavanya 
#    Error: Pass the required parameter to the function. 

# 6. Correct the code to calculate the sum of numbers using reduce():
#    from functools import reduce
#    numbers = [1, 2, 3, 4]
#    result = reduce(lambda x, y: x + y, numbers)
#    print(result) 
# ANS 
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x,y: x + y, numbers)
print(result) 


# no Error 
# 7. Code:  
   
#    class Animal:
#        def __init__(name):
#            self.name = name   
#    Error: Correct the constructor's parameter list.
# ANS 
class Animal:
       def __init__(self,name):
           self.name = name 

# 8. The following code has an error. Correct it and explain the output:
#    def multiply(x, y):
#        return x * y
#    result = multiply(2, 3, 4)
#    print(result)
# ANS 
def multiply(x, y):
       return x * y
result = multiply(2, 3)
print(result)


# 10. Code:  

#     class Car:
#         def __init__(self, make, model):
#             make = make
#             model = model
#  Error: Fix the instance variable assignment issue.  
# ANS 
class Car:
        def __init__(self, make, model):
            self.make = make
            self.model = model
c=Car('o','iio')
print(c.make)
        

# Section C: Write Code For (10 Questions)
# 1. Write a Python program to create a dictionary that stores student names as keys and their scores as values. Write a function that returns the name of the student with the highest score.
d={'A':90,'B':89,'C':56,'D':40}
m=max(d.values())
for k,v in d.items():
      if v==m:
            print("winner",k)
            break 

# 2. Write a Python program to sum all the numbers in a list. The program should use a loop to calculate the sum of the numbers in the list.
l=[10,20,30,4,5,6]
sum=0
for i in l:
      sum+=i
print("Sum:",sum)


# 3. Write a program that finds the factorial of a number using both a while loop and a for loop.
n=int(input("Enter no "))
fact=1
for i in range(1,n+1):
      fact*=i
print("Fact using for ",fact)
i=1
fact=1
while(i<=n):
      fact*=i
      i+=1

print("Fact using While",fact)
# output:
# Enter no 5
# Fact using for  120
# Fact using While 120


# 4. Write a function that uses map() to return a new list where each string in a list is reversed.
l=['abc','efgh','ijkl','mnop']
print(list(map(lambda x: x[::-1],l)))
# output:['cba', 'hgfe', 'lkji', 'ponm']


# 5. Create a class Person with a constructor that accepts name and age. Add a method to check if the person is eligible to vote.
class Person:
      def __init__(self,name,age):
            self.name=name
            self.age=age 
      def Eligible_check(self):
            if self.age>=18:
                  print(self.name,"Is eligible for Vote")
            else:
                  print(self.name,"not eligible for vote ")
# p=Person('lavanya',24)
# p1=Person('samarth',17)
# p.Eligible_check()
# p1.Eligible_check()
# output:
# lavanya Is eligible for Vote
# samarth not eligible for vote


# 6. Write a Python program that defines a class Car. The class should have a constructor that initializes the car's make, model, and year. Then, create an instance of the class and print the car's details.
class Car:
      def __init__(self,make,model,year):
            self.make=make
            self.model=model
            self.year=year
      def details(self):
            print("Make:",self.make,"Model:",self.model,"Year:",self.year)
c=Car('TaTa','Toyoto',2009)
# c.details()
# output:Make: TaTa Model: Toyoto Year: 2009 


# 7. Write a function 'sort_students_by_grade()' in the 'student_data.py' module that sorts the list of students by their grades in descending order. Print the sorted list of students.
import student_data
list=[10,40,89,90,9,8,78,76,30,20,1]
result=student_data.sort_students_by_grade(list)
print("Result:",result)
# output:
# Result: [90, 89, 78, 76, 40, 30, 20, 10, 9, 8, 1]


# 8. Nested Loops: Write a Python program using nested loops to print the following pattern:
   
#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A  

# 9. Write a Python program to demonstrate operator overloading in OOP. 
class Vector:
    def __init__(self,a):
        self.a=a 
        print(self.a)
    def __add__(self,another):
        return self.a+another.a
# v1=Vector(10)
# v2=Vector(20)
# print("Sum:",v1+v2)
# output:Sum: 30


# 10. Define a class BankAccount with the attributes balance (public), account_number (private), and account_type (protected). Provide a method deposit() that adds to the balance, and a method get_balance() to access the balance. Demonstrate usage by creating an instance of BankAccount and performing deposits and balance retrieval.
class BankAccount:
      def __init__(self,balance,acc_num,acc_type):
            self.balance=balance
            self.__account_number=acc_num 
            self._account_type=acc_type
            print(self.__account_number,self._account_type)
      def deposit(self,bal):
        
            self.balance+=bal 
      def get_balance(self):
            print("Your Balance:",self.balance)
b=BankAccount(1000,39388090,'Saving account')
b.deposit(100000)
b.get_balance()
# output:
# 39388090 Saving account
# Your Balance: 101000

d={1:10,2:20}
d.update({(3,90)})
print(d)
d.update({4:400})
print(d)
