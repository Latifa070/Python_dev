class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant (self):
        print(f"The name of the restaurant is : {self.restaurant_name}")
        print (f"The cuisine type is : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open ")

restaurant1 = Restaurant("Buka Restaurant", "Traditional West African cuisine")
restaurant1.describe_restaurant()
print(" ")


restaurant2 = Restaurant(" Santoku", "Japanese cuisine ")
restaurant2.describe_restaurant()

print(" ")
restaurant2 = Restaurant("Asanka Local Restaurant", "Traditional Ghanaian cuisine")
restaurant2.describe_restaurant()