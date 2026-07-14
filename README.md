# 🎓 Emotion Detection and Learning Support Engine

An AI-powered web application that detects students' learning emotions from text and provides personalized learning support using **BERT**, **Multi-label BiLSTM**, and **Google Gemini AI**.

---

## 📖 Project Overview

The **Emotion Detection and Learning Support Engine** is designed to analyze students' learning-related text, identify their emotional state, and provide personalized learning guidance. The system combines Natural Language Processing (NLP), Deep Learning, and Generative AI to enhance students' learning experiences.

---

## ✨ Features

- 🤖 BERT-based Emotion Detection
- 🧠 Multi-label BiLSTM Emotion Detection
- 💡 AI-Powered Learning Guidance using Google Gemini
- 📊 Emotion Analytics Dashboard
- 📚 Subject-wise Emotion Analysis
- 📈 Emotion Confidence Scores
- 📝 Prediction History Logging
- 📥 Download AI Response
- 🎨 Interactive Streamlit Interface

---

## 😊 Supported Emotions

- Curious
- Confused
- Frustrated
- Confident
- Bored

---

## 🏗️ System Architecture

```
Student Input
      │
      ▼
Text Preprocessing
      │
      ▼
BERT Emotion Detection
      │
      ▼
Multi-label BiLSTM Prediction
      │
      ▼
Rule-based Emotion Enhancement
      │
      ▼
Emotion Analysis
      │
      ▼
Google Gemini AI
      │
      ▼
Personalized Learning Support
      │
      ▼
Analytics Dashboard
```

---

## 📂 Project Structure

```
Emotion_Detection_and_Learning_Support_Engine/

│── app.py
│── requirements.txt
│── README.md
│
├── datasets/
├── docs/
├── history/
├── models/
│   ├── bert/
│   ├── bert_v2/
│   ├── bilstm/
│   └── bilstm_multilabel/
│
├── training/
│
└── utils/
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- TensorFlow
- Keras
- Hugging Face Transformers
- Google Gemini API
- Pandas
- NumPy
- Plotly
- Scikit-learn

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Emotion-Detection-and-Learning-Support-Engine.git
```

Navigate to the project

```bash
cd Emotion-Detection-and-Learning-Support-Engine
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 Google Gemini API Setup

Create a free API key from:

https://aistudio.google.com/app/apikey

Configure your API key in the application before running the project.

---

## 🤖 Models Used

### BERT

- Transformer-based emotion classification
- Predicts primary and secondary emotions
- Fine-tuned for educational emotion analysis

### Multi-label BiLSTM

Architecture:

- Embedding Layer
- Bidirectional LSTM
- Dropout Layers
- Dense Layer
- Sigmoid Output Layer

Supports simultaneous detection of multiple emotions.

---

## 📊 Dashboard

The dashboard includes:

- Emotion Distribution
- Confidence Score Visualization
- Prediction History
- Student Emotion Trends
- Analytics Charts

---

## 📸 Screenshots

- Home Page
- Emotion Prediction Results
- AI Learning Guidance
- Analytics Dashboard

---

## 📄 Output

The application provides:

- Primary Emotion
- Secondary Emotion
- Multiple Emotion Detection
- Emotion Confidence Scores
- Personalized Learning Support
- Prediction History

---

## 🔮 Future Enhancements

- Voice Emotion Detection
- Facial Emotion Recognition
- Student Progress Tracking
- Adaptive Learning Recommendations
- Cloud Deployment
- Mobile Application
- Multi-language Support

---

## 👨‍💻 Developer

**Gangadhar**

B.Tech – Computer Science and Engineering

Seshadri Rao Gudlavalleru Engineering College (SRGEC)

---

## 📜 License

This project is developed for educational and academic purposes.

---

## ⭐ Support

If you found this project useful, please give this repository a ⭐ on GitHub.
