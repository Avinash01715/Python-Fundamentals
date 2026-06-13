pet = "dog"
age = int(input("Enter the age of pet in years: "))

if pet == "dog":
    if age <= 2:
        food = "give puppy food"
    else:
        food = "give senior dog food"
elif pet == "cat":
     if age <= 5:
        food = "give kitten food"
     else:
        food = "give senior cat food"

print(food)



