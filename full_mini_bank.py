class Customer:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if self.pin != pin:
            print("Incorrect PIN.")
            return

        fee = min(amount * 0.01, 10)
        total = amount + fee

        if self.balance >= total:
            self.balance -= total
            print(f"Successfully withdrew GHC {amount}")
            print(f"Fee: GHC {fee}")
            print(f"Remaining balance: GHC {self.balance}")
        else:
            print("Insufficient balance.")

    def statement(self):
        print(f"Name: {self.name}")
        print("PIN: **")
        print(f"Balance: GHC {self.balance}")


customer1 = Customer("Latifa", 3456, 500)
customer2 = Customer("Amina", 1234, 300)

customer1.withdraw(400, 3456)

customer1.deposit(100)

customer1.statement()
customer2.statement()