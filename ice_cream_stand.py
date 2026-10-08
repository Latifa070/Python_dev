class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")

restaurant = Restaurant("Dishes and Roses ", "Local dishes")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def display_flavors (self):
        print("These are the flavors :")
        for flavour in self.flavors:
            print(f"- {flavour}")

ice_cream = IceCreamStand("Dishes and Roses ", "Local dishes",["Vanilla","chocolate", "strawberry"])
ice_cream.display_flavors()

