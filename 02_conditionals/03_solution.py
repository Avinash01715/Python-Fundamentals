score = input("Enter the Student's score: ")

score_int = int(score)

#Method 1:

# if score_int >= 101:
#     print("Invalid Score!")
# else:
#     if score_int >= 90:
#         print("Grade A")
#     elif score_int >=80:
#         print("Grade B")
#     elif score_int >=70:
#         print("Grade C")
#     elif score_int >= 60:
#         print("Grade D")
#     else:
#         print("Grade F")

#Method 2:

if score_int >= 101:
    print("Invalid Score!")
    exit()

if score_int >= 90:
    print("Grade A")
elif score_int >=80:
    print("Grade B")
elif score_int >=70:
    print("Grade C")
elif score_int >= 60:
    print("Grade D")
else:
    print("Grade F")
