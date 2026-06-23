

def debug(func):
    def wrapper(*args, **kwargs):
        arg_values = ', '.join(str(arg) for arg in args)
        kwarg_values = ', '.join(f"{k} = {w}" for k,w in kwargs.items())

        print(f"Calling {func.__name__} with args =  {arg_values} and kwargs= {kwarg_values} ")

        return func(*args, **kwargs)
    return wrapper


@debug
def greetings(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greetings("cat", greeting="pro")
   
