distance = int(input("Enter distance in km:   "))

if distance > 15:
    activity = "Travel by Car"
elif distance > 3:
    activity = "Travel by bike"
else:
    activity = "Go by Walking"

print(activity)