import time

def timer(func):
    def wrapper(*arg, **kwargs):

        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()

        print(f"{func.__name__} ran in {end - start} sec time")
         
        return result 
    return wrapper

@timer
def myfunc(n):
    time.sleep(n)

myfunc(3)