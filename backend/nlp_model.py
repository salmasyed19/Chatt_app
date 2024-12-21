import random

def process_message(message):
    genz_dict = {
        "hello": ["yo", "sup", "hey"],
        "how are you": ["I'm vibing", "chillin", "doing awesome"],
        "bye": ["laters", "catch ya", "peace out"]
    }
    
    for word, responses in genz_dict.items():
        if word in message.lower():
            message = message.replace(word, random.choice(responses))
    
    return message
