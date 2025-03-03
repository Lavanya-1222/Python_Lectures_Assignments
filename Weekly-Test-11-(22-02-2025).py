import numpy as np
# Section A: Theory (10 Questions)  

# 1. Define procedural programming. How does it differ from functional programming?  

# 2. Explain the key principles of Object-Oriented Programming (OOP).  

# 3. What are the advantages of using numpy arrays over Python lists?  

# 4. Differentiate between a 1-D array and a 2-D array in numpy.  

# 5. What is slicing in numpy arrays? Provide an example.  

# 6. Explain the concept of encapsulation in OOP with an example.  

# 7. What is the significance of immutability in functional programming?  

# 8. How does polymorphism improve code reusability in OOP?  

# 9. Describe how a 3-D numpy array is structured. Provide a use case.  

# 10. What are the primary differences between functional and procedural programming paradigms?  


# Section B: Correct the Error (10 Questions)  

# 1. Code:  
   
#    arr = np.array[1, 2, 3]
     
#    Error: Correct the array creation method.  

# 2. Code:  
   
#    def my_func(a, b):
#    return a + b
     
#    Error: Fix the indentation issue.  

# 3. Code:  
   
#    class Animal:
#        def __init__(name):
#            self.name = name
     
#    Error: Correct the constructor's parameter list.  

# 4. Code:  
   
#    arr = np.array([1, 2, 3])
#    print(arr[3])
     
#    Error: Handle the index out of bounds error.  

# 5. Code:  
   
#    arr = np.array([[1, 2], [3, 4]])
#    slice = arr[1, :]
     
#    Error: Correct the slicing syntax.  

# 6. Code:  
   
#    def square(n)
#        return n * n
     
#    Error: Add the missing syntax.  

# 7. Code:  
   
#    obj = MyClass()
#    obj.display_message
     
#    Error: Fix the method call syntax.  

# 8. Code:  
   
#    arr = np.array((1, 2, 3))
#    sliced = arr[1:3:0]
     
#    Error: Correct the slicing step value.  

# 9. Code:  
   
#    def greet(name):
#        print("Hello" + name)
#    greet()
     
#    Error: Pass the required parameter to the function.  

# 10. Code:  
    
#     class Car:
#         def __init__(self, make, model):
#             make = make
#             model = model
      
#     Error: Fix the instance variable assignment issue.  


# Section C: Coding (10 Questions)  

# 1. Write a Python function to compute the factorial of a number using procedural programming.  

# 2. Implement a numpy program to create a 1-D array of numbers from 1 to 10. 
# arr=np.arange(1,10)
# print(arr) 
# output:
# [1 2 3 4 5 6 7 8 9]
# 3. Create a 2-D numpy array of size (3 times 3) and fill it with random integers.  
from numpy import random as rd
# arr=rd.randint(1,10,(3,3))
# print(arr)
# output:
# [[4 3 1]
#  [8 6 6]
#  [6 9 5]]
# 4. Write a Python program to demonstrate inheritance in OOP.  

# 5. Slice a 3-D numpy array to extract a specific 2-D plane.  
# arr=np.arange(1,19).reshape(2,3,3)
# print(arr)
# print(arr[0])
# output:
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]

#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]]
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 6. Create a function using functional programming to filter even numbers from a list.  

# 7. Write a Python program to create and use a class with a private attribute.  
class Sample:
    def __init__(self):
        self._a=10
    def getprivate(self):
        print(self._a)
    def setprivate(self,a):
        self._a=a
s=Sample()
print(s._a)
s.getprivate()

# 8. Implement a numpy program to reshape a 1-D array of 12 elements into a 2-D (4 times 3) array.  
# arr=np.arange(1,13)
# print(arr)
# arr2=arr.reshape(4,3)
# print(arr2)
# output:
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# 9. Write a Python program to demonstrate method overloading in OOP.  

# 10. Create a numpy array and demonstrate slicing to reverse its elements.  
