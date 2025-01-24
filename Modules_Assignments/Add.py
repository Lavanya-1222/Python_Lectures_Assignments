def Return(d):
  try:
    s=input("Enter book name ")
    author=input("Enter Author name ")
    d.update({s:{'author':author,'availability':True}})
    print("Book Returned Succesfully")
  except:
    print("Please Enter Correctly")
