# 1. A student needs to know if they passed their exam. Write a program that checks their score and prints "Pass" if it is 40 or more, otherwise "Fail."  
# score=int(input("enter score "))
# if score>=40:
#     print("Pass")
# else:
#     print("Fail")

# 2. A store gives a 10% discount if the purchase is above $100 and a 20% discount if it is above $200. Write a program to calculate the final bill after applying the discount. 
# bill=int(input("enter bill "))
# if bill>=100 and bill<=200:
#     print(f"Total bill ${bill}  dicount of 10% is ${bill-(bill*(1/10))}")
# elif bill>200:
#     print(f"Total bill ${bill}  dicount of 10% is ${bill-(bill*(1/5))}")

 
# 3. A movie theater offers different ticket prices: $10 for children, $15 for adults, and $12 for seniors. Write a program to calculate the ticket price based on the age of the customer.
# age=int(input("Enter age "))
# if age<18:
#     print('Ticket Price is $10')
# elif age in range(18,60):
#     print('Ticket Price is $15')
# elif age>65:
#     print('Ticket Price is $12')


# 4. A farmer wants to check if a crop needs watering. If the temperature is above 30°C and humidity is below 40%, print "Water Needed," otherwise print "No Water Needed."  
# temp=int(input("Enter temprature "))
# humidity=int(input("Enter humidity percentage "))
# if temp>30 and humidity<40:
#     print("Water Needed")
# else:
#     print("Water not needed")


# 5. Write a program to classify a number as positive, negative, or zero.  
# n=int(input("enter no "))
# if n<0:
#     print("Negative")
# elif n>0:
#     print("Positive")
# else:
#     print("Zero")


# 6. A company gives bonuses based on years of service: 5% for less than 5 years, 10% for 5-10 years, and 20% for more than 10 years. Write a program to calculate the bonus.  
# ex=int(input("enter experience "))
# ctc=int(input("enter your CTC "))
# if ex<5:
#     print(f"You got Bonus of {ctc*5/100}")
# elif ex in range(5,11):
#     print(f"You got Bonus of {ctc*1/10}")
# elif ex>10:
#     print(f"You got Bonus of {ctc*1/5}")

# 7. A travel agency offers discounts on train tickets: 5% for students, 10% for senior citizens, and no discount otherwise. Write a program to calculate the final ticket price.  
# age=int(input("enter Your age "))
# t=100
# if age<25:
#     print(f"Ticket price {t-t*5/100}Rs")
# elif age>60:
#     print(f'Ticket Price {t-t*1/10}Rs')
# else:
#     print(f'Ticket Price {t}Rs')


# 8. A food delivery app charges $5 for delivery. If the order amount is above $50, delivery is free. Write a program to calculate the total cost.  
# amt=int(input("Enter amount "))
# if amt>50:
#     print(f"Total Cost {amt}")
# else:
#     print(f"Total Coset {amt+amt*5/100}Rs")


# 9. Write a program to check if a year is a leap year. A year is a leap year if it is divisible by 4 but not divisible by 100, except if it is divisible by 400.  
# year=int(input('Enter year '))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year,'is leap year')
#         else:
#             print(year,'Not leap year')
#     else:
#         print(year,'is leap year')


# 10. A car rental service charges $20 per day. If the customer rents for more than 7 days, they get a $50 discount. Write a program to calculate the total rental cost.
# days_rent=int(input("Enter days to taken car "))
# if days_rent>7:
#     print(f"Total rental cost {days_rent*20-50}Rs")
# else:
#     print(f"Total rental cost {days_rent*20}Rs")


# 11. A gym offers membership discounts: 10% for students, 15% for teachers, and no discount otherwise. Write a program to calculate the membership fee.  
# m_price=1000
# cu=input("please enter yes is your student enter tea if your teacher othervise enter other ")

# if cu=='yes':
#     print(f'Membership fee {m_price-m_price*1/10}' )
# elif cu=='tea':
#     print(f'Membership fee {m_price-m_price*15/100}' )
# elif cu=='other':
#     print(f'Membership fee {m_price}' )



# 12. A bank offers loans at different interest rates: 5% for loans under $50,000, 4% for loans between $50,000 and $100,000, and 3% for loans above $100,000. Write a program to calculate the interest amount. 
# loan_amount=int(input("Enter loan amount "))
 
# if loan_amount<50000:
#    print(f"Monthly Total interest is {loan_amount*5/100}")
# elif loan_amount in range(50000,100001):
#     print(f'"Monthly Total interest is {loan_amount*4/100}')
# elif loan_amount>100000:
#     print(f'"Monthly Total interest is {loan_amount*3/100}')


# 13. A restaurant categorizes its menu based on cuisine: Indian, Italian, or Chinese. Write a program that asks the user for their choice and prints the respective menu.  
# ch=input("Enter your country ")
# if ch.lower()=='india':
#     print(['Dal-Chwal','Rice','Biryani','Panner'])
# elif ch.lower()=='italian':
#     print(['soup','noodles','Sushi'])
# elif ch.lower()=='chinese':
#     print(['magge','haka-noodles','fried-egges'])

# 14. Write a program to check if a person is eligible to vote. The minimum voting age is 18 years.  
# v=int(input("Enter age "))
# if v>=18:
#     print("Your Eligible for vote")
# else:
#     print("You not eligible for vote")


#  15. A person wants to buy a mobile phone. If the phone's price is within their budget, print "Affordable," otherwise print "Expensive."  
# p=20000
# ch=int(input("Please enter your budget "))
# if ch>=p:
    
#     print("Affordable")
# else:
#     print("Expensive")


# 16. A grading system assigns grades based on marks: A for 90 and above, B for 80-89, C for 70-79, D for 60-69, and F for below 60. Write a program to determine the grade.  
# grade = int(input("Enter grade "))
# if grade>=90:
#     print('A')
# elif grade in range(80,90):
#     print('B')
# elif grade in range(70,80):
#     print('C')
# elif grade in range(60,70):
#     print('D')
# elif grade<60:
#     print('F')

# 17. Write a program to check if a triangle is equilateral, isosceles, or scalene based on the lengths of its three sides.
# s1=int(input("Enter side 1 of Triangle "))
# s2=int(input("Enter side 2 of Triangle "))
# s3=int(input("Enter side 3 of Triangle "))
# if s1==s2 and s1==s3 and s2==s3:
#     print("Tiangle is Equlator")
# elif s1==s2 or s2==s3 or s1==s3:
#     print("Triangle is Isosceles")
# elif s1!=s2 and s1!=s3 and s2!=s3:
#     print("Triangle is scalene")


# 18. A weather app categorizes the weather as "Cold" if the temperature is below 15°C, "Warm" if it is between 15°C and 25°C, and "Hot" if it is above 25°C. Write a program to determine the weather.  
# temp=int(input("Enter temprature "))
# if temp<15:
#     print('Cold')
# elif temp in range(15,26):
#     print("Warm")
# else:
#     print("Hot")


# 19. A library charges a late fee of $1 per day for the first 5 days, $2 per day for the next 5 days, and $5 per day after 10 days. Write a program to calculate the fine based on the number of late days.  
# days=int(input("Enter your late days "))
# if days<=5:
#     print(f"Total Charges are {days*1}Rs")
# elif days>5 and days<=10:
#     print(f"Total Charges are {days*2}")
# elif days>10:
#     print(f"Total charges are {days*5}")



# 20. A company offers a salary increment based on performance ratings: 20% for "Excellent," 10% for "Good," and no increment for "Average." Write a program to calculate the new salary.
# sal=int(input("Enter salary "))
# rat=input('Enter your Rating ')
# if rat.lower()=='excellent':
#     print("Total Salary",sal+sal*1/5)
# elif rat.lower()=='good':
#     print("Total Salary",sal+sal*1/10)
# elif rat.lower()=='average':
#     print("Total Salary",sal)
