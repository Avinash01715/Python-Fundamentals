class Car:
    def __init__(self, brand, model):
        self.__brand = brand    #----> private brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !!!!!"    #------> getter method

    def fullname(self):
        return f"{self.brand} {self.model}"  

    def fuel_type(self):
        return "petrol or diesel"  
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
 
    def fuel_type(self):
        return "Runs on battery"  
    

MyTesla = Electric_Car("Tesla","Model S","80kwh")
print(MyTesla.fuel_type())

Sierra = Car("Tata", "Sierra")
print(Sierra.fuel_type())






