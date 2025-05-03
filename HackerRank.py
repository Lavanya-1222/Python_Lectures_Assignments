"""
#1 Flipping Bits
# n=int(input("Enter no "))
# l=''
# while(n!=0):
#     if n%2==0:
#         l=str(n%2)+l
        
#     else:
#         # l.append(n%2)
#         l=str(n%2)+l
#     n=n//2
# ln=len(l)
# if ln<=32:
#   re='0'*(32-ln)+l
# print(re)
# final=''

# for i in re:
#     if i=='0':
#         final+='1'
#     elif i=='1':
#         final+='0'
# print(final)
# sum=0
# for i in range(len(final)):
#     if final[i]=='1':
#         sum+=2**(31-i)
# print(sum)


# print(int('1000',2))
# print(type(format(8,'b')))
'''
n=int(input("enter no "))
if(True):
    x=format(n,'b')
    re=''
    if len(x)<=32:
        re='0'*(32-len(x))+x
    final=''
    for i in re:
        if i=='0':
            final+='1'
        elif i=='1':
            final+='0'
    print(int(final,2))
   '''

# print(len(l))
"""



#2 Counting_Sort
""" 

def countingSort(arr):
    # Write your code here
    mx=max(arr)
    l=[]
    
    for i in range(100):
        l.append(0)
    for j in arr:
        l[j]+=1
    return l
print(countingSort([1,1,3,2,1]))"
"""

# s=input("enter string ").lower()
# print(s)
# sealevel=0
# start=s[0]
# valley=0
# for i in range(len(s)):
#     if s[i]=='u':
#         sealevel+=1
#     if s[i]=='d':
#         sealevel-=1
#     if start=='u' and sealevel==0 and i!=0:
#         start=s[i+1]
#         sealevel=0
#     if start=='d' and sealevel==0 and i!=0:
#         start=s[i+1]
#         sealevel=0
#         valley+=1

# print(valley)



#3 String Pangram or not 
# import string
# s=input("enter string ").lower()
# print(string.ascii_letters)
# d=len({i:1 for i in s if i in string.ascii_letters})
# if d==26:
#     print("Pangram")
# else:
#     print("Not")


#4 Mars Exploration
# s='sossot'
# c=0
# for i in range(0,len(s),3):
#     sp=s[i:i+3]

#     if sp!='sos':
#         if sp[0]!='s':
#             c+=1
#         if sp[1]!='o':
#             c+=1
#         if sp[2]!='s':
#             c+=1

# print(c)


#5 Permutation Two Array
# a=[0,1]
# b=[0,2]

# a.sort()
# print(a)
# b.sort(reverse=True)
# print(b)
# k=1
# f=1
# for i in range(len(a)):
#     if k>(a[i]+b[i]):
#         f=0
# if f==1:
#     print("Yes")
# else:
#     print("No")
    

#     """


#6 Subarray Division 2 
"""
lst=list(map(int,input().split(" ")))
d=15
m=4
c=0
sm=sum(lst[0:m])
if sm==d:
    c+=1
j=1
while(j<len(lst)):
    if (sum(lst[j:j+m]))==d:
        c+=1
    j+=1
print(c)
    """
                   

"""  
#7 XOR
s1=input("enter string1 ")
s2=input("enter string2 ")
result=''
for i in range(len(s1)):
    if s1[i]==s2[i]:
        result+='0'
    else:
        result+='1'
print(result)

#8 Sales by Match
soks=[1,2,1,2,1,3,2,1]
d={}
for i in soks:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

sum=0
for i in d.values():
    sum+=i//2
print(sum)

""" 
"""
#9 Migratory Birds
lst=[1,1,2,2,3]

d={}
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

mx=max(d.values())
list=[]
for i in d:
    if d[i]==mx:
        list.append(i)
print(min(list))"
"""

