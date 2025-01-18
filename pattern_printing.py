print('--------------inclined line--------------')
n=int(input("Enter no "))
for i in range(n):
    for j in range(i+1):
        if j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print('--------------X - pattern--------------') 
n=int(input("enter no "))
for i in range(n):
         for j in range(i+1):
           if j==i:
            print("*",end=" ")
           else:
            print(" ",end=" ")
         print() 
