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



class battery:
    def battery_info(self):
        return "This is battery"
    
class engine:
    def engine_info(self):
        return "This is engine"
    
class EV(battery,engine,Car):      #---> multiple inheritance
    pass


newCar = EV("Tesla","CyberTruck")

print(newCar.battery_info())
print(newCar.engine_info())
    


