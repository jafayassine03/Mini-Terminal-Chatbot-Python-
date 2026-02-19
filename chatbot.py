import json
import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

MEMORY_FILE = "memory.json"
LOG_FILE = "chat_log.txt"


class ChatBot:
    def __init__(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    def save_memory(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    def log(self, message):
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - {message}\n")

    def get_time(self):
        return datetime.now().strftime("%H:%M")

    def get_date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def greet(self):
        print(Fore.GREEN + "Bot: Hello! 👋\n")
        print(Fore.YELLOW + "Bot: Type 'help' to see what I can do.\n")

    def chat(self):
        self.greet()
        while True:
            user_input = input(Fore.CYAN + "You: " + Style.RESET_ALL).lower().strip()
            self.log(f"You: {user_input}")

            if user_input in ["hi", "hello", "hey"]:
                response = "Hello!"
            elif "how are you" in user_input:
                response = "I'm doing great! Thanks for asking 😊"
            elif "time" in user_input:
                response = f"Current time is {self.get_time()}"
            elif "date" in user_input:
                response = f"Today's date is {self.get_date()}"
            elif user_input == "help":
                response = (
                    "I can respond to:\n"
                    "- greetings (hi, hello, hey)\n"
                    "- how are you\n"
                    "- time / date\n"
                    "- exit / quit / bye"
                )
            elif user_input in ["exit", "quit", "bye"]:
                response = "Goodbye! See you soon 👋"
                print(Fore.MAGENTA + f"Bot: {response}")
                self.log(f"Bot: {response}")
                break
            else:
                response = "Hmm… I don't understand that yet 🤔"

            print(Fore.MAGENTA + f"Bot: {response}")
            self.log(f"Bot: {response}")


if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
