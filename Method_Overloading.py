def method_overload(name,age=10,city='Solapur'):
    print(name,city,age)
method_overload('lavanya','Pune') # if keyword is not givven maintain order 
method_overload('Samarth') # always keyword arguments are at last position 
method_overload('Samarth',city='pune',age=24) #if keyword given then no need of order
                                              # keywords should match the actual keyword
                                            

def args_eg(greating,*args):
    print(greating,args)
    

args_eg("Welcome",'Lavanya','Samarth','Sneha')

def kargs_eg(greating,**kargs):
    print(greating,kargs)
    

kargs_eg("Welcome",name='Lavanya',age=24,city="Pune")

def upackings(a,b,c):
    print(a,b,c,"Result")
l=[1,2,3]
upackings(*l)
# print(*(10,20,30))
d={'name':"lavanya",'age':24}
def uppackingKARGS(name,age):
    print(name,age)
uppackingKARGS(age='lavanya',name=34)

