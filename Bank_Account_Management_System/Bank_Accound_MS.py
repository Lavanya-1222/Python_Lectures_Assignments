
amount=0 #Start with an initial balance of `0`

#Implement a deposit function to add a specific amount to the account
def Deposit():
    global amount
    ea=int(input('Enter Amount '))
    if ea<0:
        print("please Enter Valid Number")
        Deposit()
    else:
     amount+=ea
    
# Implement a withdraw function to deduct a specific amount from the account, ensuring sufficient balance
def Withdraw():
    global amount
    wa=int(input("please enter amount "))
    if wa>amount:
        print("Insuffisient Balance")
        Withdraw()
    else:
        amount-=wa


# Provide a function to check the current account balance
def CheckBalance():
    global amount
    print("Your Current Balance:",amount)

n=0
print("Please choose you Choice")
print("1.Deposit")
print("2.Withdraw")
print("3.CheckBalance")
print("4.Exist")
n=int(input("Enter Your Chioce "))

# Create a menu-driven interface to switch between deposit, withdraw, check balance, and exit.
def Menu(n):
    if n==1:
        Deposit()
    elif n==2:
        Withdraw()
    elif n==3:
        CheckBalance()
    

while(n!=4):
    Menu(n)
    print("If you want to continue press y if not press n")
    c=input()
    if c=='y':
      print("1.Deposit")
      print("2.Withdraw")
      print("3.CheckBalance")
      n=int(input("Enter you choice"))

    else:
        n=4
print("Thank you for Visiting \U0001F600")


