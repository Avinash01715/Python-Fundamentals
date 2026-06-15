items = ["apple", "banana", "orange", "apple", "mango"]

for i in items:
    if items.count(i) == 2:
        print(i," is duplicate")
        break