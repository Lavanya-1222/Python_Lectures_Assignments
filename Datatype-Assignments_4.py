# Lists

# 1. Remove all duplicate elements from a list without using set().
#    Hint: keys of dictionary are unique .	
# l=[10,20,30,40,10,20,30,60,80]
# d={}
# d.update({l[0]:l.count(l[0])})
# d.update({l[1]:l.count(l[1])})
# d.update({l[2]:l.count(l[2])})
# d.update({l[3]:l.count(l[3])})
# d.update({l[4]:l.count(l[4])})
# d.update({l[5]:l.count(l[5])})
# d.update({l[6]:l.count(l[6])})
# d.update({l[7]:l.count(l[7])})
# d.update({l[8]:l.count(l[8])})
# print(list(d.keys()))

# outpu:-[10, 20, 30, 40, 60, 80]


# 2. Sort a list of strings in ascending order based on string length.
# l=['lavanya','lava','lk','lavanyan34','abc']

# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if len(l[j])>len(l[j+1]):
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
# print(l)

# output:['lk', 'abc', 'lava', 'lavanya', 'lavanyan34']



# 3. Check if all numbers in a list are positive.
# l=[10,20,-3,-4,20]

# for i in l:
#     if(i<0):
#         print("Not poitive")
#         break
# else:
#     print("Positive")
# output:
# Positive

# 4. Find the second largest element in a list of numbers.
# l=[10,20,12,34,34,34,56,56,56]
# l.sort(reverse=True)
# print(l)
# for i in range(len(l)):
#     if(l[i]>l[i+1]):
#         print(l[i+1])
#         break
# output:34

# 5. Reverse a list without using the reverse() method.

# l=[10,20,30,40,1,2,3,4]
# r=[]
# for i in range(len(l)-1,-1,-1):
#     r.append(l[i])
# print(r)

# output:[4, 3, 2, 1, 40, 30, 20, 10]


#  Sets

# 1. Find the union of two sets.
# s={1,2,3,4,8,9}
# s2={2,3,8,0,90}
# print(s.union(s2))
# output:-
# {0, 1, 2, 3, 4, 8, 9, 90}

# 2. Find the intersection of two sets.
# s={1,2,3,4,8,9}
# s2={2,3,8,0,90}
# print(s.intersection(s2))
# output:
# {8,2,3}

# 3. Check if one set is a subset of another.
# s={1,2,3,4,8,9}
# s2={2,3,8,0,90}
# s3={2,8}
# print(s2.issubset(s))
# print(s3.issubset(s))

# output:
# False
# True

# 4. Find the difference between two sets.
# s={1,2,3,4,8,9}
# s2={2,3,8,0,90}
# print(s.difference(s2))
# output:{1,4,9}

# 5. Check if two sets have any elements in common.
# s={1,2,3,4,8,9}
# s2={2,3,8,0,90}
# print(s.intersection(s2))
# output:{8,2,3}

                                            #  Tuples

# 1. Swap the first and last elements of a tuple.
# t=(10,20,30,40)
# t=list(t)
# temp=t[0]
# t[0]=t[-1]
# t[-1]=temp
# t=tuple(t)
# print(t)
# output:
# (40, 20, 30, 10)

# 2. Find the largest element in a tuple.
# t=(10,200,30,45,78)
# print(max(t))
# output:200

# 3. Check if the elements in a tuple are sorted in ascending order.
# A)
# t=(10,20,30,40,56,1,3)
# t2=(1,2,10,20,30,40,56)
# print(t==sorted(t))
# print(sorted(t2))
# print(t2==tuple(sorted(t2)))
# output:
# False
# [1, 2, 10, 20, 30, 40, 56]
# True

# 4. Convert a tuple to a list.
# t=(1,2,3,'tt')
# t=list(t)
# print(type(t),t)
# output:<class 'list'> [1, 2, 3, 'tt']

# 5. Find the sum of all elements in a tuple.
# sum=0
# t=(10,20,30,40,50)
# for i in t:
#     sum+=i
# print(sum)
# output:150


#  Dictionaries

# 1. Check if a key exists in a dictionary.
# d={1:20,2:67,3:'kll'}
# k=4
# p=3
# print(k in d)
# print(p in d)
# output:
# False
# True

# 2. Merge two dictionaries (without using update()).
# d2={'l':'Mira','b':'ou'}
# d={1:20,2:67,3:'kll'}
# d3=d|d2
# print(d3)

# output:{1: 20, 2: 67, 3: 'kll', 'l': 'Mira', 'b': 'ou'}

# 3. Find the key with the maximum value in a dictionary.
# d={1:10,2:20,3:40,0:100,'k':230,9:9}

# m=max(d.values())

# for k,v in d.items():
#     if v==m:
#         print(k,v)
#         break;
# output:k 230


      


# 4. Sort a dictionary by keys in ascending order
# d={1:10,20:20,3:40,0:100,40:230,9:9}
# print(sorted(d))

# 5. Check if a value exists in a dictionary.
# d={1:10,20:20,3:40,0:100,40:230,9:9}
# n=40
# for v in d.values():
#     if v==n:
#         print('Exist')
#         break

# output:Exist
# DataTypes-Assignment.txt
# Displaying DataTypes-Assignment.txt.