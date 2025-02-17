# Find the duplicates in a list.
# l=list(map(int,input("enter Elements in list ").split(" ")))
# print(l)

# result=[]
# for i in l:
#     if i not in result:
#         result.append(i)
#     else:
#         print(i)

# find out palindrome numbers from list 
l=[123,121,112211,345,676,89]
result=[]
i=0
while(i<len(l)):
    n=l[i]
    r=0
    while(n!=0):
        r=r*10+n%10
        n//=10
    if l[i]==r:
        result.append(l[i])
    i+=1
print("Palindrome List: ",result)


