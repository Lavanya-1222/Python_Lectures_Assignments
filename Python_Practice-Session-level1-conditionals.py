# Q1) Check the given no by user is even or odd 
# n=int(input("Enter no "))
# if n%2==0:
#     print(n,"Even")
# else:
#     print(n,'Odd')


# Q2) Check the given no by user is divisible by 5 or not
# n=int(input("Enter no "))
# if n%5==0:
#     print(n,'Is divisble by 5')
# else:
#     print(n,'Is not divisble by 5')

# Q3) Check the given no by user is divisible by 5 and 10 or not
# n=int(input("Enter no "))
# if n%5==0 and n%10==0:
#     print(n,'Is divisble by 5 and 10 ')
# else:
#     print(n,'Is not divisble by 5 and 10')


# Q4) Check the given age by user is adult or not
# age=int(input("Enter age "))
# if age>=18:
#     print("Adult")
# else:
#     print("Not Adult")

# Q5) Check the given no by user is between 40 and 100 or not
# n=int(input("enter no "))
# if n in range(40,100):
#     print("In Range")
# else:
#     print("Not in Range")


# Q6) Print WOOW if score given by user is between 75 to 100 else BOO
# s=int(input("enter acore "))
# if s in range(75,100):
#     print("WOOW")
# else:
#     print("BOO")

# Q7) Print Perfect if no 1 ;Good if no is between 0.9 to 0.6 ;Fine if 0.5;Poor if else than 0.5 and greater than 0    
# n=float(input("Enter no "))
# if n==1:
#     print("Perfect")
# elif n>=0.6 and n<=0.9:
#     print('Good')
# elif n>0 or n<0.5:
#     print("Poor")

# Q8) Find the elder of two brothers Tim and Jim whose ages are given by user.
# tim=int(input("enter age of tim"))
# jim=int(input("enter age of jim"))
# if tim>jim:
#     print("Tim is Elder")
# else:
#     print("Jim is Elder")

# Q9) Find the youngest of two sisters Ana and Mary whose ages are given by user.
# Mary=int(input("enter age of mary "))
# Ana=int(input("enter age of Ana "))
# if Mary<Ana:
#     print("Mary is Older")
# else:
#     print("ana is Older")


# Q10) Print the Grade of student for given percentage (A(75-100),B(60-75),C(50-60),D(40-50),F(s<40))
# grade=int(input("enter student grades "))

# if grade>=75 and grade<=100:
#     print("A")
# elif grade>=60 and grade<=74:
#     print("B")
# elif grade>=50 and grade<=59:
#     print("C")
# elif grade>=40 and grade<=49:
#     print("D")
# elif grade<40:
#     print("Fail")


# Q11) Print the greatest of 3 nos given by user.
# n1=int(input("enter no1 "))
# n2=int(input("enter no2 "))
# n3=int(input("enter no3 "))
# if n1>n2 and n1>n3:
#     print(n1, 'greatest')
# elif n2>n1 and n2>n3:
#     print(n2,'Greatest')
# else:
#     print(n3,'Greatest')

# Q12) Print the smallest of 3 nos given by user.(using nest conditionals(nested if-else))
# n1=int(input("enter no1 "))
# n2=int(input("enter no2 "))
# n3=int(input("enter no3 "))
# if n1<n2 and n1<n3:
#     print(n1, 'Smallest')
# elif n2<n1 and n2<n3:
#     print(n2,'Smallest')
# else:
    # print(n3,'Smallest')

# Q13) Check the temprature given by user is for which season
#      (spring(15-30 °C), summer(30+ °C), autumn(0-10 °C), and winter( 10–15 °C))
# temp=int(input("Enter Temprature "))
# if temp in range(15,31):
#     print("Spring")
# elif temp>30:
#     print('Summer')
# elif temp in range(0,10):
#     print('Autumn')
# elif temp in range(10,15):
#     print('Winnter')


# Q14) Jacob always choose the middle(favraoute) one of 3 nos given what will that no.
#      Ask Jacob to give three no and tell his favroute no.
# n1=int(input("Enter no1 "))
# n2=int(input("Enter no2 "))
# n3=int(input("Enter no3 "))
# if (n1<n2 and n1>n3) or (n1>n2 and n1<n3):# 20,10,30 #20 30 10
#     print("Faviroute no is ",n1)
# elif (n2<n1 and n2>n3) or (n2>n1 and n2<n3):
#     print("Faviroute number is",n2)
# else:
#     print("Faviroute number is",n3)


# Q15) Alice is trying to find a no which is non negative and even and divisble by 3 given by 
#      Alice Tell Alice the no is right or not
# n=int(input("enter no "))
# if n>0 and n%2==0 and n%3==0:
#     print("Right number ")
# else:
#     print("Not right ")


# Q16) Write a program to print Yes if no which is odd and between 10 to 15 and divisible by 4 given by user
# n=int(input("enter no "))
# if n%2!=0 and n in range(10,15) and n%4==0:
#     print("Yes")
# else:
#     print('no')


# Q17) Write a program to check the input nos. given by Jeff and Bob are same or not for same "Won" else "Lost"
# jeff=int(input("Enter no by jeff "))
# bob=int(input("enter no by bob "))
# if jeff==bob:
#     print("Won")
# else:
#     print('Lost')


# Q18) Create a program using nested if-else where the player chooses between "tea" or "coffee," 
#      and then chooses "hot" or "cold" to get a final drink suggestion.
# ch=input("Enter your choice ")
# if ch=='tea' or ch=='coffee':
#     d=input("Enter cjhoice hot or cold ")
#     if d=='hot' and ch=='tea':
#         print("Take Masala Tea")
#     elif d=='cold' and ch=='coffee':
#         print("Take Cold Coffee ")
#     elif d=='hot' and ch=='coffee':
#         print("Take Capechino ")
#     elif d=='cold' and ch=='tea':
#         print("Take Ice tea")

# Q19) Write a program to print youngest middle and eldest of three Employees given by HR.
# e1=int(input("Enter employyee 1 ")) 
# e2=int(input("Enter employyee 2 "))
# e3=int(input("Enter employyee 3 "))

# if e1>e2 and e1>e3:
#     print(e1,"e1 is oldest")
# elif e2>e1 and e2>e3:
#     print(e2,"e2 is Oldest")
# else:
#     print(e3,'e3 is Oldest')

# if (e1>e2 and e2<e3) or (e1>e3 and e1<e2):
#     print(e1,"e1 is Middlest")
# elif (e2>e1 and e2<e3) or (e2>e3 and e2<e1) :
#     print(e2,'e2 is Middlest')
# else:
#     print(e3,'e3 is Middlest')

# if e1<e2 and e1<e3:
#     print(e1,"e1 is Youngest")
# elif e2<e1 and e2<e3:
#     print(e2,"e2 is Youngest")
# else:
#     print(e3,'e3 is Youngest')

    

# Q20) Write a Python program that takes the user's age and income as input and determines if they 
#      qualify for a loan based on these rules:

#    If the age is less than 18, print "Not eligible for a loan."
#    If the age is between 18 and 60:
#       If the income is less than 20,000, print "Eligible for a basic loan."
#       If the income is between 20,000 and 50,000, print "Eligible for a standard loan."
#       If the income is above 50,000, print "Eligible for a premium loan."
#    If the age is above 60:
#     If the income is less than 30,000, print "Eligible for a senior citizen basic loan."
#     If the income is 30,000 or more, print "Eligible for a senior citizen premium loan."
# age=int(input("enter age "))
# income=int(input("Enter income "))
# if age<18:
#     print("Not eligible for a loan.")
# elif age>=18 and age<=60:
#     if income <20000:
#         print('Eligible for a basic loan.')
#     elif income>=20000 and income<=50000:
#         print('Eligible for a standard loan.')
#     elif income>50000:
#         print('Eligible for a premium loan.')
# elif age>60:
#     if income<30000:
#         print('Eligible for a senior citizen basic loan.')
#     elif income>=30000:
#         print('Eligible for a senior citizen premium loan.')