def chatbot():
    print("Chatbot: Hi! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("user: ").lower().strip()

        if user_input == "bye":
            print("Chatbot: Goodbye! Thank You for Visiting..")
            break

        elif user_input in ["hi","hello","hey"]:
            print("Chatbot: Hello there! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of python code but I'm doing great! How about you?")
        
        elif user_input in ["i am fine", "i am good","good","fine"]:
            print("Chatbot: That's nice to hear!")
        
        elif "your name" in user_input:
            print("Chatbot: I'm Chatbot, your friend with NLP logic.")
        
        elif "time" in user_input:
            print("ChatBot: Sorry I don'y have a watch. Python can help if you teach me!")
        
        elif "who created you" in user_input:
            print("Chatbot: I was created by Vamsi Krishna who is Professional in python conditionals.")
        
        elif "what can you do" in user_input:
            print("Chatbot: I can talk with you using simple rules. Try asking me simple questions!")
        
        elif "weather" in user_input:
            print("Chatbot: I'm not connected to the internet, so I can't provide real-time weather updates.")
        
        elif user_input in ["joke","make a joke", "play a joke"]:
            print("Chatbot: Why did the python programmer go hungry? Because their food was byte-sized!")
        
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! Happy to help.")
        
        elif "help" in user_input:
            print("Chatbot: You can ask me about my name, how I'm doing, the time or just say hi!")
        
        elif "favorite color" in user_input:
            print("Chatbot: I don't have eyes, but I like the color Blue!")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day...")
        else:
            print("Chatbot: I'm not sure how to respond to that. can you rephrase?")
            
chatbot()