

age = int(input("Enter age of person: "))
day = input("Enter day (keeping 1st letter capital): ")

price = 12 if age >=18 else 8 

if day == "Wednesday":
    price = price - 2

print("The price of you ticket is: $", price)
