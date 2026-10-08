class Car :
    def __init__(self, brand, model,year,color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def descriptive_name(self):
        print(f"{self.brand} {self.model} {self.year} {self.color}")

my_car = Car("Toyota","Corolla", 2020,"white")
my_car.descriptive_name()

class ElectricCar(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.battery = 50

    def describe_battery(self):
        print(f"The car has {self.battery} -kwh battery")

    

electric = ElectricCar("BMW","3 Series ",2011, "Black")
electric.descriptive_name()
electric.describe_battery()