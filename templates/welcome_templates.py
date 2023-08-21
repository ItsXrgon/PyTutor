import math
import random

def get_welcome_message():
    key = str(math.ceil(6 * random.random()))
    return welcome_messages[key]

welcome_messages = {
    "1": "Hello, How can I help you with Python?",
    "2": "Hi, Any coding questions?",
    "3": "Hello! Ask away!",
    "4": "Greetings! Ready to dive into Python?",
    "5": "Hey there! Curious about Python programming?",
    "6": "Welcome! Let's explore the world of Python coding!"
}

