# adding two numbers entered as two digits at once
two_digit_number = input("Type a two digit number: ")

first_number = two_digit_number[0]
second_number = two_digit_number[1]

# type casting after, not before subscripting
Sum = int(first_number) + int(second_number)
print(Sum)