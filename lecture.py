# # # Even Odd check
# # # a=int(input('Enter number'))
# # # if a%2==0:
# # #     print(f'{a} is even')
# # # else:
# # #     print(f'{a} id odd')












# # # check divisible by 5 and 10
# # # a=int(input("enter number"))
# # # if a%5==0 and a%10==0:
# # #     print(f'{a} is divisible by 5 and 10')
# # # else:
# # #     print(f'{a} is not divisible by 5 and 10')









# # # check number is negative or positive
# # # a= int(input("enter number"))
# # # if a>0:
# # #     print(f"{a} is positive")
# # # else:
# # #     print(f"{a} is negative")
















# # # print  wow if number not less than 10000 else b00

# # # no=int(input("enyter number"))
# # # if not(no<10000) :
# # #     print("Wow")
# # # else:
# # #     print("boo")




# # dic={}
# # name=str(input("enter name"))
# # salary=int(input(f"enter salary of {name}"))
# # dic.update({name:salary})

# # name=str(input("enter name"))
# # salary=int(input(f"enter salary of {name}"))
# # dic.update({name:salary})

# # name=str(input("enter name"))
# # salary=int(input(f"enter salary of {name}"))
# # dic.update({name:salary})
# # name=str(input("enter name"))
# # salary=int(input(f"enter salary of {name}"))
# # dic.update({name:salary})
# # list1=sorted(dic.values())
# # list1.reverse()
# # if list1[1]==dic['tom']:
# #     print(list1[1],'tom')

# # elif list1[1]==dic['jim']:
# #     print(list1[1],'jim')

# # elif list1[1]==dic['gary']:
# #     print(list1[1],'gary')

# # elif list1[1]==dic['bob']:
# #     print(list1[1],'bob')
# # else:
# #     print(list1[1],'Jeff')






# # # else:
# # #     print()





# # # list1=list(set(list1))
# # # list1.sort()


# # # print nos 10-20 
# # i=20
# # while (i>=10):
# #     print(i)
# #     i-=1
# # print()


# # n=int(input('Enter no '))

# # while(n>=0):
# #     print(n)
# #     n-=1

# # l=[10,20,30,40,4,3,5,6]

# # l=[1,2,3,4,5,6,7,8,9]
# # even=0
# # odd=0
# # for i in l:
# #     if i%2==0:
# #         even+=i
# #     else:
# #         odd+=i
# # print("even ",even,"Odd",odd)

# # for x in range(10,0,-1):
# #     print(x,end=" ")
# # print('\n')
# # for x in range(10,-1,-1):
# #     print(x,end=" ")

# # for i in range(0,10):
# #     if(i%2==0):
# #         print(i)


# # for i in range(15,35):
# #     if(i%2!=0):
# #         print(i)

# # l=[]
# # for i in range(13,50):
# #     if(i%2!=0):
# #         l.append(i)
# # print(l) 
# # for i in range(len(l)-1,-1,-1):
# #     print(l[i])


# # l=[1,3,6,7,9]
# # for i in range(len(l)):
# #     print(l[i])

# l=list(range(1,10))
# even_index=[]
# odd_index=[]
# even=[]
# odd=[]
# for i in range(len(l)):
#     if(i%2==0):
#         even_index.append(l[i])
#     else:
#         odd_index.append(l[i])
#     if(l[i]%2==0):
#         even.append(l[i])
#     else:
#         odd.append(l[i])
# print("Even_Index ",even_index,"\nOdd_index ",odd_index)
# print("even ",even,"\nOdd",odd)
    






# l=[1,2,3,4,1,2,3,4,1,2,3,4]
# un=[]

# for i in l:
#     if l.count(i)>=2:
#         l.remove(i)
# print(l)





# nested Loop 
# i=0
# while(i<=6):
#     j=0
#     while(j<=5):
#         print("* ",end=" ")
#         j+=1
#     print()
#     i+=1

# l=[2,3,23,13,15,16,18,24,56,20,11]
# for i in l:
#     f=1
#     for j in range(2,i):
#         if i%j==0:
#             f=0
#     if f==1:
#         print(i)


    # print list of primr nos between 25- 100
# for i in range(25,100):
#     f=1
#     for j in range(2,i):
#         if i%j==0:
#             f=0
#     if f==1:
#         print(i,end=" ")

# c=0
# for i in range(10,50):
#     f=1
#     for j in range(2,i):
#         if i%j==0:
#             f=0
    
#     if (f==1):
#         c+=1
#         if(c>7):
#             break
#         print(i,end=" ")



# z=65    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(z),end=" ")
#         z+=1
#     print()

# z=65
# for i in range(5,-1,-1):
#     for j in range(i):
#         print(chr(z),end=" ")
#         z+=1
#     print()







'''
#String 
    collection of hetrogenous data,
    which is indexed or ordered
    which is immutable
    it allow duplicated values
    elements written in quotes('',"",""" """,''' ''',)
    anything written in qoutes is string
'''
s="lavanya"
print(s)
print(type(s))
print(len(s))


