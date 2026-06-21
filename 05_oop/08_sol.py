class Car:
    Total_cars = 0  #----> class variable
    
    def __init__(self, brand, model):
        self.__brand = brand    #----> private brand
        self.__model = model
        Car.Total_cars += 1

    def get_brand(self):
        return self.__brand + " !!!!!"    #------> getter method
    
    @staticmethod
    def Car_description():                #---->static method
        return "Cars are Great"
    
    @property
    def model(self):
        return self.__model

    
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
 
    
    

myCar = Car("Tata","Safari")
print(myCar.model)






