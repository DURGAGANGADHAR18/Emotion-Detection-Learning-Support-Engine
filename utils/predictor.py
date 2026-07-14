import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = "models/bert_v2"

tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# -----------------------------
# Load Labels Automatically
# -----------------------------
labels_path = os.path.join(MODEL_PATH, "labels.txt")

with open(labels_path, "r", encoding="utf-8") as f:
    LABELS = [line.strip() for line in f.readlines()]

# -----------------------------
# Prediction Function
# -----------------------------
def predict_emotion(text):

    # ---------------------------------
    # Preprocess contrast sentences
    # ---------------------------------
    text_lower = text.lower()

    connectors = [
        " but ",
        " however ",
        " although ",
        " yet ",
        " though "
    ]

    for connector in connectors:
        if connector in text_lower:
            index = text_lower.find(connector)
            text = text[index + len(connector):].strip()
            break

    # ---------------------------------
    # Tokenize
    # ---------------------------------
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=64
    )

    # ---------------------------------
    # Predict
    # ---------------------------------
    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)[0]

    scores = {}

    for i, label in enumerate(LABELS):
        scores[label] = float(probabilities[i])

    sorted_scores = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    primary_emotion = sorted_scores[0][0]
    primary_score = sorted_scores[0][1]

    secondary_emotion = sorted_scores[1][0]
    secondary_score = sorted_scores[1][1]

    return {
        "emotion": primary_emotion,
        "confidence": primary_score,
        "secondary_emotion": secondary_emotion,
        "secondary_confidence": secondary_score,
        "scores": scores
    }