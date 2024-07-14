import nltk
from nltk.chat.util import Chat, reflections

# Sample conversations
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by ChatGPT.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you!", "I'm fine, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"how old are you?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"what is your favorite (.*)?",
        ["I don't have favorites, but I like to help people.",]
    ],
    [
        r"quit",
        ["Bye, take care!", "Goodbye! See you soon!",]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Can you rephrase?",]
    ],
]

def chatbot():
    print("Hi! I am a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
