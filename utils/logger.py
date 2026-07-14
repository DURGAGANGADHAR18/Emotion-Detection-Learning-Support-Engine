import csv
import os
from datetime import datetime

FILE = "history/history.csv"

os.makedirs("history", exist_ok=True)

def save_history(field, text, emotion, confidence, model, response):

    print("✅ save_history() called")

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "field",
                "text",
                "emotion",
                "confidence",
                "model",
                "response"
            ])

        writer.writerow([
            datetime.now(),
            field,
            text,
            emotion,
            confidence,
            model,
            response
        ])

    print("✅ History saved successfully")