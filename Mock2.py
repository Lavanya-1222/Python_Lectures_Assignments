lst=[10,20,40,50,60,3,5,6]
l=list(set(lst))

for i in range(len(l)):
    for j in range(len(l)-1):
        t=0
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
new_lst=l[::-1]

print(new_lst[1])




