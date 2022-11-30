student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# alternatives
# for i in student_heights:
#     total = sum(student_heights)
#     average = int(total / len(student_heights))
# print(average)

# total = 0
# for i in student_heights:
#     total = total + int(i)
#     # total += i
#     average = int(total / len(student_heights))
# print(average)
total_height = 0
for height in student_heights:
    total_height = total_height + height

number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students + 1

average = int(total_height / number_of_students)
print(average)