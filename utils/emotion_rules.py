# utils/emotion_rules.py

def apply_emotion_rules(text, scores):

    text = text.lower()

    # ---------- Curious ----------
    if any(word in text for word in [
        "curious",
        "interested",
        "enjoy",
        "love",
        "explore",
        "learn",
        "want to learn",
        "want to know"
    ]):
        scores["Curious"] = min(scores.get("Curious", 0) + 0.35, 1.0)

    # ---------- Confused ----------
    if any(word in text for word in [
        "confused",
        "confusing",
        "don't understand",
        "cannot understand",
        "difficult",
        "hard"
    ]):
        scores["Confused"] = min(scores.get("Confused", 0) + 0.25, 1.0)

    # ---------- Frustrated ----------
    if any(word in text for word in [
        "frustrated",
        "frustrating",
        "stuck",
        "error",
        "problem",
        "issue",
        "bug"
    ]):
        scores["Frustrated"] = min(scores.get("Frustrated", 0) + 0.25, 1.0)

    # ---------- Confident ----------
    if any(word in text for word in [
        "confident",
        "easy",
        "i can",
        "i know",
        "mastered",
        "successfully",
        "comfortable",
        "execellent",
        "solved",
        "understand well"
    ]):
        scores["Confident"] = min(scores.get("Confident", 0) + 0.25, 1.0)

    # ---------- Bored ----------
    if any(word in text for word in [
        "bored",
        "boring",
        "sleepy",
        "lazy",
        "lose interest"
    ]):
        scores["Bored"] = min(scores.get("Bored", 0) + 0.25, 1.0)

    return scores