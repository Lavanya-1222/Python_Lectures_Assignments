# All posible substrings 'abc'->a,ab,abc,b,bc,case

s='abc'
l=[]
# for i in range(len(s)):
#     sub=''
#     for j in range(i,len(s)):
#         sub=s[i:j+1]
#         l.append(sub)
# print(l)
for i in range(len(s)):
    a=''
    for j in range(i,len(s)):
        a+=s[j]
        l.append(a)
print(l)

# 2)----- Lambda function with for loop

#3)leap year

# 4)fibo using recurtion

# 5) Write a Python program that takes a list of tuples, sorts them based on the second element of each tuple using a lambda function, and prints the result.
# l=[(10,20),(30,40),(50,1),(60,2)]
# print(sorted(l,key=lambda l:l[1]))

#6) Use a nested loop to create the following pattern:
# *  
# * *  
# * * *  
# * *  
# * 

# 7)#17 Write a recursive function to compute the sum of all elements in a nested list (e.g., [[1, 2, [3, 4]], 5]).