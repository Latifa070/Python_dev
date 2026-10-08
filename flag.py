def formatted_fullName (firstName, lastName):
    fullName = f"{firstName} {lastName}"
    return fullName.title()

while True:
    print("\n Please tell me your name")
    print("Enter 'q' at anytime to quit")

    fName = input("first name : ")
    lName = input("last name : ")
    break

formatted = formatted_fullName(fName,lName)

print(f"Hello, {formatted}")