def make_pizza (size, *toppings):
    print (f"making {size} INCH pizza with the following toppings - {toppings}")


make_pizza (15, "meat", "beef")
make_pizza (10, "sausage", "carrots")

def build_profile (first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name

    return user_info

profile = build_profile (
                        "hamid",
                         "latifa", 
                         location="darkuman",
                           town ="accra")
print(profile)

