def remove(Items):
    print(Items)
    i=0
    n=(int(input("Enter number of Items you want to remove ")))
    while(i<n):
        name=input("Enter name ")
        f=1
        for d in Items:
           if name in d.values():
               f=0
               QTY=int(input("Enter Quntity "))
               i+=1
               if QTY>d['stock']:
                   print("Insuffient Quntity ")
                   break
               else:
                   d['stock']-=QTY
                   break
        if f==1:
          print("Item Not in List")
  
   
