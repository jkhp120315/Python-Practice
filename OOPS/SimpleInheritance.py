
class Car:
    color = "Blue"
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
    

car1 = ToyotaCar("Altis")

print(car1.color)
print(car1.start())