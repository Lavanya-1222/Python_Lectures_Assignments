# grade=int(input("Enter grades: "))
# if grade>=75:
#     print("Distinct")
# elif grade<75 and grade>=60:
#     print("First Class")
# elif grade<60 and grade>=40:
#     print("Pass")
# else:
#     print("Fail")

#4 
numbers=[3,10,30,150,9,7,102]

for i in numbers:
    if i % 3==0:
        if i>100:
            print(i,"is Super Magic Number")
        else:
            print(i," is Magic Number")

#6 write a recursive function to calculate the sum of digits of a inter no

def sum_of_digit(i,sum,n):
    if n==0:
        return 
    else:
        sum+=i
        print(sum)
        return sum_of_digit(n%10,sum,n//10)
sum_of_digit(0,0,123)

    