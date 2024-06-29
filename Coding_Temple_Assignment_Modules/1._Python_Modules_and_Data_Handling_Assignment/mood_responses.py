def mood_response(mood):
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "Awesome! What's got you so pumped?",
        "tired": "Make sure to get some rest!",
        "angry": "It's okay to feel angry sometimes. Take a deep breath."
    }
    
    # Default response if mood is not recognized
    return responses.get(mood.lower(), "I hope you have a good day, no matter what!")
