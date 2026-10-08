def build_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info

profile = build_profile(
    "Latifa",
    "Hamid",
    location = "darkuman",
    email = "example@gmail.com",
    gender = "female"
)

print (profile)