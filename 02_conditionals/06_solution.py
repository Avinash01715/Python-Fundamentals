distance = int(input("Enter distance in km:   "))

if distance > 15:
    Transport = "Travel by Car"
elif distance > 3:
    Transport = "Travel by bike"
else:
    Transport = "Go by Walking"

print(Transport)