# 1)  l=[1,3,('a',[1,'mark',66,(22,"zakurberg","l")]),[44,[45,('Elliot'),{'a':1,'Company':['Facebook',2001],'b':'Meta'},93],90]] 
# o/p: Mark Elliot Zuckerberg is an American businessman who co-founded 
#     the social media service Facebook and its parent company Meta Platforms. 
# l=[1,3,('a',[1,'mark',66,(22,"zakurberg","l")]),[44,[45,('Elliot'),{'a':1,'Company':['Facebook',2001],'b':'Meta'},93],90]] 
# print(l[2][1][1]+" "+l[2][1][3][1]+" is an American businessman who co-founded the social media service"+" " +l[3][1][2]['Company'][0] +" and its parent company "+l[3][1][2]['b']+" Platforms")


# 2) Find the greatest smallest and the middle from nos given by user.
# n1=int(input("enter no1 "))
# n2=int(input("enter no2 "))
# n3=int(input("enter no3 "))

# if n1>n2 and n1>n3:
#     print(n1,"Is greatest")
# elif n2>n3 and n2>n3:
#     print(n2,"Is greatest")
# else:
#     print(n3,"Is greatest")

# if n1<n2 and n1<n3:
#     print(n1,"Is Smallest ")
# elif n2<n3 and n2<n3:
#     print(n2,"Is Smallest ")
# else:
#     print(n3,"Is Smallest ")

# if (n1>n3 and n1<n2) or (n1>n2 and n1<n3):
#     print(n1,"Is Meddlest")
# elif (n2>n3 and n2<n1) or (n2>n1 and n2<n3):
#     print(n2,"Is Middlest")
# else:
#     print(n2,"Is Middlest")


# 3) Write a lambda function to filter nos. greater than 20. [1,7,30,20,32,60,3,7,19,21,47]
# l=[1,7,30,20,32,60,3,7,19,21,47]
# print(list(filter(lambda x:x>20,l)))


# 4) Write a program that checks whether a given year is a leap year or not. 
#    A leap year is determined based on the following rules:
#    If the year is divisible by 4, it might be a leap year.
#    However, if the year is divisible by 100, it is not a leap year unless.
#    The year is also divisible by 400, in which case it is a leap year.
# year=int(input("enter year "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year,"Leap year")
#         else:
#             print(year,"Not Leap year")
# else:
#             print(year,"Not leap year")


# 5) You are given a list of dictionaries, where each dictionary contains information about a student (their name and age). 
#       Write a list comprehension to create a list of the names of all students who are over 18 years old.
#       students = [{"name": "Alice", "age": 17},{"name": "Bob", "age": 20},{"name": "Charlie", "age": 19},{"name": "David", "age": 22},{"name": "Eve", "age": 16}]
#       o/p: ["Bob", "Charlie", "David"]
# students = [{"name": "Alice", "age": 17},{"name": "Bob", "age": 20},{"name": "Charlie", "age": 19},{"name": "David", "age": 22},{"name": "Eve", "age": 16}]
# l=[d['name'] for d in students if d['age']>18 ]

# l=[]
# for d in students:
#     if d['age']>18:
#         l.append(d['name'])
# print(l)
        

# 6) The Treasure Hunt Map

#  You’re part of a team searching for a hidden treasure on an island. 
#  The map you have is in the form of a list of coordinates (x, y). 
#  However, some coordinates are incomplete or contain errors, such as strings instead of integers. 
#  Your task is to count how many valid coordinates are provided and which ones are usable for your search.
'''
coordinates = [(1, 2), (3, "4"), ("5", 6), (7, 8), ("10", "11"), (9, 10)]
c=0
for t in coordinates:
         if type(t[0])==int and type(t[1])==int:
              c+=1

print("Count:",c)
'''


# 7) Write a Python program to check if a string contains only digits.
# s=input("enter string ")
# if s.isdigit():
#     print("string contains only digit")
# else:
#     print("False")

 
# 8) Implement a function to replace multiple spaces in a string with a single space.
# s=input("enter String ")#lava     miranam                nagesh
# s=s.strip()
# sword=" "
# r=''
# for i in range(len(s)):
#     if s[i]==' ':
#         if s[i+1]!=" ":
#             r=r+" "+s[i]
#         else:
#             continue
#     else:
#         r+=s[i]
# print(r)   


# 9) Implement a function to remove a given character from a string.
# s=input("enter string ")
# k=(input("enter charecter "))
# r=""
# for i in s:
#     if k!=i:
#         r+=i
# print(r)


# 10) Write a Python program to find the most frequent character in a string.
# s=input("enter string ")
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# max=0
# chr=''
# for i in d:
#     if d[i]>max:
#         max=d[i]
#         chr=i
# print(max,chr)

# 43. Write a Python program to find the first non-repeating character in a string.  
# s=input("enter string ")#lavanya
# l=[]
# f=1
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1

# # 1. Sum of List Elements:
# #    Write a Python function that takes a list of numbers as input and returns the sum of all the numbers in the list.
# l=list(list(map(int,input("enter elements in list ").split(" "))))
# sum=0
# for i in l:
#     sum+=i
# print("sum",sum)


# 2. Find Maximum in List:
#    Write a Python function that finds and returns the maximum value in a list of numbers without using the max() function.
# l=list(map(int,input("enter elements ").split(" ")))
# max=0
# for i in l:
#     if i>max:
#         max=i
# print("Maximum",max)


# 3. List Reversal:
#    Write a Python function to reverse a list in-place. Do not use any built-in list reversal functions.
# l=list(map(int,input("enter elemnets ").split(" ")))#[10 20 30 40] [10,20,30]
# r=(len(l)-1)#40
# for i in range(len(l)//2):
#     l[i],l[r]=l[r],l[i]
#     r-=1
# print(l)


# 4. Count Occurrences:
#    Write a Python function that takes a list and a value as input and returns the number of times the value appears in the list.
# l=list(map(int,input("enter list elements ").split(" ")))
# print({i:l.count(i) for i in l})


# 5. Remove Duplicates:
#    Write a Python function that takes a list as input and returns a new list with duplicate elements removed while preserving the original order of elements.
# l=list(map(int,input("enter list elements ").split(" ")))
# r=[]
# for i in l:
#     if i not in r:
#         r.append(i)
# print(r)


# 6. List Comprehension:
#    Create a list comprehension that generates a list of squares of all even numbers from 1 to 20.
# print([i**2 for i in range(1,20) if i%2==0])


# 7. Function with Default Argument:
#    Write a Python function that takes two arguments: a string and an integer (with a default value of 1). The function should return the input string repeated the specified number of times.
# def func(s,i=1):
#     return s*i
# print(func('codenera'))
# print(func('codenera',3))


# 8. Function to Filter Odd Numbers:
#    Write a Python function that takes a list of numbers and returns a new list containing only the odd numbers from the original list.
# l=list(map(int,input("Enter elements ").split(" ")))
# print([i for i in l if i%2!=0])


# # 9. List Sum of Even and Odd:
# # Write a Python function that takes a list of numbers and returns a tuple containing the sum of even and odd numbers separately.
# l=list(map(int,input("Enter elements ").split(" ")))
# se=0
# so=0
# for i in l:
#     if i%2==0:
#         se+=i
#     else:
#         so+=i
# t=(se,so)
# print(t)


# 10. WAP to find 2nd max element from list
# l=list(map(int,input("Enter elements ").split(" ")))# 1 2 3 4 5 
# max=0
# secmax=0
# for i in l:
#     if i>max:
#         max=i
#     elif i>secmax and i<max:
#         secmax=i
# print(max,secmax)

# 31. Write a Python program to find the Cartesian product of two sets.
# s1={1,2,3,4}
# s2={10,20,30,40}
# s3=[]
# for i in s1:
#     for j in s2:
#         s3.append(i*j)
# print(s3)

# 
# 32. Implement a function to find the power set of a given set.
# s={'a','b','c'}
# s2=set()
# for i in s:
#     for j in s:
#         if i==j:
#             s2.add(i)
#         else:
#             if j+i!=i+j:
#                 s2.add(i+j)
# print(s2)

    
# 33. Create a program to generate all possible combinations of elements from a set.

# 34. Write a Python function to find the maximum and minimum elements in a set.
s={1,2,3,4,5,10,5}
max=0
for i in s:
    min=i
    break
for i in s:
    if i>max:
        max=i
    if i<min:
        min=i
print(min,max)

# 35. Implement a function to check if a set is a superset of another set.
# s={1,2,3,4,5,6}
# s2={1,2,3}
# print(s.issuperset(s2))

# 36. Write a program to find the difference between two sets while preserving the order of elements.
# s1={1,2,0,3,4,5,6,90}
# s2={1,2,3,5}
# l2=[]
# for i in s1:
#     if i not in s2:
#         l2.append(i)
# print(l2)


# 37. Create a Python function to check if a set is immutable.
# s={1,2,3,4,5}
# s2=frozenset({1,2,3,4})
# print(isinstance(s2,frozenset))
# print(isinstance(s,frozenset))

# 38. Write a program to find the most common element in a set 
# s={1,2,3,4,5,7,1,2,4,4,4,5,6,1}
#  it is not possible set is not have sany duplicate elements in it 


# 39. Implement a function to partition a set into two subsets such that the difference of their sums is minimized.












    


     




