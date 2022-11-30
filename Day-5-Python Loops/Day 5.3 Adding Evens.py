sum_of_evens = 0 # accumulator
for even_number in range(0, 101, 2):
    sum_of_evens = sum_of_evens + even_number
print(sum_of_evens)

sum_of_evens1 = 0 # accumulator
for even_number in range(0, 101):
    if even_number % 2 == 0:
        sum_of_evens1 += even_number
print(sum_of_evens1)