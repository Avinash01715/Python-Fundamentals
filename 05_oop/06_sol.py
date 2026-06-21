class Car:
    Total_cars = 0  #----> class variable
    
    def __init__(self, brand, model):
        self.__brand = brand    #----> private brand
        self.model = model
        Car.Total_cars += 1

    def get_brand(self):
        return self.__brand + " !!!!!"    #------> getter method

    
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
 
    
    

MyTesla = Electric_Car("Tesla","Model S","80kwh")


Sierra = Car("Tata", "Sierra")


print(Car.Total_cars)






