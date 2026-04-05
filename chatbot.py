import random
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)


class ChatBot:
    def __init__(self):
        self.name = None
        self.mood = "neutral"
        self.history = []  #conversation history

        self.greetings = ["Hello!", "Hey there!", "Hii", "What's up!"]
        self.how_are_you_responses = [
            "I'm doing great ",
            "Feeling awesome today!",
            "All good here!",
        ]

    def banner(self):
        print(Fore.YELLOW + "Simple Smart ChatBot")
        print(Fore.YELLOW + "Type 'help' for commands.\n")

    def get_time(self):
        return datetime.now().strftime("Current time: %H:%M")

    def get_date(self):
        return datetime.now().strftime("Today's date: %Y-%m-%d")

    def tell_joke(self):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs 🐛",
            "Why did Python go to therapy? Too many issues.",
            "I would tell you a UDP joke… but you might not get it."
        ]
        return random.choice(jokes)

    def detect_mood(self, text):
        if any(word in text for word in ["sad", "upset", "tired"]):
            self.mood = "sad"
            return "I'm here for you. Want to talk about it?"
        if any(word in text for word in ["happy", "great", "good"]):
            self.mood = "happy"
            return "I love that energy 😄"
        return None

    def calculate(self, expression):
        try:
            result = eval(expression)  # simple calculator
            return f"Result: {result}"
        except:
            return "Invalid calculation ❌"

    def show_history(self):
        if not self.history:
            return "No history yet."
        return "\n".join(self.history[-5:])  # last 5 messages

    def help_menu(self):
        return (
            "Commands:\n"
            "- hi / hello\n"
            "- my name is <name>\n"
            "- how are you\n"
            "- time\n"
            "- date\n"
            "- joke\n"
            "- calculate <math>\n"
            "- history\n"
            "- exit"
        )

    def run(self):
        self.banner()

        while True:
            user_input = input(Fore.CYAN + "You: " + Style.RESET_ALL).strip().lower()

            # store user input
            self.history.append(f"You: {user_input}")

            if user_input in ["exit", "quit", "bye"]:
                print(Fore.MAGENTA + "Bot: Goodbye 👋")
                break

            if user_input in ["hi", "hello", "hey"]:
                response = random.choice(self.greetings)
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if user_input.startswith("my name is"):
                self.name = user_input.replace("my name is", "").strip().title()
                response = f"Nice to meet you, {self.name}!"
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if "how are you" in user_input:
                response = random.choice(self.how_are_you_responses)
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if user_input == "time":
                response = self.get_time()
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if user_input == "date":
                response = self.get_date()
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if user_input == "joke":
                response = self.tell_joke()
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if user_input.startswith("calculate"):
                expression = user_input.replace("calculate", "").strip()
                response = self.calculate(expression)
                print(Fore.MAGENTA + f"Bot: {response}")
                self.history.append(f"Bot: {response}")
                continue

            if user_input == "history":
                response = self.show_history()
                print(Fore.MAGENTA + f"Bot:\n{response}")
                continue

            if user_input == "help":
                response = self.help_menu()
                print(Fore.MAGENTA + f"Bot: {response}")
                continue

            mood_response = self.detect_mood(user_input)
            if mood_response:
                print(Fore.MAGENTA + f"Bot: {mood_response}")
                self.history.append(f"Bot: {mood_response}")
                continue

            response = "Hmm… I’m still learning 🤔"
            print(Fore.MAGENTA + f"Bot: {response}")
            self.history.append(f"Bot: {response}")


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()