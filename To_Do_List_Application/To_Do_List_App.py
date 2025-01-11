print("**************************** To Do List *************************************")

d={}
def Add():
    length=int(input("Enter no.of Items you want to add "))
    for i in range(length):
        item=input("Enter Item ")
        d.update({len(d)+1:item})
    print("Items Added Succefully ..........")

# deleting Items  
def Delete():
    # When List is Empty
    if len(d)==0:
        print("List is empty")
        return
    
    dlen=int(input('Enter no.of Items you want to delete '))
    # when no of items are not present in list 
    if dlen>len(d):
        print("No of Items Not Present ")
        return

    else:
     while(dlen!=0):
        dno=int(input("Enter Task Number "))
        if dno not in d:
            print('Task Not exist')
            
        else:
            d.pop(dno)
            dlen-=1
    print("---------------------------Deleted Succefully \U0001F600")



# Display Items
def Display():
    print("-----------------------Your To Do List-------------------")
    # when list is empty 
    if len(d)==0:
        print("**************No Tasks To do \U0001F600")
    for k,v in d.items():
        print(str(k),"-",v,"✅")


# Menu Programe
def Menu(n):
    if n==1:
        Add()
    elif n==2:
        Delete()
    elif n==3:
        Display()


print("Please Enter your Choice: ")
print('1.Add Items')
print('2.Delete Items')
print('3.Display List')
print('4.Exist')
n=int(input('Enter Choice: '))
while(n!=4):
    Menu(n)
    print('if you want to continue enter choice if not press 4')
    if (n!=4):
        print('1.Add Items')
        print('2.Delete Items')
        print('3.Display List')
    n=int(input("Enter Choice: "))
print("Thank you for Visiting \U0001F600")