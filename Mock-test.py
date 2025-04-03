#  A string containing consecutive repeated characters, e.g., "aaabbccccdde".  
#    Output: A compressed version of the string where each character is followed by the count of consecutive occurrences, e.g., "a3b2c4d2e1".
"""
s=input("Enter string ")
start_chr=s[0]
c=0
result=''
for i in s:
    if i==start_chr:
        c+=1
    else:
        result=result+start_chr+str(c)
        start_chr=i
        c=1
result+=start_chr+str(c)
print(result)
"""


# Section C: Correct the Code (10 Questions)

# 1. Code:
   
x = 10
y = 5
if x > y:
     print("x is greater than y")
   
# Task: Fix the syntax error in the code.

# 2. Code:  
#    name = "Alice"
#    age = 30
#    print("My name is {} and I am {} years old.".format(name, age))
   
#    Task: Rewrite the code using an f-string to format the string.
# ANS:
name = "Alice"
age = 30
print(f"My name is {name} and I am {id} years old.")


# 3. Code:
fruits = ["apple", "banana", "cherry"]
#    print(fruits[3])
#    Task: Correct the code to print the last element of the list.
# ANS: 
print(fruits[2])


# 4. Code:
#    number = 12
#    if number > 10
#        print("Greater than 10")
#    elif number == 10
#        print("Equal to 10")
#    else:
#        print("Less than 10")
   
#Task: Fix the syntax error in the conditional statement.
number = 12
if number > 10:
       print("Greater than 10")
elif number == 10:
       print("Equal to 10")
else:
       print("Less than 10")


# 5. Code:  
#    a = 5
#    b = 10
#    print(f"Sum of a and b is: {a + b}")
   
#    Task: Explain why this code is correct and what the f-string does here.
# ANS: in f string we can give expresion also hence we not got error 


# 6. Code:   
age = 18
if age >= 18:
       print("You are an adult")
else:
       print("You are a minor")
   
#    Task: Fix the indentation issue in the code.
# 7. Code:
   
x = "10"
y = 5
print(int(x) + y)
   
#    Task: Correct the type error so that the program adds the two values as numbers.
# 8. Code:
num = 0
if num > 0:
       print("Positive number")
elif num < 0:
       print("Negative number")
else:
       print("Zero")
   
#    Task: Correct the code to print whether the number is positive, negative, or zero correctly.
# 9. Code:
colors = ("red", "green", "blue")
# colors[1] = "yellow"
colors=list(colors)
colors[1]='yellow'
print(colors)
   
#    Task: Correct the code to show how tuples work with immutability
# 10. Code:
    
fruits = ["apple", "banana", "cherry"]
#     print(fruits["banana"])
    
#     Task: Fix the issue and explain how to access list elements by index.
# ANS:
# list index starts from 0 
print(fruits[1])
