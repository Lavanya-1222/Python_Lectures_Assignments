# 

# no=int(input("enter no: "))
# if(no%2==0):
#     print("even")
# else:
#     print("Odd")


# # no=int(input('enter your score '))

# # if(no>=75):
# #     if(no<=100):
# #         print('A')
# # else:
# #     if(no>=30):
# #         if(no<75):
# #             print('B')
# #     else:
# #         print('C')


# no=int(input("enter no"))

# if(no>=0):
#     if(no==0):
#         print('zero')
#     else:
#         print("positive")
# else:
#     print('Negative')

# w=int(input("Enter No "))

# if(w<100):
#     if(w<=50):
#      print("Underwight")
#     else:
#      print("Notmal weight")
# else:
#     print("overwight")

l=[20,21,23,24,26,25,27,29,30]
i=0
even=[]
odd=[]
while(i<len(l)):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
    i+=1
print(even)
print(odd)