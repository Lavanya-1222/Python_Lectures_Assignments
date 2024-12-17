
# NumericPrograms-Assignment
# 1.Write a program to reverse a given list of numbers.
# l=[100,121,111,123,1441,1451,1221]
# print("Before",l)
# l2=[]
# for n in l:
#     t=0
#     while(n!=0):
#         r=n%10
#         t=t*10+r
#         n=n//10
#     l2.append(t)
# print("aftere",l2)

# output:
# Before [100, 121, 111, 123, 1441, 1451, 1221]
# aftere [1, 121, 111, 321, 1441, 1541, 1221] 

#2. Write a program to check if a given list is a palindrome.
l=[100,121,111,123,1441,1451,1221]
print("Before",l)
l2=[]
for n in l:
    i=n
    t=0
    while(n!=0):
        r=n%10
        t=t*10+r
        n=n//10
    if(t==i):
        l2.append(f"Palindrom {t}")
    else:
        l2.append(f"Not Palindrom {t}")
print(l2)
# output:
# ['Not Palindrom 1', 'Palindrom 121', 'Palindrom 111', 'Not Palindrom 321', 'Palindrom 1441', 'Not Palindrom 1541', 'Palindrom 1221']

#3. Write a program to reverse a given string using a loop (without slicing).
# s='12231'
# s2=''
# for i in s:
#     s2=i+s2
# print(s2)


# 4.Write a program to calculate the sum of all elements in a list using a loop.
# l=[10,20,30,40,50,60,78,90]
# sum=0
# for i in l:
#     sum+=i
# print(sum)
# output:378

# Write a program to find the maximum and minimum values in a list using a loop.
# l=[10,20,30,40,50,60,78,90]

# min=l[0]
# max=0
# for i in l:
#     if i<min:
#         min=i
#     if i>max:
#         max=i
# print("Min:",min,"Max:",max)
# output:
# Min: 10 Max: 90

# Write a program to count how many times a specific element appears in a list.
# d={}
# l=[1,2,3,1,2,3,1,2,3,4,53,21,1,2,1,2,12,1,1,6,7,8]
# for i in l:
#     d[str(i)]=l.count(i)

# print(d)
# output:
# {'1': 7, '2': 5, '3': 3, '4': 1, '53': 1, '21': 1, '12': 1, '6': 1, '7': 1, '8': 1}

# Write a program to remove duplicates from a list using a set and print the result.
# l=[1,2,3,1,2,3,1,2,3,4,53,21,1,2,1,2,12,1,1,6,7,8]
# l=list(set(l))
# print(l)
# output:
# [1, 2, 3, 4, 6, 7, 8, 12, 53, 21]

# Write a program to check if a list of numbers is sorted in ascending order.
# l=[1, 2, 3, 4, 6, 7, 8, 12, 53, 21]
# l2=[1, 2, 3, 4, 6, 7, 8, 12, 21,53]
# print(l==sorted(l))
# print(l2==sorted(l))
# output:
# False
# True

# Write a program to find the intersection of two lists using a set.
# l1=[10,20,30,40,50]
# l2=[10,20,10,20,30]
# l1=set(l1)
# l2=set(l2)
# print(l1.intersection(l2))
# output:{10, 20, 30}

# Write a program to create a dictionary from two lists—one for keys and the other for values.
# l=['lavanya','samarth','meghana','shlok']
# age=[24,26,12,4]
# d={}
# i=0
# while(i<len(l)):
#     d[l[i]]=age[i]
#     i+=1
# print(d)
# output:
# {'lavanya': 24, 'samarth': 26, 'meghana': 12, 'shlok': 4}

# Write a program to find the sum of all values in a dictionary.
# d={'lavanya': 24, 'samarth': 26, 'meghana': 12, 'shlok': 4}
# sum=0
# for v in d.values():
#     sum+=v
# print(sum)
# output:66
# Write a program to find all even numbers in a list using a loop.
# l=[10,20,30,33,44,23,123,21,12]

# for i in l:
#    if i%2==0:
#       print(i,end=" ")
# output:10 20 30 44 12 

# Write a program to print all numbers between two given numbers using a for-range loop.
# n1=int(input("Enter start range "))
# n2=int(input("enter end range "))

# for i in range(n1,n2):
#     print(i,end=" ")
# output:
# Enter start range 10
# enter end range 15
# 10 11 12 13 14

# Write a program to check if a string is a palindrome using a loop.
# s="MooM"
# r=''
# for i in s:
#     r=i+r
# if(r==s):
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# output:Palindrome


# Write a program to find the union of two sets and print the result.
# s1={1,2,3,1,2,34,4,5,6,78,8}
# s2={34,78,8}
# print(s1.union(s2))

# output:
# {1, 2, 3, 34, 4, 5, 6, 8, 78}


# NumericProblem-Assignment.txt
# Displaying NumericProblem-Assignment.txt.
# NumericPrograms-Assignment
# Talha Hamid Syed
# •
# 12 Dec
# 100 points
# Due Yesterday, 23:59

# NumericProblem-Assignment.txt
# Text
# Class comments
# Your work
# Missing
# Private comments