# 5. Welcome to the Tip calculator:

print("Welcome to the Tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")
total_bill_float = float(total_bill)
tip_percentage_float = float(tip_percentage)
num_people_float = float(num_people)
tip_amount = (tip_percentage_float / 100) * total_bill_float
bill_amount = round((tip_amount + total_bill_float) / num_people_float, 2)
final_bill_amount = "{:.2f}".format(bill_amount)
message = f"Each person should pay: ${final_bill_amount}"
print(message)
