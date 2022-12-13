#DAY 2

print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
members = int(input("How many people to split the bill? "))
tip = float(bill * (tip_percentage / 100))
bill_after_tip = float(bill + tip)
bill_per_member = (bill_after_tip / members)
final_amount = "{:.2f}".format(bill_per_member, 4)
print(f"Each person should pay: ${final_amount}")
