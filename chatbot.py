import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def get_time():
    return datetime.now().strftime("%H:%M")


def get_date():
    return datetime.now().strftime("%Y-%m-%d")


def chatbot():
    memory = load_memory()

    if "name" not in memory:
        name = input("Bot: Hi! What's your name? \nYou: ").strip()
        memory["name"] = name
        save_memory(memory)
        print(f"Bot: Nice to meet you, {name} ")
    else:
        print(f"Bot: Welcome back, {memory['name']} 👋")

    print("Bot: Type 'help' to see what I can do.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hi", "hello", "hey"]:
            print(f"Bot: Hello {memory['name']}!")

        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking ")

        elif "time" in user_input:
            print(f"Bot: Current time is {get_time()} ")

        elif "date" in user_input:
            print(f"Bot: Today's date is {get_date()} ")

        elif user_input == "help":
            print(
                "Bot: I can respond to:\n"
                "- greetings (hi, hello)\n"
                "- how are you\n"
                "- time / date\n"
                "- exit"
            )

        elif user_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! See you soon ")
            break

        else:
            print("Bot: Hmm… I don't understand that yet ")


if __name__ == "__main__":
    chatbot()
