class Car:
    def __init__(self, model, make):
        self.model = model
        self.make = make
        

    def get_descriptive_name(self):
        print(f"{self.model} {self.make}")

    def update_read_odometer(self, read_odometer):
        self.read_odometer = read_odometer

    def increment(self, miles):
        self.read_odometer += miles

        
    def read (self):
        print(f"The car has {self.read_odometer} on it ")



my_car = Car ("Toyota","corolla" )
my_car.get_descriptive_name ()
my_car.update_read_odometer(50)
my_car.read()

my_car.increment(100)
my_car.read()