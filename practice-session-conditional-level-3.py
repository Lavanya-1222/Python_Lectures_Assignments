# 1.  Write a program to check if a given character is a vowel, a consonant, or neither (e.g., numbers or special characters) using nested if-else statements. 
# c=input("Enter Charecter ")
# if c in 'aioueAIOUE':
#     print("Charecter is Vowel")
# elif c not in 'aioueAIOUE' and c not in '123456789' and c not in '!@#$%^&*()-~':
#     print("Charecter is consonant")
# elif c.isdigit():
#     print("Charecter is number")
# elif c in '!@#$%^&*()-~':
#     print("Charecter is specail charecter ")

# sol-2
# if c.isalpha():
#     if c in 'aioueAOIUE':
#         print("Vowel")
#     else:
#         print("Consonant")
# elif c.isdigit():
#     print("Number")
# else:
#     print("Special Charecter ")
    

# 2.  Write a program to check in which quadrant a point (x, y) lies, or if it is on the X-axis, Y-axis, or the origin.
# x,y=int(input("Enter x point")),int(input("Enter y point"))
# if x==0 and y==0:
#     print("Point lies on Origin")
# elif x==0 and y>0:
#     print('Point lies on y-axis')
# elif x>0 and y==0:
#     print('point on x axis')



# 3.  Write a program to classify a given angle as acute, right, obtuse, or straight using if-elif-else. 
# ang=int(input("Enter "))

# if ang==90:
#     print('Right angle')
# elif ang<90:
#     print("Acute angle")
# elif ang>90 and ang<180:
#     print("Obtuse angle")
# elif ang==180:
#     print("Straight angle")



# 4.  Write a program to calculate the income tax based on the income entered by the user, using the following tax slabs:
# Income up to ₹2,50,000: No tax
# Income between ₹2,50,001 and ₹5,00,000: Tax rate is 5%
# Income between ₹5,00,001 and ₹10,00,000: Tax rate is 20%
# Income above ₹10,00,000: Tax rate is 30%
# income=int(input("enter your income "))
# if income<=250000:
#     print("no tax for you ")
# elif income in range(250001,500001):
#      tax=(income-250000)*0.5  
#      print("Your Tax",tax)
# elif income in range(500001,1000001):
#     r=income-250000
#     s=(250000)*(5/100)
#     k=(r-250000*20/100)
#     print("Tax",k+s)
# elif income>1000000:
#     r=income-250000
#     s=250000*(1/5)
#     k=(income-500000*30/100)
#     k=("Tax",k+s)


# 5. 
# Write a program that categorizes the input temperature (in degrees Celsius) into one of the following:
# Freezing: Below or equal to 0°C
# Cold: Greater than 0°C and less than 10°C
# Warm: Greater than or equal to 10°C and less than 25°C
# Hot: Greater than or equal to 25°C
# temp=int(input("Enter Temmprature "))
# if temp<=0:
#     print("Freezing")
# elif temp>0 and temp<10:
#     print("Cold")
# elif temp>=10 and temp<25:
#     print("Warm")
# elif temp>=25:
#     print("Hot")


# 6. Write a program where the user inputs the weather condition (e.g., "sunny", "rainy", "snowy"). Based on the input, suggest an activity:
# If it's sunny, suggest going for a picnic.
# If it's rainy, suggest staying indoors and reading a book.
# If it's snowy, suggest building a snowman.
# s=input("Enter Weather").lower()
# if s=='sunny':
#     print("Picnic")
# elif s=='rainy':
#     print('staying indoors and reading a book.')
# elif s=='snowy':
#     print('building a snowman')


# 7. Write a program that asks the user for their destination (e.g., "beach", "mountains", "city"). Based on the destination, suggest what to pack:
# If they choose the beach, suggest sunscreen and swimwear.
# If they choose the mountains, suggest hiking boots and warm clothing.
# If they choose the city, suggest comfortable walking shoes and a camera.
# d=input("Enter your designation ").lower()
# if d=='beach':
#     print('sunscreen and swimwear')
# elif d=='mountains':
#     print('hiking boots and warm clothing')
# elif d=='city':
#     print('comfortable walking shoes and a camera')


# 8. Holiday Activity Planner: Based on the day of the week, decide the activity:
# Monday–Friday: Go to work.
# Saturday: Go shopping.
# Sunday: Relax at home.
# Write a program that takes the day of the week as input and prints the planned activity.
# day=input("Enter Day of week ").lower()

# if day in ['monday','tuesday','wednessday','thursday','friday']:
#     print("Go to work")
# elif day=='saturday':
#     print("Go to Shopping")
# elif day=='sunday':
#     print("Relax at Home")


# 9. Write a program that suggests a meal based on the time of day entered by the user (e.g., "morning", "afternoon", "evening", "night").
# If the input is morning, suggest having breakfast.
# If it's afternoon, suggest having lunch.
# If it's evening, suggest a light snack.
# If it's night, suggest having dinner.
# timing=input("Enter timing of day ").lower()

# if timing=='morning':
#     print("Take breakfast")
# elif timing=='afternoon':
#     print('Take lunch')
# elif timing=='evening':
#     print("Take snack")
# elif timing=='night':
#     print("Take dinner")


# 10. Age Group Classification:
# Write a program to classify a person based on their age:
# 0–12 years: Child
# 13–19 years: Teenager
# 20–59 years: Adult
# 60+ years: Senior Citizen
# age=int(input("Enter age "))
# if age in range(0,13):
#     print("your Child")
# elif age in range(13,20):
#     print("Your Teenage")
# elif age in range(20,60):
#     print("Your Adult")
# elif age>=60:
#     print("yor Senior")

# 11. Traffic Light System:  A traffic light changes color:
# 	Green: Proceed.
# 	Yellow: Slow down.
# 	Red: Stop.
#     Write a program that takes the traffic light color as input and prints the action.
# t_light=input("Enter Traffic light ").lower()
# if t_light=='green':
#     print('Proceed')
# elif t_light=='yellow':
#     print("Slow down")
# elif t_light=='red':
#     print("Stop")


# 12. Fitness Plan: A fitness coach recommends exercises:
# If the user’s BMI is above 25, recommend weight loss exercises.
# If the user’s BMI is between 18.5 and 25, recommend maintaining their current routine.
# If the user’s BMI is below 18.5, recommend gaining muscle mass.
# Write a program that takes the user's BMI as input and prints the recommendation.
# bmi=float(input("Enter your BMI "))
# if bmi>25:
#     print('do weight loss exercises')
# elif bmi>=18.5 and bmi<=25:
#     print('Please  maintaining your  current routine.')
# elif bmi<18.5:
#     print('gaine  muscle mass.')


# 13. Bank ATM Withdrawal
#  An ATM must process withdrawals:
# Check if the withdrawal amount is a multiple of 100.
# Check if the withdrawal amount exceeds the account balance.
# Otherwise, allow the withdrawal.
# Task: Write a program to handle these conditions. 
# amount=int(input("Enter amount "))
# bal=1000
# if amount%100==0 and amount<bal:
#     print("Yor balance",bal-amount)
# elif amount%100!=0:
#     print("Please enter amount in multiple of 100 ")
# elif amount>bal:
#     print("Insuffient balance")


# 14.  Password Strength Checker A password is considered strong if:
# Its length is at least 8 characters.
# It contains both uppercase and lowercase letters.
# It has at least one digit.
# If it satisfies all criteria, print Strong Password.
# If any criteria fail, print which criteria failed.
# pws=input("Enter your password ")
# if len(pws)>=8:
#    if any(filter(lambda x:x.islower(),pws))  and any(filter(lambda x:x.isupper(),pws)) and any(filter(lambda x:x.isdigit(),pws)) and any(filter(lambda x: x in '!@#$%^&*()_-',pws)):
#        print("yes")   
#    else:
#        print("criteria failed")
       
# else:
#     print("criteria failed")


# 15. Password Validator 
# A user is trying to log in. The program must:
# Check if the username is correct.
# If the username is correct, check the password.
# If the username is incorrect, display an error message.
# Task: Write a program to validate the username and password using nested if.
# d={'nitish':'lava@2203'}
# usr=input("Enter user name ")
# pwd=input("Enter password ")
# if usr in d.keys():
#     if d[usr]==pwd:
#         print("Login succesfull ")
#     else:
#         print('password is incorrect')
# else:
#     print("Login failed ")


# 16. Student Result Analysis: Given a student’s scores in three subjects:
# Check if the student passed:
# A subject is passed if the score is ≥ 35.
# The student must pass all subjects to be declared Pass.
# If the student passed, check:
# If the average score is ≥ 90, print Distinction.
# If the average is between 60 and 89, print First Class.
# Otherwise, print Second Class.
# If the student failed in any subject, print Fail.
# scores=list(map(int,input("Enter student scores ").split(" ")))
# sum=0
# f=0
# for i in scores:
#     if i>=35:
#         sum+=i
#     else:
#         print("Student Failed ")
#         f=1
#         break
# avg=sum/3
# if f==0:
#  if avg>=90:
#     print("Distinct")
#  elif avg in range(60,90):
#     print("First class")
#  elif avg in range(35,60):
#     print("Pass")


# 17.  Car Loan Eligibility: 
#  A car loan eligibility system checks:
# If the person is employed:
# If the annual salary is more than ₹5,00,000, they are Eligible.
# Otherwise, check if they have a guarantor.
# If yes, they are Eligible with guarantor.
# If no, they are Not eligible.
# If the person is unemployed, they are Not eligible.
# status=input("enter yes if you employed ")


# if status=='yes':
#     sal=int(input("enter your salary "))
#     if sal>500000:
#         print("your eligible ")
#     elif input("Enter yes if you have gaurantor ")=='yes':
#         print("ypur eligible with guarantor")
#     else:
#         print("Your not eligible")
# else:
#     print("your not eligible")

    
        

# 18.  Quiz Scoring System: A quiz competition scores participants based on:
# If the participant’s score is greater than 90, they win a Gold medal.
# If the score is between 75 and 90:
# Check if they answered all bonus questions correctly:
# If yes, they win a Silver medal.
# Otherwise, a Bronze medal.
# If the score is below 75, print Better luck next time.
# yes=input("Enter yes if you answered all bonus quetions currectly ")
# score=int(input("enter your score"))
# if score>90:
#     print("Won the Gold medal")
# elif score in range(75,91):
#     if yes=='yes':
#         print('won Silver medal')
#     else:
#         print("Won bronze medal")
# elif score<75:
#     print("Better luck next time")
    

# 19. Write a program to calculate electricity bills based on the following:
# If the total consumption (units) is less than 100, charge ₹5 per unit.
# If the consumption is between 100 and 300:
# The first 100 units are charged at ₹5 per unit.->
# The remaining units are charged at ₹7 per unit.
# If the consumption exceeds 300:
# The first 100 units are charged at ₹5 per unit.
# The next 200 units are charged at ₹7 per unit.
# Any units above 300 are charged at ₹10 per unit.
# Finally, add a fixed surcharge of ₹50 to the total bill.
units=int(input("enter units of electricity "))

if units<100:
    print("Total bill",units*5+50)
elif units in range(100,301):
    t=((units-100)*7)
    print("Total units",100*5+t+50)
elif units>300:# 400->100*5->500->200*7->1400-->100*10-->1000
    t=200*7
    f=(units-300)*10
    print("Total bill",100*5+t+f+50)

# 20. Write a program to determine the grade of steel based on three properties (hardness, carbon content, tensile strength) using nested if-else.  
# A steel grade is determined by the following conditions:
# If the hardness > 50, carbon content < 0.7, and tensile strength > 5600, grade is 10.
# If only the first two conditions are met, grade is 9.
# If the first and last conditions are met, grade is 8.
# If only the last two conditions are met, grade is 7.
# If none of the conditions are met, grade is 6.
# hard,c_con,tensile_strength=tuple((map(float,input("hardness,carbal_content,tensile_strenth ").split(","))))

# if hard>50 and c_con<0.7 :
#     if tensile_strength>5600:
#         print("grade 10")
#     else:
#         print("grade 9")
# elif hard>50 and tensile_strength>5600:
#     print("grade 8")
# elif c_con<0.7 and tensile_strength>5600:
#     print("grade 7")
# else:
#     print("grade 6")


# 21. A student is eligible for an exam if their attendance is ≥ 75% ≥75%. Given the total classes held and attended, determine whether the student is eligible.
# total_class_held=100
# attented=int(input("Enter total class attended "))
# if (attented/100)*100>75:
#     print("Eligible ")
# else:
#     print("Not Eligible ")


# 22. Write a program to calculate and print whether a transaction resulted in a "Profit" or "Loss". Input the cost price and selling price.
# cost_price=int(input("enter cost price "))
# sell_price=int(input("Enter selling price "))
# if sell_price>cost_price:
#     print("Profit")
# else:
#     print("Loss")


# 23. Given three integers as sides of a triangle, determine if they can form a valid triangle: A triangle is valid if the sum of any two sides is greater than the third side.
# s1=int(input("enter side 1 "))
# s2=int(input("enter side 2 "))
# s3=int(input("enter side 3 "))

# if s1+s3>s2 or s2+s1>s3 or s2+s3>s1:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")


# 24. Given the age of a customer, determine the ticket price: Below 12 or above 60: ₹100., Everyone else: ₹200.
# age=int(input("enter your age "))
# if age<12 or age>60:
#     print('Ticket Price 100Rs')
# else:
#     print("ticket price 200Rs")


# 25. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# month=input("enter a month ").lower()

# if month in ['september','october','november']:
#     print('Autumn')
# elif month in ['january','february','december']:
#  print("Winter")
# elif month in ['march','april','may']:
#     print("Spring")
# elif month in ['june','july','august']:
#     print('Summer')
