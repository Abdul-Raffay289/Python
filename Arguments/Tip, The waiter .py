def total_calc(bill_amount, tip):
    total_bill = bill_amount*(1 + 0.01*tip)
    total_bill = round(total_bill, 2)
    print( f"Please Pay ${total_bill} ")
total_calc(150, 20)