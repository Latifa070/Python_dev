class  Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def read_number_served (self):
        print(f"The number of customers served is : {self.number_served}")

    def  increment_number_served(self,numbers):
        self.number_served += numbers
        


restaurant = Restaurant("Dishes and Roses","African dishes")
print(f"Number of customers the restaurant has served {restaurant.number_served}")

restaurant.number_served = 10

print(f"Number of customers the restaurant has served {restaurant.number_served}")

restaurant.set_number_served(50)
restaurant.read_number_served()
restaurant.increment_number_served(25)
restaurant.read_number_served()
