# 1. Right-Angled Triangle of Numbers  
# Create a right-angled triangle where each row contains increasing numbers from 1 to the current row number.  
# Example for N=5:  

# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


print()

# 2. Inverted Right-Angled Triangle of Numbers  
# Generate an inverted right-angled triangle where each row starts from the highest number and decrements.  
# Example for N=5:  

# 12345
# 1234
# 123
# 12
# 1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()



# 3. Pyramid of Numbers  
# Create a pyramid pattern with increasing numbers that also mirror themselves in each row.  
# Example for N=4:  

#    1
#   121
#  12321
# 1234321
n=4
for i in range(1,5):
    for s in range(n-i):
        print(" ",end="")
    for c in range(1,2*i):
        print(c,end="")
    print()
    


print()
# 4. Number Square  
# Generate a square of numbers where each row contains the same number repeated N times.  
# Example for N=4:  

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
for i in range(1,5):
   for j in range(1,5):
       print(i,end=" ")
   print()
       


print()
# 5. Hollow Square of Numbers  
# Create a hollow square where the borders are filled with numbers and the inside is empty.  
# Example for N=5:  

# 1 1 1 1 1
# 1       1
# 1       1
# 1       1
# 1 1 1 1 1
for i in range(1,6):
    if i==1 or i==5:
        for j in range(5):
           print(1,end=" ")
    else:
        for j in range(5):
            if j==0 or j==4:
                print(1,end=" ")
            else:
                print(" ",end=" ")
    print() 



print()
# 6. Inverted Pyramid of Numbers  
# Generate an inverted pyramid where numbers decrement in each row.  
# Example for N=5:  

# 12345
# 1234
# 123
# 12
# 1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()



# 7. Half Diamond of Numbers  
# Create a half-diamond pattern with numbers.  
# Example for N=4:  
print()
# 1
# 12
# 123
# 1234
# 123
# 12
# 1

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(3,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()



# 8. Number Rhombus  
# Generate a rhombus shape where numbers increase in the first half and decrease in the second half.  
# Example for N=4:  

#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1

r=0 #2
for i in range(1,6):
    for s in range(6-i):
      print(" ",end="") 
    for c in range(1,2*i): 
        if c<=i:
            print(c,end="")
            r+=1