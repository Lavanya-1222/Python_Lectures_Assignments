def borrow(d):
    b=input("Enter book name ")
    if b in d.keys():
        if d[b]['availability']==True:
            print("Please take your book")
            d.pop(b)
        else:
            print("You can't borrow this Book is currently not available")
    else:
        print("The book is not in book list")
