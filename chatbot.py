import random
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)


class ChatBot:
    def __init__(self):
        self.name = None
        self.mood = "neutral"

        self.greetings = ["Hello!", "Hey there!", "Hi 👋", "What's up!"]
        self.how_are_you_responses = [
            "I'm doing great 😄",
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

    def help_menu(self):
        return (
            "Commands:\n"
            "- hi / hello\n"
            "- my name is <name>\n"
            "- how are you\n"
            "- time\n"
            "- date\n"
            "- joke\n"
            "- exit"
        )

    def run(self):
        self.banner()

        while True:
            user_input = input(Fore.CYAN + "You: " + Style.RESET_ALL).strip().lower()

            if user_input in ["exit", "quit", "bye"]:
                print(Fore.MAGENTA + "Bot: Goodbye 👋")
                break

            if user_input in ["hi", "hello", "hey"]:
                print(Fore.MAGENTA + f"Bot: {random.choice(self.greetings)}")
                continue

            if user_input.startswith("my name is"):
                self.name = user_input.replace("my name is", "").strip().title()
                print(Fore.MAGENTA + f"Bot: Nice to meet you, {self.name}!")
                continue

            if "how are you" in user_input:
                print(Fore.MAGENTA + f"Bot: {random.choice(self.how_are_you_responses)}")
                continue

            if user_input == "time":
                print(Fore.MAGENTA + f"Bot: {self.get_time()}")
                continue

            if user_input == "date":
                print(Fore.MAGENTA + f"Bot: {self.get_date()}")
                continue

            if user_input == "joke":
                print(Fore.MAGENTA + f"Bot: {self.tell_joke()}")
                continue

            if user_input == "help":
                print(Fore.MAGENTA + f"Bot: {self.help_menu()}")
                continue

            mood_response = self.detect_mood(user_input)
            if mood_response:
                print(Fore.MAGENTA + f"Bot: {mood_response}")
                continue

            print(Fore.MAGENTA + "Bot: Hmm… I’m still learning 🤔")


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()