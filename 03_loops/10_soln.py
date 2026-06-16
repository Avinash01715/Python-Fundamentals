import time

times = 2

attempts = 1

password = 1234

max_attempts = 5

while attempts <= max_attempts:
    org_pass = int(input("Enter the password in intergers: "))

    if org_pass == password:
        print("correct")
        break
    
    print("Wrong Attempt- ", attempts, " retry in ",times, " seconds")
    time.sleep(times)
    attempts = attempts + 1
    times = times*times



