def key_value(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print(key_value(name="homelander",powers="lazers"))