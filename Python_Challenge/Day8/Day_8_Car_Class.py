# Create a Car class with attributes and a display method
class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.is_engine_on = False
        self.speed = 0

    def start_engine(self):
        if not self.is_engine_on:
            self.is_engine_on = True
            print("Engine started.")
        else:
            print("Engine is already on.")

    def stop_engine(self):
        if self.is_engine_on:
            self.is_engine_on = False
            self.speed = 0
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def __str__(self):
        return (
            f"Car Details:\n"
            f"Make       : {self.make}\n"
            f"Model      : {self.model}\n"
            f"Year       : {self.year}\n"
            f"Color      : {self.color}\n"
            f"Mileage    : {self.mileage} km\n"
            f"Engine On  : {'Yes' if self.is_engine_on else 'No'}\n"
            f"Speed      : {self.speed} km/h"
        )
my_car = Car("Hyundai", "i20", 2020, "White", 15000)
print(my_car)
        
