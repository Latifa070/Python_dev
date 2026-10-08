def monthly_budget_calculator():
    """creating a function that will calculate a users monthly budget"""
    
    active = True
    while active:
        monthly_budget =int (input(f"Enter your budget for the month :  "))
        amount_on_food =  int(input(f"Enter the amount you spent on food : "))
        amount_on_transport = int( input (f"Enter the amount you spent on transport : "))
        amount_on_data = int (input (f"Enter the amount you spent on data : "))
        amount_on_others = int (input (f"Enter the amount you spent on other things : "))

        active = False
    total_amount_spent = amount_on_food+ amount_on_transport + amount_on_data + amount_on_others

    print (f"\nThe total amount spent is GHC :{total_amount_spent}")

    balance_remaining = monthly_budget - total_amount_spent

    print (f"The balance remaing is GHC: {balance_remaining}")

monthly_budget_calculator()