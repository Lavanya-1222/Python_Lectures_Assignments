'''
# 1.Create a BankAccount class with a constructor that initializes the account holder's name 
# and initial balance. Implement methods to deposit and withdraw money.
class BankAccount:
    def __init__(self,name,bal=0):
        self.name=name
        self.bal=bal
    def deposit(self,amount):
        try:
           self.bal+=amount
           print("Diposited Succefully")
        except:
            print("Amount Should be in whole number")
    def withdraw(self,amount):
        if self.bal<amount:
            print("Insuffient Balance")
        else:
            self.bal-=amount
            print("Windrawal succefully")
    def display(self):
        print("your Current Balance:",self.bal)
b=BankAccount('lavanya',1000)
b.display()
b.deposit('2000')
b.display()
b.withdraw(500)
b.display()


'''
"""
# 2.Create a Student class with a constructor that takes the student's name and marks in three subjects. 
# Implement a method to calculate the average marks and determine the grade based on the average.
class Student:
    def __init__(self,name):
        self.name=name
        self.hindi=int(input("enter marks in hindi "))
        self.math=int(input("enter marks in Maths  "))
        self.marathi=int(input("enter marks in Marathi "))
    def avg(self):
        self.avg=(self.hindi+self.math+self.marathi)//3
    def grade(self):
        if self.avg in range(80,100):
            print("A")
        elif self.avg in range(60,79):
            print("B")
        elif self.avg in range(40,59):
            print("C")
        else:
            print("Fail")
s=Student('lavanya')
s.avg()
s.grade()

"""

# 3.Create a Rectangle class with a constructor that initializes the length and width. 
# Implement methods to calculate the area and perimeter of the rectangle
class Rectangle:
    def __init__(self,len,width):
        self.length=len
        self.width=width
    def area(self):
        print("Area",self.length*self.width)
    def perimeter(self):
        print("Perimeter",2*(self.length+self.width))
r=Rectangle(10,20)
r.area()
r.perimeter()

# 4.Create an Employee class that has a constructor accepting name, designation, and salary. 
# Implement a method to increase the salary by a given percentage.
class Employee:
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
    def increasesal(self,percentage):
        print("Before Increase Salary ",self.salary)
        print("Increased Salary",self.salary+(self.salary*(percentage/100)))

e=Employee('lavanya','DataScientist',100)
e.increasesal(10)

# 5.Create a NumberCheck class with a constructor (_init_) that initializes a number.
# and check a Number is Armstrong or not. Display in a method.

class NumberCheck:
    def __init__(self,no):
        self.num=no
    def CheckArm(self):
        ln=len(str(self.num))
        t=self.num
        sum=0
        while(self.num!=0):
            sum+=((self.num%10)**ln)
            self.num//=10 
        if t==sum:
            print("Armstrong")
        else:
            print("Not ArmStrong")
n=NumberCheck(8208)
n.CheckArm()
            
