def show_messages (messages, sent_messsages):
    while messages:
        current_message = messages.pop(0)
        print(f"I'm printing this message : {current_message}")
        sent_messsages.append(current_message)

messages =[
    "Hi, how are you doing?",
    "Are we expecting you ?",
    "How much are we making ?",
    "We have to make improvements"
]

sent_messages =[ ]

show_messages(messages[:], sent_messages)

print(f"\nThis is the original list : {messages}\n")
print(f"This is the new list : {sent_messages}")


