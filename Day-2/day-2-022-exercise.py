# B_M_I calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# type casting
float(weight)
float(height)

# calculation
B_M_I = weight / height ** 2
B_M_I = int(B_M_I)

print(B_M_I)