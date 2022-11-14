# code begin
age = int(input("What is your current age? "))
age_diff = 90 - age
# conversion
days_left = int(age_diff * 365)
weeks_left = int(age_diff * 52)
months_left = int(age_diff * 12)

# formatted output
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months to reach 90yrs.")