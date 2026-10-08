class User:
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first} {self.last} {self.age} {self.gender}")

    def greet_user(self):
        print(f"Hello, {self.first} {self.last}")

    def increment_login_attempts(self ):
        self.login_attempts += 1

    def reset_login_attempts(self):
       self.login_attempts = 0
       

user1 = User("Latifa", "Hamid", 26, "Female" , 0)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
