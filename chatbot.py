print("ChatBot: Hi! I'm your chatbot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("ChatBot: Hello... How are you?")
    elif user == "fine" or user == "good":
        print("ChatBot: That's great to hear...")
    elif user == "what is your name":
        print("ChatBot: I'm a simple chatbot created in Python.")
    elif user == "bye":
        print("ChatBot: Goodbye... Have a nice day.")
        break
    else:
        print("ChatBot: Sorry, I don't understand that.")