
# this function sets a budget for the user
def set_budget():
    active = True
    while active:
       budget_amount = int(input("Enter your budget : "))
       if budget_amount <= 0:
         print(f"Invalid amount, try again")

       else :

         return budget_amount
    active = False
       

def add_expense ():
