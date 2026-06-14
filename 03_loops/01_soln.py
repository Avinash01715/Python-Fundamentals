# given list

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_count = 0

for i in numbers:
    if i > 0:
        positive_count = positive_count + 1
print("Positive numbers count : ",positive_count)
