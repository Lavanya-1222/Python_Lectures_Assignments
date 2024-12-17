
# Loop(For-iterative)-AssignmentLoop(For-iterative)-Assignment
# 1. Write a program that takes a list of integers and
#  removes all elements that appear more than once, using loops and conditionals. 
# Return the modified list.
# l=[1,2,3,1,2,3,4,5,1,6,2]
# un=[]
# for i in l:
#     if l.count(i)>=2:
#          pass
#     else:
#          un.append(i)

        
# print(un)
# output:[4, 5, 6]


# 2. Given a list of tuples, each containing a string and a number, 
# write a program to filter out the tuples where the number is less than 10,
#  using a for loop and conditional statements.
# l=['123',23,456,'67',788,0,1,2,3,90,12,8,'7']

# for i in l:
#      if int(i)<10:
#          print(i)
    
# output:=
# 0
# 1
# 2
# 3
# 8
# 7

# 3. Write a program that takes a set of numbers and 
# prints the sum of all numbers that are divisible by 3 but not 5. Use a loop and conditional logic to solve this.
# l=[3,6,9,5,10,15,12,10,4,8,51]
# sum=0
# for i in l:
#     if(i%3==0 and i%5!=0):
#         sum+=i
# print(sum)

# output:81

# 4. Given a dictionary where the keys are names and the values are ages, 
# write a program to print the names of people who are over 18, using a loop and a conditional check.
# d={'lava':24,'sama':34,'john':10,'smita':18}

# for k,v in d.items():
#     if(v>18):
#         print(k,v)

# output:
# lava 24
# sama 34

# 5. Create a program that iterates over a list of strings 
# and finds the longest string, using a loop and conditional checks.
# l=['lavanya','i','am','my','role','datascience']
# max=''
# for i in range(len(l)):
#     if len(l[i])>=len(max):
#         max=l[i]
# print(max)
   
# output:datascience

# 6. Write code that iterates through a set of integers and 
# adds 2 to each element if it's even, and subtracts 2 if it's odd. Return the resulting set.
# l=[1,2,3,4,10,20,30,5,7,9,13,12]
# l2=[]
# print(l)
# for i in range(len(l)):
#     if l[i]%2==0:
#         l[i]=l[i]+2
#     else:
#         l[i]=l[i]+3
# print(l)
# output:
# [1, 2, 3, 4, 10, 20, 30, 5, 7, 9, 13, 12]
# [4, 4, 6, 6, 12, 22, 32, 8, 10, 12, 16, 14]

# 7. Given a list of mixed types (integers, floats, and strings), 
# write a program to separate the numbers (integers and floats) into one list 
# and the strings into another list using a loop and conditionals.
# l=[True,1,0,12,'lava',34,9.67,'lotana','c']
# int_l=[]
# string_l=[]
# for i in  l:
#     if(type(i)==int) or  (type(i)==float):
#         int_l.append(i)
#     elif(type(i)==str):
#         string_l.append(i)
# print(int_l)
# print(string_l)

# output:-
# [1, 2, 3, 4, 10, 20, 30, 5, 7, 9, 13, 12]
# [4, 4, 6, 6, 12, 22, 32, 8, 10, 12, 16, 14]





# 8. Write a program that iterates through a list of dictionaries
#  (each representing a person with a name and age) and 
# prints the names of people older than 30, using a for loop and a conditional.
# d={'lava':24,'sama':34,'john':10,'smita':38}

# for k,v in d.items():
#     if(v>30):
#         print(k,v)
# output:-
# sama 34
# smita 38

# 9. Create a program that checks if a given number is both in a set 
# and in a dictionary’s keys, printing a corresponding message. 
# Use both a conditional and a loop to achieve this.
# n=3
# s={1,2,3,4,5,6,10}
# d={1:23,2:34,4:67,3:78}
# if n in s and n in d:
#     print("True")
# else:
#     print("false")

# output:True

# 10. Given a tuple of tuples, where each inner tuple contains two integers, 
# write a program to find the sum of all second elements in each tuple using a loop and conditional checks.
# t=((1,2),(3,4),(5,6),(10,100))
# sum=0
# for i in t:
#     sum+=i[1]
# print(sum)

# output:112

# 11. Write a program to merge two lists, 
# but only include elements that appear in both lists (set intersection). 
# Use loops, sets, and conditionals.
# l=[10,20,30,40,60]
# l2=[10,20,50,30,60]
# s=set()
# for i in l2:
#     if i in l:
#         s.add(i)
# print(s)

# output:{10, 20, 30, 60}


# 12. Write a program that takes a dictionary and
#  finds the keys that have a value greater than 100, using a loop and conditionals.
# d={1:100,2:400,3:3,4:45,5:130,6:9000}

# for k,v in d.items():
#     if(v>100):
#         print(k)
# output:-
# 2
# 5
# 6

# 13. Using a set, create a program that removes all elements from the set 
# that appear in a given list, using loops and conditionals.
# l=[10,20,30,40,1,2,34,67]
# s={2,3,4,10,40,6}

# for i in l:
#     if i in s:
#         l.remove(i)
# print(l)

# output:-[20, 30, 1, 34, 67]

# 14. Write a program that iterates over a list of numbers and 
# finds the largest number that is not divisible by 2 or 3, using a loop 
# and conditional statements.
# l=[2,4,8,15,18,16,12,40,23,34,89,94]
# l2=[]
# for i in l:
#     if i%2!=0 and i%3!=0:
#         l2.append(i)
# print(l2)
# print(max(l2))

# output:[23, 89]
# 89

# 15. Given a list of tuples, each containing a string and a number,
#  write a program that filters out the tuples where the string starts with a vowel 
# and the number is even. Use loops and conditionals.
# l=[('abc',2),('lava',24),('okay',3),('opra',12)]

# for i in l:
#     if (i[0][0] in 'ioeua') and i[1]%2==0:
#         print(i)
# output:
# ('abc', 2)
# ('opra', 12)

# 16. Create a program that iterates through a list of dictionaries,
#  where each dictionary contains a person’s name and age. 
# The program should print out the names of all people whose age is between 18 and 30,
#  using a loop and a conditional.
# d={'lava':24,'sama':34,'john':10,'smita':20,'samarth':9}

# for k,v in d.items():
#     if(v<30 and v>18):
#         print(k,v)
# output:
# lava 24
# smita 20

# 17. Given a set and a dictionary, 
# write a program that finds the common elements between the set and the dictionary’s keys
#  and returns them as a set, using loops and conditionals.
# d={1:23,2:34,4:67,3:78}
# s={1,2,3,6}
# s2=set()

# for i in s:
#     if i in d:
#         s2.add(i)
# print(s2)
# output:-
# {1, 2, 3}

# 18. Write a program to check if a tuple is a subset of another tuple, 
# using a loop and a conditional check.
# t=(1,2,3,45,5)
# t2=(1,45)
# f=True
# for i in t2:
#     if i not in t:
#         f=False
#         break
# print(f)

# output:=True

# 19. Create a program that takes a list of numbers and 
# prints all the numbers greater than 50, using a while loop and a conditional check.
# l=[200,230,20,1,503,12,23,45,1,2]

# i=0
# while(i<len(l)):
#     if(l[i]>50):
#       print(l[i])
#     i+=1

# output:200
# 230
# 503

# 20. Given a dictionary of items and their prices,
#  write a program to check which items have a price greater than 20, and 
# return a list of those items using a loop and conditionals.
# d={'T-shirt:':200,'cloth':20,'Cup':50,'laptop':10}
# l=[]
# for i in d.values():
#     if i>20:
#         l.append(i)
# print(l)

# output:[200,50]


