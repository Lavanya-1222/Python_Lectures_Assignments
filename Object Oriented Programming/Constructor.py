


class A:
    def __init__(self):
        print("Constructor called")
    def greet(self):
        print("hello")
# o=A()
# o.greet()
# we have called __init__ it get excuted as we created the object 
# while we have to call the greet() with the object 




class Cal:
    def __init__(self):
        self.a=10
        self.b=20
    def add(self):
        print("Sum",self.a+self.b)
    def sub(self):
        print("Sub",self.a-self.b)
    def mul(self):
        print("MUL",self.a*self.b)
# o=Cal()
# o.sub()
# o.mul()

# 2 Parameterised Constructor

class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Sum",self.a+self.b)
    
o=Cal(10,20)
# o.add()





class Bank:
    def __init__(self,balance):
        self.balance=balance
    def Balance(self):
        print("Current Balance:",{self.balance})
    def Deposit(self):
        amt=int(input("Enter amout "))
        self.balance+=amt
    def Withdrawl(self):
        amt=int(input("Enter amount "))
        if amt>self.balance:
            print("Insuffient Balance")
        else:
            self.balance-=amt

# print("""Welcome to Bank:
#       1-Check Balance
#       2-Deposit
#       3-withdrawl
#       4-Exit
#       """)
# ch=int(input("Enter your Choice: "))
# bnk=Bank(0)
# while(ch!=4):
#     if ch==1:
#         bnk.Balance()
#     elif ch==2:
#         bnk.Deposit()
#     elif ch==3:
#         bnk.Withdrawl()
#     ch=int(input("Enter your Choice "))





class Numbers:
    def __init__(self,l):
        self.l=l
    def Check_even(self):
        for i in self.l:
            if i%2==0:
                print(i,'Even')
    def Check_Odd(self):
        for i in self.l:
            if i%2!=0:
                print(i,'Odd')
    def Check_Prime(self):
        for i in self.l:
            f=1
            for j in range(2,i):
                if i%j==0:
                    f=0
            if f==1:
                print(i,"Prime Number")
# n=Numbers([3,8,5,7,11,21,45,87])
# n.Check_even()
# n.Check_Odd()
# n.Check_Prime()

    