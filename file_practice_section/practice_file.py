# Q1. Wap create a file enter string in it, now reads that file and finds the frequency of each character.

# with open('file.txt','r') as f:
#     p=f.readline() 
#     d={}
#     for i in p:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     print(d)


# Q2. Wap create a file enter string in it, now reads that file and prints all the words that start from vowel.
# with open('file_2.txt','r') as f:
#     p=f.readline()
#     l=p.split(" ")
#     for i in l:
#         if i[0] in 'AIOUEaioue':
#             print(i)

# Q3. Write a Python program to create a file and enter a string in it. Then, read the file and find the longest word in the file.
# from functools import reduce
# with open('file_2.txt','r') as f:
#     p=f.readline()
#     print(p)
#     lst=p.split(" ")
#     print(reduce(lambda x,y:x if len(x)>len(y) else y,lst))


# Q4. Write a Python program to create a file and enter a string in it. Now, read the file and count the number of sentences in the file.
# with open('file_4','a') as f:
#     n=input("enter done once you done ")
#     while(n!='done'):
#         f.write(n+'\n')
#         n=input()
    


# with open('file_4','r') as f:
#     p=f.readlines()
#     print(p)
#     print(len(p))


# Q5. Write a Python program that reads a file containing multiple lines of text. The program should count the frequency of each word across all lines and then find and print the top 5 most frequent words.
from functools import reduce 
with open('file_4.txt','r') as f:
    lst=[]
    for i in f.readlines():
        temp=i.split(' ')
        lst.append(reduce(lambda x :x if len(x)>len(y) else y),temp)
    print(lst)
        


    


    