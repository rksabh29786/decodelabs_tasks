# ==========================================
# DecodeLabs AI Internship Project 1
# Rule-Based AI Chatbot
#
# Developed by: Muhammad Ramzan
# Language: Python
# ==========================================

from datetime import datetime


# ==========================
# Welcome Message
# ==========================
def show_welcome():
    print("=" * 55)
    print("        DecodeLabs Rule-Based AI Chatbot")
    print("=" * 55)
    print("Hello! 👋")
    print("I am AI_ChatBot.")
    print("I am here to answer some basic questions.")
    print("\nType 'help' to see available commands.")
    print("Type 'exit', 'bye', or 'quit' to end the chat.")
    print("=" * 55)


# ==========================
# Chatbot Response Function
# ==========================
def get_response(user):

    user = user.lower().strip()

    # Empty input
    if user == "":
        return "Please type something."

    # Greetings
    elif user in ["hello", "hi", "hey"]:
        return "Hello! Nice to meet you."

    # How are you
    elif user == "how are you":
        return "I am doing great! Thanks for asking."

    # Bot name
    elif user in ["your name", "what is your name"]:
        return "My name is AI_ChatBot."

    # Creator
    elif user == "who made you":
        return "I was created by Muhammad Ramzan for the DecodeLabs AI Internship."

    # AI
    elif user == "what is ai":
        return "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence."

    # Python
    elif user == "python":
        return "Python is a popular programming language used in AI, web development, automation, and data science."

    # Internship
    elif user == "internship":
        return "This chatbot is my Project 1 for the DecodeLabs Artificial Intelligence Internship."

    # Time
    elif user == "time":
        return "Current Time: " + datetime.now().strftime("%I:%M:%S %p")

    # Date
    elif user == "date":
        return "Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    # Joke
    elif user == "joke":
        return "Why do programmers prefer dark mode?\nBecause light attracts bugs!"

    # Motivation
    elif user == "motivate me":
        return "Success is the sum of small efforts repeated every day."

    # Weather
    elif user == "weather":
        return "Sorry, I cannot check live weather because I work without internet."

    # Favorite color
    elif user == "favorite color":
        return "I like blue because it represents technology and trust."

    # Thanks
    elif user in ["thanks", "thank you"]:
        return "You're welcome! Happy to help."

    # Help
    elif user == "help":
        return """
Available Commands

• hello
• hi
• hey
• how are you
• your name
• who made you
• what is ai
• python
• internship
• date
• time
• joke
• motivate me
• weather
• favorite color
• thanks
• help
• exit
"""

    # Unknown Question
    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."


# ==========================
# Main Function
# ==========================
def main():

    show_welcome()

    while True:

        user = input("\nYou: ")

        if user.lower().strip() in ["exit", "bye", "quit"]:

            print("\nBot: Thank you for chatting with me.")
            print("Bot: Have a wonderful day! 😊")
            break

        response = get_response(user)

        print("\nBot:", response)


# ==========================
# Run Program
# ==========================
if __name__ == "__main__":
    main()