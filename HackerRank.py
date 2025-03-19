#Flipping Bits
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
"""
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
   """

# print(len(l))

# Counting_Sort
""" """

def countingSort(arr):
    # Write your code here
    mx=max(arr)
    l=[]
    
    for i in range(100):
        l.append(0)
    for j in arr:
        l[j]+=1
    return l
print(countingSort([1,1,3,2,1]))