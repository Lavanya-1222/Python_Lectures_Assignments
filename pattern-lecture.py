for i in range(5):
    for j in range(i+1):
        print('*',"(",i,j,")",end=" ")
    print()
# output
# * ( 0 0 ) 
# * ( 1 0 ) * ( 1 1 ) 
# * ( 2 0 ) * ( 2 1 ) * ( 2 2 )
# * ( 3 0 ) * ( 3 1 ) * ( 3 2 ) * ( 3 3 )
# * ( 4 0 ) * ( 4 1 ) * ( 4 2 ) * ( 4 3 ) * ( 4 4 )

for i in range(6):
    for j in range(i+1):
        print(i,end=" ")
    print()
# output:
# 0
# 1 1
# 2 2 2
# 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5 5
# for i in range(6):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()
# output:0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5

# z=1
# for i in range(4):
#     for j in range(i+1):
#         print(z,end=" ")
#         z+=1
#     print()
# output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# i=5
# while(i>0):
#     for j in range(i):
#         print('*',end=" ")
#     i-=1
#     print()
# output:
# * * * * *
# * * * *
# * * * 
# * *
# *

# n=5
# for i in range(5):
#     for j in range(n-i):
#         print('*',end=" ")
#     print()
# output:
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(1,n):
    for s in range(1,n-i):
        print(' ',end=" ")
    for j in range(i):
        print('*',end=" ")
    print()
