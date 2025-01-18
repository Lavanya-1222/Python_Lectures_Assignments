# 1. A library has a list of books with their respective ratings. Write a function to find the top-rated book. If multiple books have the same highest rating, return the first one alphabetically. Use appropriate data structures and a combination of lambda and sorted.
# d={'man':8,'frog':10,'mindset':4,'deepwork':10}
# max=max(d.values())
# l=[k for k,v in d.items() if v==max]

# print(sorted(l))
# output:
# ['deepwork', 'frog']
    

# 2. A chef is organizing ingredients stored in different categories. Write a program that takes two lists of categories and items, zips them together, and prints a sorted list of the items for each category using a loop.
# cat=['kiteche','Clothing','Acsseries']
# ite=['Mixer','T-Shirt','Ear-Rings']

# for i,v in zip(cat,ite):
#     print(i,v)
# output:
# kiteche Mixer
# Clothing T-Shirt
# Acsseries Ear-Rings



# 3. A game development company wants to evaluate player scores. Write a function that takes a list of player scores, removes the highest and lowest scores, and returns the average of the remaining scores. Ensure the function handles cases where there are fewer than three scores gracefully.
# l=[10,20,30,40,50,60]
# # l=[10,20]
# sum=0
# if len(l)<3:
#     for i in l:
#         sum+=i
#     avg=sum/len(l)
#     print("Avarage",avg)
# else:
#     l.sort()
#     for i in range(1,len(l)-1):
#         sum+=l[i]
#     print("Avrage",sum/(len(l)-2))

# output:
# Avrage 35.0  


# 4. A store has a weekly sale where the discount percentage depends on the day of the week. Write a program using zip to pair each day with its discount percentage and print the day with the highest discount.
# day=['Sun','Mon','Tues','Wed','Thur','Fri','Sat']
# sale=[50,10,10,20,34,0,40]
# max=0
# k=''

# for k,v in zip(day,sale):
#     if v>max:
#         max=v
#         d=k
# print(d,f'{max}% Sale')
# output
# sun 50% 


# 5. A sports coach needs to evaluate athletes' performance metrics. Write a program that uses a list of tuples, where each tuple contains an athlete's name and scores in three events. Use enumerate and a loop to find the athlete with the highest average score.
# l=[('merry',45,90,100),('john',68,90,67),('maria',20,30,400)]
# max=0
# ind=0
# favg=0
# for k,v in enumerate(l):
#     sum=0
#     for j in range(1,4):
#         sum+=v[j]
#     avg=sum/3
#     if avg>max:
#         max=avg
     
#         ind=k
#         print(ind)
# print(l[ind])
# output:('maria', 20, 30, 4000)


# 6. A gardener tracks the growth of plants each day. Write a program that takes a list of daily heights and calculates the maximum growth in one day, the total growth over a week, and the average growth. Use a combination of loops, functions, and eval.
# l=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,19,20]]
# maxi=[]
# sum=0
# le=0
# for i in l:
#     maxi.append(max(i))
#     for j in i:
#        sum+=j
#        le+=1
# print('Maximum Weekly Growth',maxi)
# print('Total_Growth',maxi[-1])
# print('Avrage grouth',sum/le)
# output:
# Maximum Weekly Growth [3, 6, 9, 12, 15, 18, 20]
# Total_Growth 20
# Avrage grouth 10.904761904761905

# 7. A teacher has a list of students and their test scores. Write a function using lambda and filter to find all students who scored above a certain threshold. Then, return their names and scores sorted by scores in descending order.
# l=[('A',67),('B',80),('c',76),('d',20),('e',30)]
# sum=0
# for i in l:
#     sum+=i[1]
# avg=sum/len(l)
# print(avg)
# # sorted(l,key=lambda x:x[1])
# print(list(filter(lambda x:x[1]>avg,l)))
# output:
# 54.6
# [('A', 67), ('B', 80), ('c', 76)]


# 8. A weather monitoring app stores daily temperatures in two lists: one for city A and one for city B. Write a program that uses zip to pair the temperatures and finds the day when the temperature difference between the two cities was the highest.
# A=[10,20,30,40,50,89,8]
# B=[100,90,67,8,9,10,-3]
# max=0
# i=1
# for a,b in zip(A,B):
#     if abs(a-b)>max:
#         max=abs(a-b)
#         d=i
#         i+=1
#     else:
#         i+=1
# print('day',d,'Hignest Temprature',max)
# output:
# day 1 Hignest Temprature 90


# 9. An artist has multiple paintings, each priced differently. Write a function to calculate the total cost after applying a discount based on the number of paintings purchased. Use lambda for the discount calculation and ensure it handles cases where no paintings are bought.

# l={1:50000,2:10000,3:300,4:900000,5:78899}
# n=int(input("Enter no. of painting you want"))
# sum=0
# if n==0:
#    print("Please Purches some paitings")
# for i in range(n):
#     p=int(input("Enter paiting number "))
#     sum+=l[p]

# def Total_Discount(d,s,n):
#     if n>2:
#         print(f'Your Total Cost {s},after Discount {(lambda x,d:x-(d/100*x))(s,d)}')
#     else:
#         print(f'Yout Total Cost {s}')
# Total_Discount(50,sum,n)
# output:
# Enter no. of painting you want3
# Enter paiting number 1
# Enter paiting number 2
# Enter paiting number 3
# Your Total Cost 60300,after Discount 30150.0
        

# # 10. A bakery tracks daily sales of different items. Write a program that uses enumerate to assign a unique ID to each item and prints a sorted list of items based on their sales.
# d=[('cupcake',50),('cake',300),('bread',30),('pizzaBase',25)]
# print(sorted(d,key=lambda x:x[1]))
# output:
# [('pizzaBase', 25), ('bread', 30), ('cupcake', 50), ('cake', 300)]


# 11. A treasure hunter deciphers clues using patterns of numbers. Write a function that generates a sequence of numbers based on a formula using eval. Ensure the formula can be dynamically entered by the user.

# 12. A tech company conducts coding challenges. Write a program that accepts a list of participants' names and their scores, uses lambda to sort them by scores, and finds the top three participants.
# l=[('lavanya',8),('samarth',2),('priti',7),('raghav',6)]
# lst=sorted(l,key=lambda x:x[1],reverse=True)
# print(lst[:3])
# output:
# [('lavanya', 8), ('priti', 7), ('raghav', 6)]


# 13. A travel agency pairs countries with their capitals in two separate lists. Write a program that zips them together, sorts the pairs alphabetically by country name, and displays the results in a user-friendly format.
# l1=['India','Africa','America','Italy','Japan']
# l2=['Dehli','Ethiopia','Washintone D.c','Rome','Tokyo']
# l3=zip(l1,l2)
# print(sorted(l3,key=lambda x:x[0]))
# output:
# [('Africa', 'Ethiopia'), ('America', 'Washintone D.c'), ('India', 'Dehli'), ('Italy', 'Rome'), ('Japan', 'Tokyo')]

# 14. A bookstore offers discounts based on the total number of books purchased. Write a function that calculates the total cost using lambda and returns the discounted price for a given number of books and their prices
# book={1:300,2:566,3:700,4:78,5:900}
# n=int(input("Enter no of book you want "))
# boks=[]
# for i in range(n):
#     k=int(input("Enter book no "))
#     boks.append(book[k])

# sum=(lambda l: sum(l))(boks)
# def Dicount_Price(sum,d):
#     dc=lambda sum,d:(sum-(d/100*sum))
#     return dc(sum,d)
# if n>2:
#     print(f'Your Total Cost {sum} Dicounted Price {Dicount_Price(sum,20)}')
# output:
# nter no of book you want 3
# Enter book no 1
# Enter book no 2
# Enter book no 3
# Your Total Cost 1566 Dicounted Price 1252.8

# 15. A wildlife researcher tracks the weights of animals over time. Write a program that takes two lists of weights recorded on different days, zips them together, and uses a loop to find the maximum weight change between any two days.\
# d1=[100,90,300,200]
# d2=[112,88,304,203]

# max=0
# for i,j in zip(d1,d2):
#     if abs(j-i)>max:
#         max=abs(j-i)
# print('Maximum weight difference',max)
# output:
# Maximum weight difference 12

