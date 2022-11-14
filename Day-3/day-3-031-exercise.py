height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Body Mass Index = weight / height ** 2
B_M_I = round((weight / height ** 2), 2)

if B_M_I < 18.5:
    print(f"with {B_M_I}, You're underweight")
elif B_M_I < 25:
    print(f"with {B_M_I}, You have normal weight")
elif B_M_I < 30:
    print(f"with {B_M_I}, You're overweight")
elif B_M_I < 35:
    print(f"with {B_M_I}, You're obese")
else:
    print(f"with {B_M_I}, You're clinically obese")

print(B_M_I)