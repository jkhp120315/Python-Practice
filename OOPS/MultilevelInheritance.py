
class Car:
    def __init__(self,transmissiontype):
        self.transmissiontype = transmissiontype

    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class Cartype(Car):
    def __init__(self,type,transmissiontype):
        self.type = type
        super().__init__(transmissiontype)

    def getCarType(self):
        return self.type
    

class Toyota(Cartype):
    def __init__(self,name,type,transmissiontype):
        self.name = name
        super().__init__(type,transmissiontype)

car1 = Toyota("Fortuner" , "SUV", "Automatic")
print(car1.name)
print(car1.getCarType())
print(car1.transmissiontype)