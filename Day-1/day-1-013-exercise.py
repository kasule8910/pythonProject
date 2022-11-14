# a should output value of b and vice versa
a = input("a: ")
b = input("b: ")

# adding a new variable (container) to help move the assigned values
# c is like a third cup to help transfer contents like a to c then b to a then c to b
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)