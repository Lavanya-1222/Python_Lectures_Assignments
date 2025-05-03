# try:
#     a=10
# except ZeroDivisionError:
#     print("not")
# else:
#     print("no any Exception S")
# finally:
#     print("i will excutue")

class A:
    no=0
    def __int__(self):
        # cls.no=12
        pass
        # self.myclass()
    def inst(self,cls):
        cls.no=12
        print(cls.no)


  
    @classmethod
    def myclass(cls):
        cls.no+=1
        print("class =",cls.no)
a=A()
# A.myclass()
# a.inst(A)
A.myclass()
a.myclass()