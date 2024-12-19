# 

name=input('Enter Full name ')
l=name.split(" ")

if len(l)==3:
    print(f'First_name: {l[0]}\n Last_name: {l[1]}\nMiddle_name: {l[2]}')
else:
    print("full name not found")