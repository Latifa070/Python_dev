#passing a list of users to a function and sending them greetings individually

def greet_users(names):
    for name in names:
     mgs = f"Hello, {name.title()}"
     print(mgs)

usernames = ["latifa","hamid","rahmatu"]
greet_users(usernames)

#modifying a list in a function

def print_models(unprinted_models, completed_models):
   while unprinted_models:
      current_design =unprinted_models.pop()
      print(f"Designing this model: {current_design}")
      completed_models.append(current_design)

def show_completed_design(completed_models):
   for completed_model in completed_models:
      print(completed_model)

unprinted_models =["gold", "silver", "diamond"]
completed_models =[]

print_models(unprinted_models, completed_models)
show_completed_design(completed_models)
