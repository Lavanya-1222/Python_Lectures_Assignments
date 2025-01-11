# Maintain a list of available books along with their copies (e.g., a dictionary with book names as keys and copies as values).  
Book_List={
    "The Power of Now": 10,
    "Atomic Habits": 15,
    "The Four Agreements": 9,
    "The Alchemist": 18,
    "You Are a Badass": 10,
    "The Power of Habit": 12,
    "Start with Why": 11,
    "The Lean Startup": 7,
    "The 48 Laws of Power": 6,
    "Deep Work": 8,
    "Daring Greatly": 11,
    "The Secret": 13,
    "The Magic of Thinking Big": 8,
    "The Slight Edge": 7,
    "The 5 AM Club": 10,
    "Becoming": 9,
    "The Science of Getting Rich": 5,
    "Principles: Life and Work": 6,
    "The Compound Effect": 7,
    "The Success Principles": 8,
    "Awaken the Giant Within": 12,
    "You Can Heal Your Life": 10,
    "The Untethered Soul": 13,
    "The One Thing": 11,
    "The Confidence Gap": 8,
    "Who Moved My Cheese?": 6,
    "The Motivation Manifesto": 5,
    "The Big Leap": 7,
    "The Little Book of Hygge": 7,
    "Rising Strong": 9,
    "The Confidence Code": 8,
    "The Motivation Hacker": 7
}

# Provide an option to add new books or update the number of copies for existing books.  
def Add_Books():
    global Book_List
    l=int(input("Enter No.of books you want to add "))
    for i in range(l):
        name=input("Enter Name Of book ")
        QTY=int(input("enter Quantity of book "))
        if name in Book_List:
             QTY=Book_List[name]+QTY
        else: 
            QTY=QTY
        Book_List.update({name:QTY})

# Display a list of all available books with the number of copies for each.
def Display_Available_Books():
    global Book_List
    for k,v in Book_List.items():
        print(k,v)

# Allow users to borrow books, reducing the available copies by 1.  
def Borrow_Books():
    ans=int(input("Enter No. of book you want to borrow "))
    for i in range(ans):
        name=input("Enter name of book ")
        QTY=int(input("Enter Quntity "))
        # Prevent users from borrowing books that are out of stock.
        if name not in Book_List.keys():
            print("Entered book is out of Stock")
            continue
        else:
            Book_List[name]=Book_List[name]-QTY





def Menu(n):
    if n==1:
        Add_Books()
    elif n==2:
        Display_Available_Books()
    elif n==3:
        Borrow_Books()
print("Select Your Choice")
print("1.Add_Books")
print("2.Display_Available_Books")
print("3.Borrow _Books")
print("4.Exist")

n=int(input("Enter Your Choice "))
while(n!=4):
    Menu(n)
    ans=input("if you want to continue press y if not press n ")
    if ans=='y':
        print("1.Add_Books")
        print("2.Display_Available_Books")
        print("3.Borrow _Books")
        n=int(input("Enter Your Choice "))
    else:
        n=4
print("Thank you For Visiting \U0001F600")    