# # find greatest midlest and smallest of number
# n1=int(input("enter no1: "))
# n2=int(input("Enter no2: "))
# n3=int(input("enter no3: "))  

# if n1>n2:
#     if n1>n3:
#         print(n1,'is greatest')
#         if n3>n2:
#            print(n3,'is middlest')
#            print(n2,'is smallest')
#         else:
#            print(n2,'is middlest')
#            print(n3,'is smallest')
           
#     else:
#         print(n3,'is greatest')
#         print(n1,'is middlest')
#         print(n2,'is smallest ')
# else:
#     if(n2>n3):
#      print(n2,'is gretest')
#      if n3>n1:
#         print(n3,'is middlest')
#         print(n1,'is smallest')
#      else:
#        print(n1 ,'middlest')
#        print(n3,'is smallest')
#     else:
#      print (n3,'is gtretest')
#      print(n2,'is middlest')
#      print(n1,'is smallest')




    
#2 positive print yes positive

# n=int(input("Enter no "))
# if n>0:
#     print('The number is positive')

#3 marks>=90 - A
# marks>=75 - B
# marks >=50 - c
# below 50 grade - F
# grades=int(input("Enter grades "))
# if grades >= 90:
#     print('A')
# elif (grades>=75)and(grades<90):
#     print('B')
# elif (grades>=50)and(grades<75):
#     print('C')
# else:
#     print("Fail")

#7 write a program to check if number lies between 10 and 59 
# n=int(input("enter no "))
# if n in range(10,51):
#     print("Number is in range")

#8 wap to create simple calculator addition,substraction,multiplication and division based on user input
# ex=eval(input("enter input "))
# print(ex)

# ex=input("enter expression ")

# if '+' in ex:
#     l=ex.index('+')
#     print(int(ex[:l])+int(ex[l+1:]))
# elif '-' in ex:
#     l=ex.index('-')
#     print(int(ex[:l])-int(ex[l+1:]))
# elif '*' in ex:
#     l=ex.index('*')
#     print(int(ex[:l])*int(ex[l+1:]))


#9 

#6-1-25
# 1

# 2 valid cordinates  count rather than int
# c=0
# co=[(1,2),(3,'4'),('5',6),(7,8),('10','11'),(9,10)]
# for i in co:
#     if type(i[0])==int and type(i[1])==int:
#         c+=1
# print(c)

#4 lambda function to filter nos. greater than 20 
# l=[1,7,30,20,32,60,3,7,19,21,47]
# print(list(filter(lambda x:x>20,l)))

# 5
# data={'1/1/2024':100,'2/1/2024':200,'3/1/2024':50,'4/1/2024':300,'5/1/2024':400,'6/1/2024':500,'7/1/2024':80}
# min=data['1/1/2024']
# max=0
# for i in data:
#     if data[i]<min:
#         min=data[i]
    
#     if data[i]>max:
#         max=data[i]

# print('Best Buing Date:',min)
# print('Best Selling Date:',max)
# print('Max_Profit',max-min)


# data={
#     'Match 1':50,
#     'Match 2':100,
#     'Match 3':15,
#     'Match 4':75,
#     'Match 5':39
# }

# # best score
# #lowest score
# min=data['Match 1']
# max=0
# sum=0
# more_than_50=0
# Total_fifties=0
# Total_centuries=0
# for i in data:
#     if data[i]>=50 or data[i]<100:
#         Total_fifties +=1
#     if data[i]>=100:
#         Total_centuries +=1

#     if data[i]>=50:
#         more_than_50+=1

#     if data[i]<min:
#         min=data[i]
#     if data[i]>max:
#         max=data[i]
#     sum+=data[i]
# for i in data:
#     if data[i]==max:
#         print('Best Score: ',max)
#         print('Best Match: ',i)
#     if data[i]==min:
#         print('Lowest Score: ',min)
#         print('Least Match: ',i)
# print("Avg: ",sum/len(data))
# print('Total_Fifties_and Centuries: ',Total_fifties,Total_centuries)
# print('More_Than_50: ',more_than_50)

# 7-12-2025
# 1
# list of dictionary where each dictionary caontains information about a student (their name and age)
# write list comprehension to create list of the name of all students who are over 18 year old
# students=[
#     {'name':'Alice','age':17},
#     {'name':'Bob','age':20},
#     {'name':'Charlie','age':19},
#     {'name':'David','age':22},
#     {'name':'Eve','age':16}
#     ]
# print(students)
# lst=[d['name']for d in students if d['age']>18]
# print(lst)

# 2 the logest palidrome from the string 
# s='abacdabbacd'
# max=0
# for i in s:
#     for j in range(i+2):
    
