class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"    
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

MyTesla = Electric_Car("Tesla","Model S","80kwh")

print(MyTesla.brand)
print(MyTesla.battery_size)
print(MyTesla.fullname())




