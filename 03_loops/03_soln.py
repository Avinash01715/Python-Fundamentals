n = int(input("Enter the number: "))


 # method 1

# for i in range(1, 11):
#     if(i != 5):
#         print(n, " x ", i, " = ", n*i)
    
# method 2

for i in range(1, 11):
    if(i == 5):
        continue
    print(n, " x ", i, " = ", n*i)



    
