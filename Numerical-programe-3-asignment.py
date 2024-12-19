
# NumricalProgams-3-Assignment

# # 1. Given a list of integers, write a program that returns a list with all duplicate elements removed, but preserves the order of the original elements.
# l=[10,1,2,3,4,5,6,10,30,20,2,3,50,80,90]
# for i in l:
#     if l.count(i)>=2:
#         l.remove(i)
# print(l)
# output:
# [1, 4, 5, 6, 10, 30, 20, 2, 3, 50, 80, 90]


# 2. Write a program that takes two sets of integers and returns a list of elements that are present in both sets but not in the other.
# s1={1,2,3,4,5,6,7,8,10}
# s2={1,5,6,10}
# l=list(s1.intersection(s2))
# print(l)
# output:
# [1, 10, 5, 6]

# 3. Write a program that takes a dictionary of people's names and their ages. It should return a dictionary where the names of people who are older than 30 are changed to uppercase.
# d={'lava':90,'nagesh':100,'samarth':150,'pira':8,'shlok':23}
# d2={}
# for k,v in d.items():
#     if v>30:
#        d2.update({k.upper():v})
#     else:
#         d2.update({k:v})
# print(d2)
# output:
# {'LAVA': 90, 'NAGESH': 100, 'SAMARTH': 150, 'pira': 8, 'shlok': 23}

# 4. Write a program that accepts a list of tuples, where each tuple contains a person's name and their age. The program should return a list of names of people whose age is greater than 18.
# l=[('lava',80),('sama',82),('priya',19),('sam',3),('saranya',1)]
# names=[]
# for i in l:
#     if i[1]>18:
#         names.append(i[0])
# print(names)
# output:
# ['lava', 'sama', 'priya']

# 5. Given a list of numbers, write a program that classifies each number as "even" or "odd" and returns the count of "even" and "odd" numbers in the list.
# l=[10,2,4,9,12,8,20,19,34,23,3,5,89,100]
# eo=[]
# for i in l:
#     if(i%2==0):
#         eo.append('even')
#     else:
#         eo.append('odd')
# ec=0
# oc=0
# for i in eo:
#     if i=='even':
#         ec+=1
#     else:
#         oc+=1
# print(l)
# print(eo)
# print("even_count ",ec,"Odd_count ",oc)

# output:
# [10, 2, 4, 9, 12, 8, 20, 19, 34, 23, 3, 5, 89, 100]
# ['even', 'even', 'even', 'odd', 'even', 'even', 'even', 'odd', 'even', 'odd', 'odd', 'odd', 'odd', 'even']
# even_count  8 Odd_count  6

# 6. Write a program that takes a list of integers and returns the sum of all the even numbers. If the sum of even numbers exceeds 100, print "Limit Exceeded" and stop.
#  

# 7. Write a program that prints the following pattern of stars:
    
#     *
#     **
#     ***
#     ****
for i in range(1,4+1):
    for j in range(i):
        print('*',end=" ")
    print()
# output:
# * 
# * * 
# * * *
# * * * *  
#     The number of stars should be equal to the row number.

# 8. Write a program that prints a reverse triangle pattern of numbers, such as:
    
#     12345
#     1234
#     123
#     12
#     1
# i=6
# while(i>1):
#     for j in range(1,i):
#         print(j,end="")
#     print()
#     i-=1
# output:
# 12345
# 1234
# 123
# 12
# 1  

# 9. Write a program that takes a list of integers and prints the sum of the squares of all numbers in the list, using a for-range() loop.
# l=[10,20,2,3,4,5,11]
# sum=0
# for i in range(len(l)):
#     sum+=l[i]**2
# print(sum)
# output:
# 675

# # 10. Write a program that uses a while loop to print all numbers from 1 to 50 that are divisible by 7.
# i=1
# while(i<50):
#     if i%7==0:
#         print(i,end=" ")
#     i+=1
# output:
# 7 14 21 28 35 42 49
# NumricalProgams-3-Assignment.txt
# Displaying NumricalProgams-3-Assignment.txt.