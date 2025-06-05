class Car:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Starting {self.fuel_type} engine if {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model, fuel_type= 'Electric')

    def start_engine(self):
        print(f"Starting {self.fuel_type} Motor of {self.brand} {self.model}")

    def charge_battery(self):
        print("Battery charging..")

car = Car("Lamborghini", "Urus", "Petrol")
car.start_engine()

ecar = ElectricCar("Tesla", "Model 3")
ecar.start_engine()
ecar.charge_battery()
