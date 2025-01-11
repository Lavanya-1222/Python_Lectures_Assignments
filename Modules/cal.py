import Maths 
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Floordiv")
print('6.Expo')

n=int(input("Enter your choice "))
while(n!=0):
    if n==1:
        print("Sum:",Maths.add(int(input("Enter no1 ")),int(input("Enter no2 "))))
    elif n==2:
        Maths.sub(int(input("Enter no1 ")),int(input("Enter no2 ")))
    n=int(input("Enter no "))
    



