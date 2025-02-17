# # Section A: Theory  
import numpy as np 
import pandas as pd

# # 1. What is a NumPy array, and how is it different from a Python list?  

# # 2. Explain the concept of broadcasting in NumPy with an example.  

# # 3. What are ufuncs in NumPy? Provide an example.  
# x=[1,2,34,4]
# y=[10,10,20,10]
# print(np.add(x,y))
# print(type(np.add))
# print(np.sqrt(x))
# print(type(np.sqrt))
# print(np.less(x,y))

# def each_add_10(x,y):
#     return x+y+10
# arr=np.frompyfunc(each_add_10,2,1)
# print(arr(x,y))

# # 4. What is the purpose of the numpy.random module? Name three functions it provides.  
# from numpy import random as rd
# # rand
# # print(rd.rand(2,2))
# # [[0.08217302 0.5734172 ]
# #  [0.61766962 0.03358355]]


# #randint
# # print(rd.randint(1,10)) ->5
# # print(rd.randint(1,10,(2,2)))
# # [[3 2]
# #  [5 8]]

# # print(rd.randint(1,10,size=5))
# # [3 4 1 2 1]

# # randn
# # print(rd.randn(2,2))
# # [[ 2.24035776  1.23595522]
# #  [-0.39494653 -0.6499075 ]]

# # choice
# # print(rd.choice([1,2,3,4]))#2
# print(rd.choice([1,1,4,5,6],size=6))#[6 1 6 5 1 1]
# print(rd.choice([1,2,3,4],size=3,replace=False))#[2 1 4]
# print(rd.choice([1,2,1,3,4],size=4,replace=False))#[2 4 1 1]
# # print(rd.choice([1,2,3,4,1],size=6,replace=False))#Error


# # Shuffle
# arr=[10,20,30,40]
# rd.shuffle(arr)
# print(arr)
# arr2=np.array([[10,20,30],[11,22,33],[1,2,3]])
# rd.shuffle(arr2)
# print(arr2)


# # Permutation
# print(rd.permutation([1,2,3,7,8,9,0]))

# #uniform
# print("Uniform",rd.uniform(1,100))

# #normal
# print(rd.normal(0,1,(2,2)))

# #binomal
# print(rd.binomial(10,0.5,3))


# #seed
# rd.seed(12)#it can be any number
# print(rd.rand())


# 5. Explain how to compute the transpose of a matrix in NumPy.  
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)
# trans=np.transpose(arr)
# print(trans)
# witht=trans.T
# print(witht)
# output:
# [[1 2 3]
#  [4 5 6]]
# [[1 4]
#  [2 5]
# #  [3 6]]
# [[1 2 3]
#  [4 5 6]]
# 6. Define the inverse of a matrix. When does a matrix not have an inverse?  
# arr=[[4,7],[2,6]]
# print("Inverseal",np.linalg.inv(arr))
# 7. What are the primary features of a pandas Series?  

# 8. How does a pandas Series differ from a NumPy array?  

# 9. What is the role of the dtype parameter in a pandas Series?  
# print("Q-9-----------")
# s=pd.Series([1,2,3,"hello"])
# print(s)
# s1=s.astype('string')
# print(s1)
# print(type(s1[0]))

# s2=pd.Series([1,1,2],dtype='float32')
# print(s2)

# 10. Discuss the advantages of using pandas over NumPy for data analysis.  



# Section B: Correct the Error  
# 1. arr = np.array[1, 2, 3]
#ANS 
# arr = np.array([1, 2, 3])


# 2. result = np.random.randint(10, 20, size=5, replace=False)  
# ANS: 
# result = np.random.randint(10, 20, size=5)  #replace is present choice function


# 3. np.add([1, 2, 3], [4, 5]) 
# ANS 
# # print(np.add([1, 2], [4, 5]) )


# # 4. matrix = np.array([[1, 2], [3, 4]]) print(matrix.T()  
# matrix = np.array([[1, 2], [3, 4]]) 
# # ANS: print(matrix.T) 

# # 5. inv_matrix = np.linalg.inv([[1, 2], [3, 4]])  
# # inv_matrix = np.linalg.inv([[1, 2], [3, 4]]) 
# # ANS 
# # print(inv_matrix)
# # [[-2.   1. ]
# #  [ 1.5 -0.5]]


# # 6. series = pd.Series[1, 2, 3]  
# # ANS
# series = pd.Series([1, 2, 3])
# print(series)

# # 7. data = {'a': 1, 'b': 2, 'c': 3} pd.Series(data, index=data.keys)  
# data = {'a': 1, 'b': 2, 'c': 3} 
# print(pd.Series(data))

# # 8. random_arr = np.random.random(2.5)  
# random_arr = np.random.rand(2,5)

# print(random_arr)
# print(np.random.random(2))#random takes only 1 positional argument 

# # 9. matrix = np.array([1, 2], [3, 4])  
# matrix = np.array([[1, 2], [3, 4]])

# # 10. print(pd.Series([1, 2, 3, 4], dtype=int64))  
# print(pd.Series([1, 2, 3, 4], dtype='int64'))#you  have to give it in string form if you giving with bytes other wise int is ok 


# Section C: Write a Program  
from numpy import random as rd
# 1. Create a 3x3 NumPy array filled with random integers between 1 and 10.  
# arr=rd.randint(1,10,(3,3))
# print(arr)
# output:
# [[3 2 1]
#  [9 1 5]
#  [4 8 4]]


# 2. Write a program to find the transpose of a 4x4 matrix.  
# arr=np.arange(1,17).reshape(4,4)
# print(arr.T)
# output:
# [[ 1  5  9 13]
#  [ 2  6 10 14]
#  [ 3  7 11 15]
#  [ 4  8 12 16]]


# 3. Generate a NumPy array of 10 random floats between 0 and 1.  
# print(rd.rand(10))
# output:
# [0.57443462 0.19231697 0.25399767 0.39233393 0.26131864 0.12850515
#  0.24464098 0.6318173  0.26389712 0.31208749]


# 4. Write a program to compute the inverse of a 2x2 matrix.  
# arr=rd.randint(1,10,(2,2))
# print(np.linalg.inv(arr))
# output:
# [[ 1.16666667 -0.33333333]
#  [-0.66666667  0.33333333]]


# 5. Create a NumPy array and apply the np.sqrt ufunc on all its elements.  
# arr=np.array([1,2,3,4,5,8,16])
# print(np.sqrt(arr))
# output:
# [1.         1.41421356 1.73205081 2.         2.23606798 2.82842712
#  4.        ]


# 6. Write a program to create a pandas Series from a Python dictionary.  
d={'Nitis':78,'Lavanya':90,'Samarth':98,'Kirana':34}
# print(pd.Series(d))
# output:
# Nitis      78
# Lavanya    90
# Samarth    98
# Kirana     34
# dtype: int64


# 7. Create a pandas Series with custom indices and retrieve values using indices.  
# s=pd.Series([78,89,90,56],index=['nitis','samarth','lavanya','kiran'])
# print(s['lavanya'])
# output:90

# 8. Generate a 5x5 identity matrix using NumPy.  
# print(np.eye(5,5,dtype=int))
# output:
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]


# 9. Write a program to create a NumPy array of even numbers between 10 and 30.  
# arr=np.arange(10,30,2)
# print(arr)
# output:
# [10 12 14 16 18 20 22 24 26 28]


# 10. Create a pandas Series from a NumPy array and display its dtype.  
# nprray=np.array([1,2,3,4,5])
# arr=pd.Series(nprray)
# print(arr.dtype)
# print(nprray.dtype)
# output:
# 0    1      
# 1    2      
# 2    3      
# 3    4      
# 4    5      
# dtype: int64
# int64
# int64