def Order(menu):
  ans=1
  Total_Bill=0
  print("Please Enter Your Items once done enter done")
  #      2. Use a loop to allow customers to order multiple items.
  while(True):
    s=input("please Enter name of Item ")
    if s=='Done':
       break
    else:
     if s in menu:
         Total_Bill+=menu[s]
     else:
       print("Please Enter Items of Menu only")
  return Total_Bill
    
       


