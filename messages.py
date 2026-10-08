def send_messages (messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"I'm printing this : {current_message}")
        sent_messages.append(current_message)

messages = [
            "Good morning, dear", 
            "are we expecting you today",
            "Have a nice day", 
            "It's a lovely day, isn't it?"
            ]

sent_messages =[]

#send_messages (messages, sent_messages)
#print(f"This is the original list : {messages}")
#print(f"This is the new list : {sent_messages}")

send_messages(messages[:],sent_messages)
print(f"This is the original list : {messages}")