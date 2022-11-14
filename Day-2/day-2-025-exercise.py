print("Welcome to the tip calculator")
# user input
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# calculations
percentage_tip = (tip / 100)
total_tip = bill * percentage_tip
total_bill = bill + total_tip
bill_per_person = round((total_bill / people), 2)

# output
print(f"Each person should pay ${bill_per_person}")