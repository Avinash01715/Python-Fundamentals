def even_generator(limit):
    for i in range(2,limit + 1, 2):
        yield i


for j in even_generator(10):
    print(j)