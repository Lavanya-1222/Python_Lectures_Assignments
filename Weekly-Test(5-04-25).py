
# 1.Write a function that reads an integer from the user and raises a custom exception if the number is not in the range 1-100. 
# Handle the exception and prompt the user until a valid number is entered.
# n=int(input("enter no "))
# class RangeError(Exception):
#     pass
# try:
#     if n not in range(1,100):
#         raise RangeError("Number is not in range")
#     else:
#         print(n)
# except RangeError:
#     print("Enter number between 1-100")
# output:
# enter no 0
# Enter number between 1-100


# 2.Write a function that accepts a list of integers and returns a list of integers where each element is the square of the original list element, 
# but only include squares of even numbers.
# l=[1,2,3,5,6]
# lst=[i**2 for i in l if i%2==0]
# print(lst)

# 3.Write a Python function that attempts to divide two numbers, catching and handling ZeroDivisionError, TypeError, and custom exceptions for negative input values.
# class NegativeInput(Exception):
#     pass
# def devide(a,b):
#     try:
#         a=int(a)
#         b=int(b)
#         if a<0 or b<0:
#             raise NegativeInput
#         print(a/b)
#     except ZeroDivisionError:
#         print("Not able devide boz of Zero divisible Error")
#     except ValueError as t:
#         print(t)
#     except NegativeInput:
#         print("Negative number not able to delete")
# devide(input("enter number "),input("Enter no "))

# output:
# enter number 0  
# Enter no abc
# invalid literal for int() with base 10: 'abc'
#     enter number 0
# Enter no -2
# Negative number not able to delete
# enter number 5
# Enter no 0
# Not able devide boz of Zero divisible Error


# 4.Write a Python script that counts the number of lines, words, and characters in a given text file.


# 5.Write a function that takes a list of integers and returns the list sorted in ascending order, but with all duplicates removed.
# l=[1,1,2,3,2,4,5,9,8,4,7,2]
# l=list(set(l))
# print(sorted(l))

"""
# 6.Create a function that merges two lists into a dictionary, where the elements of the first list are the keys and the elements of the second list are the values. 
# Handle cases where the lists are of unequal length.
name=['A','B','C','D','E']
age=[20,24,30,34]
l=''
if len(name)>len(age):
    ln=len(name)
    l='name'
else:
    ln=len(age)
    l='age'
print(ln)
d={}
for i in range(ln):
    try:
        d.update({name[i]:age[i]})
    except IndexError:
        if l=='age':
            break
        else:
            d.update({name[i]:None})
print(d)
"""
# output: {'A': 20, 'B': 24, 'C': 30, 'D': 34, 'E': None}


# 7.Write a function that takes a string and returns a new string with all duplicate characters removed.
# s=input("enter string ")
# r=''
# for i in s:
#     if i not in r:
#         r+=i
# print(r)
# output:
# enter string lavanya
# lavny


# 8.Write a function that takes a string and returns True if it is a valid palindrome, ignoring spaces, punctuation, and case.
# s=input("enter string ").strip()
# r=''
# for i in s:
#     if i.isalpha():
#         r+=i
# print(r)
# if r==r[::-1]:
#     print('Palindrom')
# else:
#     print("Not Palindrom")
# output:
# enter string           woo w#
# woow
# Palindrom


# 9.Create a class 'Library' that maintains a list of books. Implement methods to add a book, remove a book, and list all books currently in the library. 
class Library:
    def __init__(self):
        self.books = {
    1: {"title": "Atomic Habits", "author": "James Clear", "price": 499},

    2: {"title": "Deep Work", "author": "Cal Newport", "price": 550},
    
}
    def add_book(self,d):
        mx=max(self.books)
        self.books.update({mx+1:d})
    def remove_book(self,name):
        for k,val in self.books.items():
            if val['title']==name:
                self.books.pop(k)
                break
    def list(self):
        for i in self.books.items():
            print(i)
l=Library()
l.list()
l.add_book({'title': 'Deep Work', 'author': 'Cal Newport', 'price': 700})
l.list()
l.remove_book('Deep Work')
l.list()
# Ensure proper error handling for cases like trying to remove a book that doesn't exist.

# 10.Write a function that accepts a list of integers and returns a list of the first n Fibonacci numbers, where n is the length of the input list.

# 11.Write a function that takes a string and returns a new string with each word reversed but the word order preserved.

# 12.Create a function that takes a string and returns the longest substring without repeating characters.

# 13.Define a class Person with attributes for name and age. Implement a subclass Employee that adds an attribute for salary and a method to 
# calculate the annual bonus (e.g., 10% of salary).

# 14.Implement a function that generates a random password of a given length. The password should include uppercase and lowercase letters, digits, 
# and special characters.

# 15.Create a function that takes a string and returns a dictionary with the frequency count of each character. Ignore case and non-alphabetic characters.