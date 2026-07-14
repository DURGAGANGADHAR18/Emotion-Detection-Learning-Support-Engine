import os
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from utils.emotion_rules import apply_emotion_rules

# --------------------------------------------------
# Paths
# --------------------------------------------------

MODEL_DIR = "models/bilstm_multilabel"

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "bilstm_multilabel.keras"
)

TOKENIZER_PATH = os.path.join(
    MODEL_DIR,
    "tokenizer.pkl"
)

LABELS_PATH = os.path.join(
    MODEL_DIR,
    "labels.txt"
)

MAX_LENGTH = 80

# --------------------------------------------------
# Load Model
# --------------------------------------------------

print("\nLoading Multi-label BiLSTM...")

model = load_model(MODEL_PATH)

with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

with open(LABELS_PATH, "r", encoding="utf-8") as f:
    LABELS = [line.strip() for line in f.readlines()]

print("Loaded Successfully.")

# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict_multilabel_bilstm(text, threshold=0.25):

    sequence = tokenizer.texts_to_sequences([text])

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    probabilities = model.predict(
        padded,
        verbose=0
    )[0]

    print("\n==============================")
    print("RAW MODEL OUTPUT")
    print("==============================")

    scores = {}

    for label, score in zip(LABELS, probabilities):
        score = float(score)
        scores[label] = score
        print(f"{label:12}: {score:.4f}")

    # --------------------------------------------------
    # Rule Enhancement
    # --------------------------------------------------

    scores = apply_emotion_rules(text, scores)

    print("\nAfter Rules:")
    for k, v in scores.items():
        print(k, ":", v)

    print("\n==============================")
    print("AFTER RULE ENHANCEMENT")
    print("==============================")

    for emotion, score in scores.items():
        print(f"{emotion:12}: {score:.4f}")

    # --------------------------------------------------
    # Sort Scores
    # --------------------------------------------------

    sorted_scores = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    primary_emotion = sorted_scores[0][0]
    primary_confidence = sorted_scores[0][1]

    # --------------------------------------------------
    # Mixed Emotions
    # --------------------------------------------------

    detected = []

    for emotion, score in sorted_scores:

        if score >= threshold:

            detected.append({
                "emotion": emotion,
                "confidence": score
            })

    if len(detected) == 0:

        detected.append({
            "emotion": primary_emotion,
            "confidence": primary_confidence
        })

    # Keep only Top-2 emotions
    detected = detected[:2]

    print("\n==============================")
    print("FINAL PREDICTION")
    print("==============================")

    print("Primary Emotion :", primary_emotion)
    print("Confidence      :", round(primary_confidence, 4))
    print("Detected        :", detected)

    return {

        "emotion": primary_emotion,

        "confidence": primary_confidence,

        "mixed_emotions": detected,

        "scores": scores,

        "model": "BiLSTM Multi-label"

    }