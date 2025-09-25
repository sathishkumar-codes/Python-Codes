import datetime
import random

print("ChatBot: Hi! I'm your chatbot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("ChatBot: Hello! How are you?")
    
    elif user in ["fine", "good", "great", "awesome"]:
        print("ChatBot: That's great to hear!")
    
    elif user == "what is your name":
        print("ChatBot: I'm a simple chatbot created in Python.")
    
    elif user == "what time is it":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"ChatBot: The current time is {now}")
    
    elif user == "what is the date":
        today = datetime.date.today().strftime("%d-%m-%Y")
        print(f"ChatBot: Today's date is {today}")
    
    elif user == "tell me a joke":
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why was the computer cold? It left its Windows open!"
        ]
        print("ChatBot: " + random.choice(jokes))
    
    elif user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break
    
    else:
        print("ChatBot: Sorry, I don't understand that.")
