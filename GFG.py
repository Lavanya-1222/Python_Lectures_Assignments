#1 reverser the array
# arr=[10,20,30,40]
# def reverseArray(arr):
#         # code here
#         j=len(arr)-1
#         for i in range(len(arr)):
#             t=0
#             if i<j:
#                 t=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=t
#                 j-=1
# reverseArray(arr)
# print(arr)
# -------------------------------------------------------------
#2 array rotation by one
# l=[1, 2, 3, 4, 5]
# #1) l.insert(0,l[-1])
# # l.pop()
# # print(l)

# 2)t=l[len(l)-1]
# st=l[0]
# l[0]=t
# l[-1]=st
# print(l)
# --------------------------------------------------------------------
#3 array duplcate elements Find
arr=[1,2,3,4,1,2,8,8,90]
# b) Optimized way in GFG
# def findDuplicates(arr):
#         d={}
#         for i in arr:
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
#         r=[]
#         for k,v in d.items():
#             if v>1:
#                 r.append(k)
#         return r
# print(findDuplicates(arr))

# a)
# d=[]
# c=0
# for i in l:
#     if i not in d:
#         d.append(i)
#     else:
#         c=1
#         print(i)

# ----------------------------------------------------
#4 Move all negative at start and all positive at end
# def segregateElements(self, arr):
#        dn=[]
#        dp=[]
#         # Your code goes here
#        for i in arr:
#           if i<0:
#              dn.append(i)
#           else:
#               dp.append(i)
#        arr[:len(dp)]=dp
#        arr[len(dp):]=dn
#        return arr
# segregateElements([1 -1 3 2 -7 -5 11 6])

# ------------------------------------------------
#5 Find the Row with a Maximum Number of 1’s
    # def rowWithMax1s(self, arr):
    #     # code here
    #     max=0
    #     f=0
    #     for i in range(len(arr)):
    #         c=arr[i].count(1)
    #         if c>max:
    #             max=c
    #             f=i
    #     return f

# -------------------------------------------------------------
#6 majaority elements wi which comes more than arr.size/2 times
    # def majorityElement(self, arr):
    #     d={}
    #     if len(arr)==1:
    #         return arr[0]
    #     else:
    #         for i in arr:
    #             if i not in d:
    #                 d[i]=1
    #             else:
    #                 d[i]+=1
                    
    #     max=1
    #     # e=-1
    #     for k,v in d.items():
    #         if v>int(len(arr)//2):
    #          return k
    #     return -1
# [3, 1, 3, 3, 2]
# [7]
# [2, 13]=== -1

# --------------------------------------------------------
    # def sort012(self, arr):
    #     cz=0
    #     co=0
    #     ct=0
    #     # d={0:0,1:0,2:0}
    #     for n in arr:
    #         if n==0:
    #             cz+=1
    #         elif n==1:
    #             co+=1
    #         elif n==2:
    #             ct+=1
    #     ind=0
    #     for i in range(cz):
    #         arr[ind]=0
    #         ind+=1
    #     for i in range(co):
    #         arr[ind]=1
    #         ind+=1
    #     for i in range(ct):
    #         arr[ind]=2
    #         ind+=1
            
    #     return arr
# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# ************************************************Level 2****************************************************
# def factorial(n):
#         fact=1
#         for i in range(1,n+1):
#             fact*=i
#         return str(fact)
# s=factorial(5)
# for i in s:
#       print(i,end=" ")


