
# promptign user to enter a series of pizza toppings
prompt = "\n Enter a series of toppings for the pizza "
prompt += "\n Enter 'quit' to stop the program : "

active = True
while active:
   message = input(prompt)
   if message.lower()=='quit': 
    active = False
   else:
    print(f" \n You will add {message } to your pizza")

print(" ")


