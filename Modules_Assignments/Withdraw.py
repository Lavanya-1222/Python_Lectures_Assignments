def withdraw(acc,d):
    
    while(True):

     try:
       amount=int(input("enter amount "))
       if d[acc]>=amount:
         d[acc]=d[acc]-amount
         print("Withdrawal Sussefully")
         return
       else:
         print("Insuffiensint Balance ")
         return
         
         
     except:
       print("Enter amount in positive integer ")
