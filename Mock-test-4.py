# n=int(input("Enter no "))

# n1=0
# n2=1
# sum=1
# print(n1,n2,end=" ")
# for i in range(n-2):
#     c=n1+n2
#     print(c,end=" ")
#     sum+=c
#     n1=n2
#     n2=c
# print("sum:",sum)

# mplement a class Rectangle with methods to compute area and perimeter.

class Rectangle:
    def __init__(self):
        self.length=int(input("enter length "))
        self.breadth=int(input("enter breadth "))
    def area(self):
        print("Area:",self.length*self.breadth)
    def perimeter(self):
        print("perimeter:",2*(self.length+self.breadth))

r1=Rectangle()
r1.area()
r1.perimeter()