unconfirm_users =['latifa','mohammed','rahmatu','assia','tijani']
confirm_users = []

while unconfirm_users:
    current_user = unconfirm_users.pop()

    print(f"verifying user:  {current_user.title()}")
    confirm_users.append(current_user)

print("\nVerified users : \n")
for confirm_user in confirm_users:
    print(f"{confirm_user.title()} ")
