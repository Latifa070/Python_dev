class User:
    def __init__(self,first_name, last_name,gender, marital_status):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.marital_status = marital_status

    def describe_user(self):
        print(f" {self.first_name} {self.last_name} , is a {self.gender} and {self.marital_status}"
        )


    def  greet_user(self):
        print(f"Hello, {self.first_name}  {self.last_name}")


user1 = User("Latifa","Hamid" , "Female", "single")
user1.describe_user()
user1.greet_user()
print(" ")
user2 = User("Assia","Ali" , "Female", "single")
user2.describe_user()
user2.greet_user()

print(" ")

user3 = User("Ramatu","salam" , "Female", "married")
user3.describe_user()
user3.greet_user()

        