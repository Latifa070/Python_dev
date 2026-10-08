message =input("Tell me something and I will repeat it to you : ")
print(message)
print(" ")


name = input("Enter your name: ")
print(f"\n Hello, {name}")
print(" ")

# taking a user input, asking the user the kind of rental car they like and print some
rental_car =input("What kind of rental car would you like?: ")
print(f"Let's see if we can get you a {rental_car}")
print(" ")

# a program asking the user the number of people in his/her group
numberOfPeople = int(input("What is the number of people in your dinner group? : "))
if numberOfPeople > 8:
   print("Sorry, You will have to wait for a table")
else:
    print("Your table is ready")
print(" ")

#asking the user for number and reporting weather the number is a multiple of 10 or not
number =int(input("Enter a number to whether it is a multiple of 10 or not : "))
if number % 10 == 0:
    print(f"{number } is a multiple of 10 ")
else:
    print(f"{number } is not a multiple of 10 ")