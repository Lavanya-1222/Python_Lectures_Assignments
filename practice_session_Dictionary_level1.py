# 1. Convert two list into one dictionary. (using zip function and without zip function)
# l1=['xyz','pqr','abc','wrv']
# l2=[67,89,90,87]

# for k,v in zip(l1,l2):
#     print(k,v)
# print()
# for i in range(len(l1)):
#     print(l1[i],l2[i])


# 2. Write a Python script to sort (ascending and descending) a dictionary by value.
# d={'xyz':89,'abc':90,'pqr':78,'wvp':70}
# print(sorted(d.items(),key=lambda x : x[1]))
# print(sorted(d.items(),key=lambda x : x[1],reverse=True))

# 3. Write a Python program to combine two dictionary by adding values for common keys.
# d1={'A':10,'B':90,'C':10}
# d2={'A':20,'D':20,'E':30,'C':10}
# d3=d1.copy()
# print(d3)
# for k,v in d2.items():
#     if k in d3:
#         d3.update({k:v+d3[k]})
#     else:
#         d3.update({k:v})
# print(d3)

# 4. Write a Python function to count the frequency of each word in a given text document 
#    and return a dictionary with word frequencies.
# s=input("enter string ")
# word=''
# lst=[]
# for i in s:
#     if i!=" ":
#         word+=i
#     else:
#         lst.append(word)
#         word=''
# lst.append(word)
# # print(lst)

# d={}
# for i in lst:
#     if i in d:
#         d[i]+=1

#     else:
#         d[i]=1
# print(d)


# 5. Given two dictionaries, write a function to find and return a new dictionary containing 
#    only the common keys and their corresponding values.
# d1={'A':10,'B':90,'C':10}
# d2={'A':20,'D':20,'E':30,'C':10}
# d3={}
# for i in d1:
#     if i in d2:
#         d3[i]=[d2[i],d1[i]]   
# print(d3)


# 6. Develop a function that finds the element with the maximum frequency in a list 
#     and returns the element along with its frequency.
# l=[1,1,2,3,4,1,6,7,8,1]
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# mx=0
# chr=''
# for i in d:
#     if d[i]>mx:
#         mx=d[i]
#         chr=i
# print(chr)


# 7. Write a Python script to concatenate the following dictionaries to create a new one.
# d1={'A':10,'B':20,'C':89}
# d2={1: 4, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1}
# d3={'D':9,'G':8}
# d4=d1.copy()
# for i,v in d2.items():
#     d4[i]=v
# print(d4)
# for i,v in d3.items():
#     d4[i]=v
# print(d4)

# 8. WAP and Find the Key with Maximum Value.
# d={'A':10,'B':20,'C':89}
# mx=0
# chr=''
# for k,v in d.items():
#     if v>mx:
#         mx=v
#         chr=k
# print(chr)


# 9. Write a function to invert a dictionary, swapping keys and values.(with duplicates value)
# d={'A':10,'B':20,'C':89}
# d2={}
# for i,v in d.items():
#     d2[v]=i
# print(d2)

# 10. Find the common keys between two dictionaries and return a dictionary with common keys 
#     and their values from the first dictionary.
d1={'A':10,'B':20,'C':89}
d2={'A':20,'D':80,'C':90}
d3={}
for i in d1:
    if i in d2:
        d3.update({i:d1[i]})
print(d3)
