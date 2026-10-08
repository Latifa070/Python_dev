class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def  describe_user(self):
        print(
            f"{self.first_name} {self.last_name} {self.age} {self.gender}"
            
            )
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

user = User("Latifa", "Hamid", 26, "Female")
user.describe_user()
user.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, privileges):
        super().__init__(first_name, last_name, age, gender)

        self.privileges = privileges

    def show_privileges(self):
        print(f"{self.privileges}")

admin = Admin("Latifa","Hamid", 26,"Female",["can add post","can delete post", "can ban user"])
admin.show_privileges()
