def get_response(emotion):
    responses = {
        "Frustrated": "Take a short break and solve one small problem at a time.",
        "Confused": "Review the basics and try a simple example first.",
        "Curious": "Great! Explore more examples and ask questions.",
        "Confident": "Excellent! Challenge yourself with harder problems.",
        "Bored": "Try learning through videos or practical projects.",
        "Unknown": "Please provide more details about your study problem."
    }

    return responses.get(emotion, "Keep learning!")