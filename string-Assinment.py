# 1. Write a Python program to print a right-angled triangle pattern using numbers. The number of rows should be input by the user.

#     Example:  
#    1
#    1 2
#    1 2 3
#    1 2 3 4

# rno=int(input('Enter No. of Row '))
# for i in range(1,rno+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# output:
# Enter No. of Row 4
# 1 
# 1 2
# 1 2 3
# 1 2 3 4

   

#  2. Write a Python program to print an inverted right-angled triangle using numbers. The number of rows should be input by the user.

#    Example:
   
#    5 4 3 2 1
#    5 4 3 2
#    5 4 3
#    5 4
#    5
rno= int(input('Enter no. of row '))
for i in range(rno,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
   
# output:Enter no. of row 5
# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1

#  3. Write a Python program to print a right-angled triangle pattern using alphabets. The number of rows should be input by the user.

#    Example:
   
#    A
#    A B
#    A B C
#    A B C D
   
rno=int(input('Enter no. of rows '))

for i in range(rno):
    z=65
    for j in range(i+1):
        print(chr(z),end=" ")
        z+=1    
    print()
# output:
# Enter no. of rows 5
# A 
# A B
# A B C
# A B C D
# A B C D E


#  4. Write a Python program to print an inverted right-angled triangle pattern using alphabets. The number of rows should be input by the user.

#    Example:
   
#    A B C D E
#    A B C D
#    A B C
#    A B
#    A
rno=int(input('Enter no. of Rows'))
for i in range(rno,0,-1):
    z=65
    for j in range(i,0,-1):
        print(chr(z),end=" ")
        z+=1
    print()

# output:
# Enter no. of Rows5
# A B C D E 
# A B C D
# A B C
# A B
# A

#  5. Write a Python program that prints the multiplication table for a given number (1 to 10) using nested loops.

#    Example for input 5:
   
#    1 x 5 = 5
#    2 x 5 = 10
#    3 x 5 = 15
#    4 x 5 = 20
#    5 x 5 = 25
#    6 x 5 = 30
#    7 x 5 = 35
#    8 x 5 = 40
#    9 x 5 = 45
#    10 x 5 = 50
n=int(input('Enter no '))
for i in range(1,10+1):
    print(n,'X',i,'=',n*i)

# output:-
# Enter no 5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50

#  6. Write a Python program that takes a list of numbers and returns the sum of all even numbers in the list.
#    Example:
   
#    Input: [1, 2, 3, 4, 5, 6]
#    Output: 12
l=[10,20,30,40,50,60,70,80]
sum=0
for i in l:
    if i%2==0:
        sum+=i
print(sum)

# output:
# 360
   

#  7. Write a Python program that finds the maximum and minimum values from a given tuple of numbers.

#    Example:
   
#    Input: (3, 5, 7, 2, 8)
#    Output: Maximum: 8, Minimum: 2
t=(3, 5, 7, 2, 8)
min=t[0]
max=0
for i in t:
    if i>max:
        max=i
    if i<min:
        min=i
print('Minimum: ',min,'Maximum: ',max)

# output:
# Minimum:  2 Maximum:  8

#  8. Write a Python program that takes two sets and returns the union of these two sets.

#    Example:
   
#    Input: set1 = {1, 2, 3}, set2 = {3, 4, 5}
#    Output: {1, 2, 3, 4, 5}
set1 = {1, 2, 3} 
set2 = {3, 4, 5}
print('Union ',set1.union(set2))
# output:
# Union  {1, 2, 3, 4, 5}

#  9. Write a Python program that takes a string, splits it into words, and then reverses the order of the words using loops.

#    Example:
   
#    Input: "Python is great"
#    Output: "great is Python"
l="Python is great".split(" ")
s=''
for i in l:
    s=i+" "+s
print(s)
    
# output:
# great is Python

#  10. Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string using split and loop.

#    Example:
   
#    Input: "Hello, how are you?"
#    Output: 7
l="Hello how are you?".split()
print(s)
v='aioueAIOUE'
c=0
for i in l:
    for j in i:
      if j in v:
         c+=1
print(c)
output:7
