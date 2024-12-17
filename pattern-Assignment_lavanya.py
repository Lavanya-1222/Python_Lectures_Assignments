
# Write the programs to print the given patterns

# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=" ")
    print()




# *****
# ****
# ***
# **
# *
for i in range(3,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


print()
# 1
# 12
# 123
# 1234
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()



print()
# 1234
# 123
# 12
# 1 
# 

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()	


print()
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
for i in range(1,6):
    for s in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print('*',end="")
    print()



# *
# **
# ***
# ****
# ****
# ***
# **
# *
print("---------------")
len=8
z=1
for i in range(len):
    if(i<=(len//2-1)):
        for j in range(i+1):
            print('*',end="")
        
    if(i>(len//2-1)):
        for k in range(len-i,0,-1):
            print('*',end="")
        
               
    print()




# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('-------------------------------------')
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()


# 1
# 12
# 123
# 1234
# 1234
# 123
# 12
# 1
print('-------------------------------------')
for i in range(len):
    if(i<=(len//2-1)):
        for j in range(1,i+1+1):
            print(j,end="")
        
    if(i>(len//2-1)):
        for k in range(1,len+1-i):
            print(k,end="")
        
               
    print()
print('-------------------------------------')
'''
*
* #
* # *
* # * #
* # * # *
'''
for i in range(6):
    for j in range(i):
        if(j%2==0):
            print('*',end=' ')
        else:
            print('#',end=' ')
    print()

  


# Patterns-Assignment.txt
# Displaying Patterns-Assignment.txt.