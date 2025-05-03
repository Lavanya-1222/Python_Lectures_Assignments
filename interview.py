def mydecor(fun):
    def wrapper():
        print('***********')
        fun()
        print("***********")
    return wrapper
@mydecor
def fun():
    print("Welcome to Website ")
fun()