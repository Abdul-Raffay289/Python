# Input total amount
total_amount = float(input("Enter total amount: "))

# Input paid amount
paid_amount = float(input("Enter paid amount: "))

# Calculate due amount
due_amount = total_amount - paid_amount

# Check and display result
if due_amount > 0:
    print("Due amount is:", due_amount)
elif due_amount == 0:
    print("No due amount. Payment is complete.")
else:
    print("Extra amount paid:", abs(due_amount))
