d={}
def Login():
    username=input("Enter Username ")
    if username in d:
        password=input("Enter Password ")
        if password==d[username]:
            print("---------------------Loggined Succefully \U0001F600")
        else:# password is not currect
            print('Password is incorrect Try Again')
            Login()
    else:#user is not available 
        print("User doesn't Exist please Register")
        Register()



# Resistration process
def Register():
    username=input("Enter Username: ")
    if (validate(username)):
        password=input("Enter Password:")
        d.update({username:password})
        print("----------------------------------Registration Succefull\U0001F600")


       

# Validating username
def validate(name):
    spchr=['!','@','#','$','%','^','&','*','(',')','-','~','+','//','\\']
    if len(name)==0:
        print('username should not be empty')
        Register()
    elif (len(name)>25):
        print('username not more than 25 chatercters')
        Register()
    elif any(c in spchr for c in name):
        print('username doesn\'t contain any special charecters')
        Register()
    elif name in d:
        print('Username is available enter other one')
        Register()  
    else:
        return True



# here we are creating the menu for user with choice 
# step 4th is implemented
def Menu(n):

    if n==1:
        Login()
    elif n==2:
        Register()
#  
    
        
    
print()
print("*************Welcome To SBM Solutions ***************")
print()
print("Please Enter your Choice")
print("1.Login")
print("2.Register")
print("3.Exit")
n=int(input("Enter no: "))

   
while(n!=3):
    Menu(n)
    print("If you want to continue Please Enter your Choice if not press 3")
    if n!=3:
      print("1.Login")
      print("2.Resister")
      
    n=int(input("Enter no: "))
print("Thank you for Visiting \U0001F600")

    
    