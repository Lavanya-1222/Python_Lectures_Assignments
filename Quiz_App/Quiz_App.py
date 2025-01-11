# Prepare a list of questions and their correct answers.  
d={1:{'What is a correct syntax to output "Hello" in Python?':
      ['Print("Hello")','print(Hello)','print Hello','print("Hello")'],
      'ans':4
      },

    2:{'Is Python code compiled or interpreted?':['Python code is both compiled and interpreted',' Python code is neither compiled nor interpreted','Python code is only compiled','Python code is only interpreted'],
         'ans':1
         },
    3:{'All keywords in Python are in _________':['Capitalized','lower case','UPPER CASE','None of the mentioned'],
            'ans':4},
    4:{'What is the order of precedence in python?':[' Exponential, Parentheses, Multiplication, Division, Addition, Subtraction','Parentheses, Exponential, Multiplication, Division, Addition, Subtraction','Exponential, Parentheses, Division, Multiplication, Addition, Subtraction','Parentheses, Exponential, Multiplication, Addition, Division, Subtraction'],
           'ans':2},
            
    5:{'What does pip stand for python?':['Pip Installs Python','Pip Installs Packages','Preferred Installer Program','All of the mentioned'],
       'ans':3},
    6:{' Which of the following is the truncation division operator in Python?':['/','//','%','|'],
       'ans':2},
    7:{'What will be the output of the following Python function?\nmin(max(False,-3,-4), 2,7)':[2,-4,0,7],
       'ans':3},
    8:{'What arithmetic operators cannot be used with strings in Python?':['+','*','-','All Of Above'],'ans':3
       },
    9:{'Which of the following statements is used to create an empty set in Python?':['()','[]','{}','set()'],
       'ans':4},
    10:{'What is the maximum possible length of an identifier in Python?':['71','32','64','None Of All'],'ans':4}


            }

# Create a function to display each question and accept the user's answer. 
def Quiz():
    n=1
    global Final_Score
    Final_Score=0
    score=0
    for val in d.values():

        print()
        for k,v in list(val.items()):
         if k!='ans':
           print(n,"-",k)
           print('1)',v[0])
           print('2)',v[1])
           print('3)',v[2])
           print('4)',v[3])
        n+=1
        an=int(input("Enter Your Answer "))
        if k=='ans':
         if an==v:
            score+=10 #Validate the user’s answer and keep track of the score.
    Final_Score=((score/100)*100)
    return Final_Score

    

def View_Score(f_score):
    print("Your Recent Score is",f_score) # Allow users to view their most recent score without retaking the quiz
    print("if you want to retake Quize please enter y",end=" ")#Provide an option to retake the quiz and reset the score for a new attempt.
    out=input()
    if out=='y':
       f=Quiz()
       print("Your current Score: ",f)
    else:
       return


Final_Score=0
def Menu(n):
    global Final_Score
    if n==1:
        Final_Score=Quiz()
        print('Your Score:',Final_Score)# Display the final score after the quiz is completed
    elif n==2:
        View_Score(Final_Score)




print("******************Welcome To Quiz Computition*****************")
print('Please Enter your Choice')
print('1.Take Quiz')
print('2.View Score')
print('3.Exit')
n=int(input("Enter Choice "))
while(n!=3):
    Menu(n)
    print("If you want to continue press choice if not the press 3")
    if n!=3:
        print('1.Take quiz')
        print('2.View Score')
    n=int(input("Enter Choice "))

print("Thank you for visiting \u0001F600")


    


