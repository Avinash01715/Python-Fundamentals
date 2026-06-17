

# def greet(user):
#     if not user:
#        print("hello avi")
#     else:
#         print("hello",user)


# greet("")


# method 2

def greet(user = "defalut_name"):
    return "hello "+ user + " !"

print(greet())
