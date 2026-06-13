weather = input("How is the Weather today(sunny,rainy,snowy)?   ")

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a Book"
elif weather == "snowy":
    activity = "Build a snowman"
else:
    activity = "Invalid input!"

print(activity)