# accumulator
hundred = 0
for number in range(1, 101):
    # hundred = hundred + number
    if number % 3 and number % 5:
        print("FizzBuzz")
    elif number % 3:
        print("Fizz")
    elif number % 5:
        print("Buzz")
    else:
        print(number)