class ChatBot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "hello": "Hi! 😊 How can I help you today?",
            "hi": "Hello! Nice to meet you.",
            "hey": "Hey! What can I do for you?",
            
            "how are you": "I'm doing great! Thanks for asking. How about you?",
            "i am fine": "That's good to hear! 😊",
            "i am sad": "I'm sorry to hear that. I hope things get better soon.",

            "your name": f"My name is {name}. I'm a simple AI chatbot.",
            "who are you": "I'm an AI assistant created to chat and answer basic questions.",

            "what can you do": "I can answer simple questions, have conversations, and help you with basic information.",

            "what is python": "Python is a popular programming language used for web development, automation, data science, and AI.",
            "what is ai": "AI stands for Artificial Intelligence. It enables machines to learn, think, and make decisions.",

            "what is machine learning": "Machine Learning is a part of AI where computers learn patterns from data to make predictions.",

            "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",

            "what time": "I don't have access to real-time data yet, but you can check your device clock.",

            "thank you": "You're welcome! 😊",
            "thanks": "Happy to help!",

            "what are you doing": "I'm chatting with you and waiting for your next question.",

            "i love programming": "That's great! Keep learning and building projects. 🚀",

            "bye": "Goodbye! It was nice talking with you. Have a great day!"
        }

    def reply(self, user_message):
        user_message = user_message.lower()

        for question, answer in self.responses.items():
            if question in user_message:
                return answer

        return "I'm still learning. Can you ask me something else?"
        

bot = ChatBot("Nova")

print("Nova: Hi! Type 'bye' to exit.")

while True:
    user = input("You: ")

    print("Nova:", bot.reply(user))

    if "bye" in user.lower():
        break