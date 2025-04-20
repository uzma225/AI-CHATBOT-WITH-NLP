# chatbot.py

from nltk.chat.util import Chat, reflections

# Pattern-response pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created for Task 3.", "You can call me PyBot."]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great!", "All good! How about you?"]
    ],
    [
        r"(.*) help (.*)",
        ["I'm here to help. Please ask your question."]
    ],
    [
        r"quit",
        ["Goodbye!", "See you soon!"]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
def start_chat():
    print("Hi, I'm your chatbot for Task 3. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
