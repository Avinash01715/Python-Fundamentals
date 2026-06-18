# def sum_all(*args):
#     return sum(args)

# print(sum_all(2,3,2))

def sum_all(*args):
    sum1 = 0
    for i in args:
        sum1 = sum1 + i
    return sum1    

print(sum_all(3,43,2))

        