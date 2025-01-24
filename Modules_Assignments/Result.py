def result(name,marks):
  if marks>100:
    print(name,"You Got Invalid Result ")
  else:
    print(f'-------------{name}-----------------')
    if marks>=75 and marks<=100:
        print("Total Marks:",marks,"Grade:",'A')
    elif marks>=55 and marks<=74:
        print("Total Marks:",marks,"Grade:",'B')
    elif marks>=35 and marks<=54:
        print("Total Marks:",marks,"Grade:",'C')
    elif marks<35:
        print("Your Failed ")


    