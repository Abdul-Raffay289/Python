actual_amount = float(input("Enter the actual amount:" ))
selling_amount = float(input("Enter the selling amount:" ))
if actual_amount < selling_amount: 
    amount = selling_amount - actual_amount
    print("Your profit is", amount)
else:
    print("No Profit!")