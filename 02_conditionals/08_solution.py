password = input("Enter the password: ")
pass_len = len(password)

if pass_len <= 6:
    strength = "WEAK"
elif pass_len <= 10:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print("The password strength is: ", strength)