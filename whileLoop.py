number = 0
while number  < 5:
    number += 1
    print(number)


prompt = "Tell me something and I will repeat it back to you: "
prompt += "Enter 'quit to stop the program : "

message = " "
while message != 'quit'.lower():
   message = input(prompt)
   
   if message != 'quit':
     print(message)