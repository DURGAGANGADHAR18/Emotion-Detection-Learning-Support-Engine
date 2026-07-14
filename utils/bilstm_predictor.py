import os
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ---------------------------------------------------
# Model Path
# ---------------------------------------------------

MODEL_DIR = "models/bilstm"

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

print("\n======================================")
print("Loading BiLSTM Model...")
print("======================================")

model = load_model(
    os.path.join(MODEL_DIR, "bilstm_model.keras")
)

print("✓ Model Loaded")

# ---------------------------------------------------
# Load Tokenizer
# ---------------------------------------------------

with open(
    os.path.join(MODEL_DIR, "tokenizer.pkl"),
    "rb"
) as f:
    tokenizer = pickle.load(f)

print("✓ Tokenizer Loaded")

# ---------------------------------------------------
# Load Label Encoder
# ---------------------------------------------------

with open(
    os.path.join(MODEL_DIR, "label_encoder.pkl"),
    "rb"
) as f:
    label_encoder = pickle.load(f)

print("✓ Label Encoder Loaded")

print("\nEmotion Classes:")
print(label_encoder.classes_)

print("\nModel Directory:")
print(os.path.abspath(MODEL_DIR))

print("======================================\n")

MAX_LENGTH = 80


# ---------------------------------------------------
# Text Preprocessing
# ---------------------------------------------------

def preprocess_text(text):

    text_lower = text.lower()

    connectors = [
        " but ",
        " however ",
        " although ",
        " though ",
        " yet "
    ]

    for connector in connectors:

        if connector in text_lower:

            idx = text_lower.find(connector)

            text = text[idx + len(connector):].strip()

            print("\nDetected Connector :", connector.strip())
            print("Using Important Part:")
            print(text)

            break

    return text


# ---------------------------------------------------
# Prediction Function
# ---------------------------------------------------

def predict_bilstm(text):

    print("\n======================================")
    print("BiLSTM Prediction")
    print("======================================")

    print("Original Input:")
    print(text)

    # ---------- Preprocess ----------
    text = preprocess_text(text)

    sequence = tokenizer.texts_to_sequences([text])

    print("\nTokenized Sequence:")
    print(sequence)

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )

    prediction = model.predict(
        padded,
        verbose=0
    )[0]

    scores = {}

    print("\nEmotion Scores")
    print("-" * 35)

    for label, score in zip(label_encoder.classes_, prediction):

        scores[label] = float(score)

        print(f"{label:12s}: {score:.6f}")

    print("-" * 35)

    emotion = max(scores, key=scores.get)
    confidence = scores[emotion]

    print("\nPredicted Emotion :", emotion)
    print("Confidence        :", round(confidence * 100, 2), "%")

    print("======================================\n")

    return {
        "emotion": emotion,
        "confidence": confidence,
        "scores": scores,
        "model": "BiLSTM"
    }