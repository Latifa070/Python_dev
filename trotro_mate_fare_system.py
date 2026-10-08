class Trotro:
    def __init__(self, route, fare, passengers):
        self.route = route
        self.fare = fare
        self.passengers = passengers

    def total_money(self,):
        total = self.fare * self.passengers
        print(f"The total fare is : GHC {total}")
        
    def can_go(self):
        if self.passengers >= 10:
            print("The bus can go.")

        else:
            print("The bus can't go.")

bus = Trotro("Circle-Madina", 5.5, 15)
bus.total_money()
bus.can_go()