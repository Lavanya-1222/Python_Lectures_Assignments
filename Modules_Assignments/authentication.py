def isauthor(acc,d):
 i=0
 while(i<2):
    try:
        if int(acc) in d:
            print("Loggined Succefully")
            return int(acc)
        else:
           print("Account number is Invalid")
           i+=1
           acc=input("Enter Account Number ")
           if i==2:
              if int(acc) in d:
                 print("Loggined Succefully")
                 return int(acc)
           
           
    except:
       acc=input("Please enter Account number in positive integer")
 return "No"
    