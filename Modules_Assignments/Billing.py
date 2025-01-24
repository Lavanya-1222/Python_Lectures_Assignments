#      3. Calculate the total bill and apply a conditional discount if the bill exceeds a certain amount. 
def Bill(Total_Bill):
    if Total_Bill>200 and Total_Bill<1000:
        print("Congrasulations You Got Discount of 20% on above 200 Bill")
        return f'Total Bill: {Total_Bill} Discounted Bill: {Total_Bill-(20/100*Total_Bill)}'
    elif Total_Bill>1000:
        print("Congrasulations You Got Discount of 50% on above 1000 Bill")
        return f'Total Bill: {Total_Bill} Discounted Bill: {Total_Bill-(50/100*Total_Bill)}'
    else:
        return f'Your Total Bill {Total_Bill}'


