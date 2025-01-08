"""
==========================================
    Program: Discount
    Author: Arthur Weale
    Date: 1-08-2025
    Description:
        A brief description of what the script does.
==========================================
"""

# Import required modules
from datetime import datetime  

today = datetime.now()
current_day = today.strftime("%A")
print(current_day)

final_subtotal = 0

subtotal = float(input("What is your Subtotal: "))
sales_tax = 6/100
discount = 10/100

discount_amount = subtotal * discount #The Discount amount
total_amount_due = subtotal - discount_amount #Total amount without tax
sales_tax_amount = total_amount_due * sales_tax
new_final_subtotal = total_amount_due + sales_tax_amount


if subtotal >= 50 and (current_day == "Tuesday" or current_day == "Wednesday"):
    
    print(f"Sales tax amount: {sales_tax_amount:.2f}")
    print(f"Total: {new_final_subtotal:.2f}")
else:
    new_sales_tax_amount = ((6/100) * subtotal)
    new_final_subtotal_nodiscount = subtotal + ((6/100) * subtotal)
    print(f"Sales tax amount: {new_sales_tax_amount:.2f}")
    print(f"Total: {new_final_subtotal_nodiscount:.2f}")

