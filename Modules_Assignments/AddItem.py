def add(Item):
    for i in range(int(input("Enter no of Items you want to add "))):
      name=input("Enter name of Item ")
      price=float(input("Enter Price "))
      while(True):
        try:

          QTY=int(input("Enter quantity "))
          if QTY<=0:
            print("enter QTY in positive number")
          else:
            Item.append({'name':name,'price':price,'stock':QTY})
            print("")
            break 
        except:
          print("enter QTY in positive number")
    print("Items Succesully Added")
