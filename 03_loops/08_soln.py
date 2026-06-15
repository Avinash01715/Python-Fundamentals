n = int(input("Enter the number: "))

factor = 0 

for i in range(1,n + 1):
    if n % i == 0:
        factor = factor + 1

if factor == 2:
    print(n," is a PRIME number")
else:
    print(n," is NOT a PRIME number")

    







    



