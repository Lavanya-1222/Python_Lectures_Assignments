# Section A: Theory (10 Questions)

# Q1. What are the benefits of using list comprehensions over traditional for loops?


# Q2. Hpw do you handle multiple exception in a single try block? Provide an example.

# Q3. What is File Handling?

# Q4. What are the advantages of using a tuple over a list

# Q5. What is difference between shallow copy and deep copy of a list. Provide example.

# Q6. What are raw strings in python, How are they useful?

# Q7. Explain the concept of Polymorphism in Python with example.

# Q8. What is the role of __init__ in python.
 

# Q9. Explain the use of Decorators in Python with example.
import time 
def my_decorator(func):
    def wrapper():
        start=time.time()
        func()
        print("Time taken for function",time.time()-start)
    return wrapper
        


@my_decorator
def fun():
    for i in range(10):
       for j in range(10):
           pass
fun()
           

# Q10. What is difference between Class method and Static Method in python?


# Section B: Correct the Code (10 Questions)

# Q1.

# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(numbers[i+1])
# ANS :List out of index 
# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(numbers[i])


# Q2. 
# count = 5
# while count >= 0:
#     print(count)
# ANS  infinite loop
# count = 5
# while count >= 0:
#     print(count)
#     count-=1


# Q3.
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
# ANS  no need to change


# Q4.
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             print(i, j)
#             break
# ANS 
#  for i in range(3):
#     for j in range(3):
#         if i == j:
#             print(i, j)
            # break


# Q5. 
# num = 15
# if num % 3 == 0:
#     print("Divisible by 3")
# elif num % 5 == 0:
#     print("Divisible by 5")
# ANS 
# num = 15
# if num % 3 == 0:
#     if num%5==0:
#         print("Divisible by both")
#     else:
#         print("Divisible by 3")
# elif num % 5 == 0:
#     print("Divisible by 5")


# Q6.
# x = 10
# if x > 5:
# print("Greater than 5")
# else:
#     print("Less than or equal to 5")
# ANS 
# x = 10
# if x > 5:
#     print("Greater than 5")
# else:
#     print("Less than or equal to 5")


# Q7.
# a, b = 5, 10
# if a > 0 and b < 5:
#     print("Condition met")
# else:
#     print("Condition not met") 
# ANS
# a, b = 5, 10
# if a > 0 and b > 5:
#     print("Condition met")
# else:
#     print("Condition not met") 


# Q8.
# class Parent:
#     def show(self):
#         print("Parent class")

# class Child(Parent):
#     def show(self):
#         print("Child class")
#         super.show()

# obj = Child()
# obj.show()
# ANS 
# class Parent:
#     def show(self):
#         print("Parent class")

# class Child(Parent):
#     def show(self):
#         print("Child class")
#         # super.show()

# obj = Child()
# obj.show()


# Q9.
# class Car:
#     def __init__(self, brand):
#         brand = brand

# c1 = Car("Toyota")
# print(c1.brand)
# ANS 
# class Car:
#     def __init__(self, brand):
#         self.brand = brand

# c1 = Car("Toyota")
# print(c1.brand)



# Q10.
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, breed):
#         self.breed = breed

# dog = Dog("Labrador")
# print(dog.name)
# # ANS 
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, breed):
#         self.breed = breed
#         super().__init__(breed)

# dog = Dog("Labrador")
# print(dog.name)




# Section C: Write Code For (10 Questions) 

# Q1. Define a class person with attributes for name and age. Implement a subclass Employee that adds an attribute for salary and method to calculate the annual bonus.
#     (eg: 10% of salary)
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Employee(Person):
#     def calannualbonus(self,salary):
#         print(self.name,self.age)
#         print(f"Anual bonus: {salary*1/10}")
# e=Employee('lavanya',24)
# e.calannualbonus(1200000)


# Q2. Implement a function that generates a random password of given length, The password should include uppercase letters, lowercase letters, digits and special character.
# len=int(input("Enter length "))
# import string
# import random as rd
# def generaterandompassword(l):
#     upperchr='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lowerchr='abcdefghijklmnopqrstuvwxyz'
#     digit='1234567890'
#     specail=string.punctuation
#     allchar=upperchr+lowerchr+digit+specail
#     requred=[]
#     requred.append(rd.choice(upperchr))
#     requred.append(rd.choice(lowerchr))
#     requred.append(rd.choice(digit))
#     requred.append(rd.choice(specail))
#     pwd=[]
#     pwd.extend(requred)
#     for i in range(len-4):
#         pwd.append(rd.choice(allchar))
#     print(pwd)
#     rd.shuffle(pwd)
#     return "".join(pwd)
# print(generaterandompassword(len))
# output:
# Enter length 10
# ?u2TN.eB(D
# Enter length 8
# pJ<-f?8n


# Q3. Create a function that takes a string and returns a dictionary with the frequency count of each character.
# s=input("enter string ")
# print({i:s.count(i) for i in s})



# Q4.Write a NumPy program to test whether none of the elements of a given array are zero. 
# import numpy as np
# arr=np.array([1,2,3,10,9,7])
# f=1
# for i in np.nditer(arr):
#     if i==0:
#         f=0
#         break
# if f==1:
#     print("Test worked")
# else:
#     print("Test Failed")


# Q5. Check a number is Automorphic or not.
# n=int(input("Enter no "))#76
# sqr=n**n#5576
# temp=n
# r=0
# while(n!=0):
#         if sqr%10==n%10:
#             r=r*10+n%10
#         n//=10
#         sqr//=10

# result=0
# while(r!=0):
#       result=result*10+r%10
#       r//=10

# if result==temp:
#       print(result,temp,"Automorphic number")
# else:
#       print("Not Automorphic ")
# output:
# Enter no 76
# 76 76 Automorphic number 
# Enter no 12
# Not Automorphic      
      

# Q6.  Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).
# arr=np.array([10,0,np.inf,np.inf,12,1,np.nan])
# for i in arr:
#     if np.isfinite(i):
#         print(i,"Finite")
#     else:
#         print(i,"not finite")
# output:
# 10.0 Finite
# 0.0 Finite
# inf not finite
# inf not finite
# 12.0 Finite
# 1.0 Finite
# nan not finite


# Q7.Write a Python program to combine two dictionary by adding values for common keys 
# d1={'a':10,'b':5,'c':20}
# d2={'a':5,'d':30,'c':20}
# merged={}
# for i in d1:
#     if i in d2:
#         merged.update({i:d1[i]+d2[i]})
#         d2.pop(i)
#     else:
#         merged.update({i:d1[i]})
# for i in d2:
#     merged.update({i:d2[i]})
# print(merged)
# output:{'a': 15, 'b': 5, 'c': 40, 'd': 30}
    

# Q8. Write a NumPy program to test element-wise for complex numbers, real numbers in a given array. Also test if a given number is of a scalar type or not.
# import numpy as np
# arr=np.array([12,12+0j,23+1j,67+34j])

# for i in arr:
#     if np.iscomplex(i):
#         print(i,"Complex")
#     elif np.isreal(i):
#         print(i,"Real")
#     else:
#         print(type(i))
# output:
# (12+0j) Real
# (12+0j) Real
# (23+1j) Complex
# (67+34j) Complex
 
# Q9. Create a class "Library" that maintains a list of books. Implement a method add a book. Borrow a book and list of books are currebtly available in library.
# class Library:
#     def __init__(self):
#         self.dict={}
#     def addbook(self,name,author):
#         self.dict.update({name:author})
#     def listbook(self):
#         print(self.dict)
#     def borrowbook(self,name,author):
#         if (name in self.dict) and self.dict[name]==author:
#             self.dict.pop(name)
#             print("Borrowd Succefully")
# l=Library()
# l.addbook('DeepWork','D R VINS')
# l.addbook('Frog',"Trowe")
# l.listbook()
# l.borrowbook('Frog',"Trowe")
# l.listbook()
# Output:
# {'DeepWork': 'D R VINS', 'Frog': 'Trowe'}
# Borrowd Succefully
# {'DeepWork': 'D R VINS'}


# Q10. Write a function that takes a string and returns a new string with all duplicate characters removed.
# def dupremove(s):
#     se=[]
#     for i in s:
#         if i not in se:
#             se.append(i)
#     return "".join(se)
# print(dupremove('lavanya'))
# output: lavnya