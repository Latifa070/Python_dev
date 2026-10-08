#movie ticket
while True:
   message = input("How old are you? \n Enter quit to stop the program :" ) 
   if message.lower()== 'quit':
    print("Goodbye!")
    break
   
   age=int(message)

   if age <3:
       print("\nYour movie ticket is free")

   elif 3<= age <=12:
     print("\nYour movie ticket cost $10")

   else:
     print("\nYour ticket is $15")