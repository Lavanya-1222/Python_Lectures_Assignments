
def patient_register(p,d,Id):

    
    print(Id)
    department=input("enter Department ")
    if department in d.values():
      name=input("Enter Name ")
      p.update({'name':name,'ID':Id,'Department':department})
    else:
       print("Sorry Dr is not available ")