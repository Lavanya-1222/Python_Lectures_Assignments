# 
l=[1,3,6,10,15,20,21]

a=list(filter(lambda k: k%3!=0,l))
l=[i**2 for i in a]
print(l)
