import random
import pandas as pd


subjects = [
    "Python",
    "Java",
    "C Programming",
    "C++",
    "Data Structures",
    "Algorithms",
    "DBMS",
    "Operating Systems",
    "Computer Networks",
    "Machine Learning",
    "Artificial Intelligence",
    "Deep Learning",
    "Data Science",
    "Cyber Security",
    "Cloud Computing",
    "Software Engineering",
    "Discrete Mathematics",
    "Statistics",
    "Physics",
    "Chemistry",
    "Mathematics",
    "Biology",
    "Web Development",
    "Android Development",
    "React",
    "SQL"
]

confused = [

"I don't understand {}.",
"I'm confused about {}.",
"I cannot understand the basics of {}.",
"I don't know where to start learning {}.",
"The concepts in {} are confusing.",
"I keep mixing up the topics in {}.",
"I don't understand the explanation in {}.",
"The examples in {} confuse me.",
"I am unable to solve questions in {}.",
"I don't know why my answers in {} are wrong.",
"I cannot understand the teacher's explanation of {}.",
"I feel lost while studying {}.",
"I don't know what this topic means in {}.",
"I keep forgetting concepts in {}.",
"I don't understand the syntax used in {}.",
"I cannot identify my mistakes in {}.",
"I don't know how to approach {} problems.",
"I get confused between different concepts in {}.",
"I find {} difficult to understand.",
"I don't understand the logic behind {}."

]

frustrated = [

"I am frustrated with {}.",
"I have been trying {} for hours without success.",
"I feel stuck while learning {}.",
"I cannot solve {} problems.",
"My code keeps failing in {}.",
"I am tired of debugging {}.",
"I keep getting errors in {}.",
"I feel like giving up on {}.",
"I worked hard but still cannot understand {}.",
"I spend hours studying {} but make no progress.",
"I always make mistakes in {}.",
"I feel stressed while learning {}.",
"I cannot finish my {} assignment.",
"I am disappointed with my performance in {}.",
"I don't know why {} is so difficult.",
"I am exhausted because of {}.",
"I cannot complete my {} project.",
"I feel overwhelmed by {}.",
"I lose confidence while studying {}.",
"I hate solving {} questions."

]

curious = [

"I want to know more about {}.",
"I'm curious about advanced concepts in {}.",
"I enjoy exploring {}.",
"I want to build projects using {}.",
"I want to learn the latest technologies in {}.",
"I like experimenting with {}.",
"I enjoy reading about {}.",
"I want deeper knowledge of {}.",
"I am excited to study {}.",
"I want to become an expert in {}."

]

confident = [

"I understand {} very well.",
"I solved all {} problems correctly.",
"I am confident in {}.",
"I completed my {} assignment successfully.",
"I enjoy solving {} questions.",
"I can explain {} to my classmates.",
"I scored high marks in {}.",
"I can build projects using {}.",
"I learn {} quickly.",
"I feel prepared for my {} exam."

]

bored = [

"I feel bored while studying {}.",
"{} is becoming repetitive.",
"I lose focus during {} lectures.",
"I don't enjoy studying {} anymore.",
"I find {} uninteresting.",
"I feel sleepy while learning {}.",
"I cannot stay motivated in {}.",
"I keep getting distracted while studying {}.",
"I don't feel excited about {}.",
"I find {} monotonous."

]

subjects = [
    "Python", "Java", "C", "C++", "DBMS", "Operating Systems",
    "Computer Networks", "Data Structures", "Algorithms",
    "Machine Learning", "Artificial Intelligence",
    "Mathematics", "Physics", "Chemistry"
]

confused = [
    "I don't understand {}.",
    "I am confused about {}.",
    "The concepts in {} are difficult for me.",
    "I cannot understand the basics of {}.",
    "The examples in {} confuse me."
]

frustrated = [
    "I am frustrated with {}.",
    "No matter how much I study {}, I keep making mistakes.",
    "Debugging {} programs is exhausting.",
    "I feel stuck while learning {}.",
    "{} is making me lose my confidence."
]

curious = [
    "I want to learn more about {}.",
    "I am curious about advanced {} concepts.",
    "{} seems interesting and I want to explore it.",
    "I enjoy reading about {}.",
    "I want to build projects using {}."
]

confident = [
    "I solved all {} exercises successfully.",
    "I feel confident in {}.",
    "I can explain {} to my classmates.",
    "I completed my {} assignment without help.",
    "I understand {} very well."
]

bored = [
    "{} feels repetitive.",
    "I am bored while studying {}.",
    "{} lectures are not interesting.",
    "I lose focus during {} class.",
    "I don't enjoy studying {} anymore."
]

templates = {
    "Confused": confused,
    "Frustrated": frustrated,
    "Curious": curious,
    "Confident": confident,
    "Bored": bored
}

# ---------------------------------------------
# Mixed Emotion Templates
# ---------------------------------------------

mixed_templates = [

    ("Confused", "Frustrated",
     [
         "I don't understand {} and it's making me frustrated.",
         "I'm confused about {} because nothing seems to work.",
         "I keep making mistakes in {} and I'm getting frustrated.",
         "The concepts in {} are confusing and stressful.",
         "I can't solve {} problems no matter how much I practice.",
         "I don't know where I'm going wrong in {}.",
         "Studying {} makes me feel confused and overwhelmed.",
         "I tried everything but {} still doesn't make sense.",
         "I feel lost while learning {} and it's frustrating.",
         "I don't understand {} and I'm losing confidence."
     ]),

    ("Curious", "Confident",
     [
         "I understand {} well and want to learn advanced topics.",
         "I'm confident in {} and excited to explore more.",
         "I enjoy {} and want to build real projects.",
         "I mastered the basics of {} and want more challenges.",
         "I'm doing well in {} and I'm curious about advanced concepts.",
         "I love solving {} problems and learning new tricks.",
         "I'm confident enough to teach others {}.",
         "I want to explore research in {}.",
         "I'm excited to learn professional applications of {}.",
         "I enjoy experimenting with {} every day."
     ]),

    ("Bored", "Frustrated",
     [
         "{} feels repetitive and I can't stay motivated.",
         "I'm bored with {} and frustrated because I don't improve.",
         "Studying {} feels like a burden.",
         "I lose interest quickly while learning {}.",
         "I don't enjoy {} anymore because it is difficult.",
         "{} is boring and stressful at the same time.",
         "I cannot concentrate on {} lectures.",
         "Assignments in {} are repetitive and frustrating.",
         "I feel bored even before opening my {} notes.",
         "I wish {} were more interesting."
     ]),

    ("Confused", "Curious",
     [
         "I'm confused about {} but I really want to understand it.",
         "{} looks difficult but I'm excited to learn it.",
         "I don't understand {} yet but I'm interested.",
         "I want to know how {} actually works.",
         "{} is confusing but fascinating.",
         "I keep asking questions because {} interests me.",
         "I hope to master {} even though I'm confused.",
         "{} is difficult but worth learning.",
         "I enjoy discovering new ideas in {} despite being confused.",
         "I want to explore {} more deeply."
     ]),

    ("Frustrated", "Confident",
     [
         "I struggled with {} but I know I'll master it.",
         "I'm frustrated today but confident I'll improve in {}.",
         "Although {} is difficult, I believe I can solve it.",
         "I'm making mistakes in {} but I'm learning from them.",
         "I know I'll eventually become good at {}.",
         "Every error in {} teaches me something.",
         "I failed before but I'm confident about {} now.",
         "Practice will help me master {}.",
         "I'm determined to improve in {}.",
         "I won't give up learning {}."
     ])

]

# -------------------------------------------------------
# Dataset Generation
# -------------------------------------------------------

rows = []

# ---------- Single Emotion Samples ----------
single_templates = {
    "Confused": confused,
    "Frustrated": frustrated,
    "Curious": curious,
    "Confident": confident,
    "Bored": bored
}

for emotion, templates in single_templates.items():

    for _ in range(800):      # 800 × 5 = 4000 rows

        sentence = random.choice(templates).format(
            random.choice(subjects)
        )

        rows.append({
            "text": sentence,
            "primary_emotion": emotion,
            "secondary_emotion": ""
        })


# ---------- Mixed Emotion Samples ----------

for primary, secondary, templates in mixed_templates:

    for _ in range(200):      # 200 × 5 = 1000 rows

        sentence = random.choice(templates).format(
            random.choice(subjects)
        )

        rows.append({
            "text": sentence,
            "primary_emotion": primary,
            "secondary_emotion": secondary
        })


# Shuffle Dataset

random.shuffle(rows)

# -------------------------------------------------------
# Remove Duplicates
# -------------------------------------------------------

import pandas as pd

df = pd.DataFrame(rows)

# Remove duplicate sentences
df.drop_duplicates(subset=["text"], inplace=True)

# Shuffle again
df = df.sample(frac=1).reset_index(drop=True)

# -------------------------------------------------------
# Balance Dataset (Optional)
# -------------------------------------------------------

print("\nEmotion Distribution\n")

print(df["primary_emotion"].value_counts())

print("\nMixed Emotion Distribution\n")

print(df["secondary_emotion"].value_counts())

# -------------------------------------------------------
# Save Dataset
# -------------------------------------------------------

OUTPUT_FILE = "learning_emotions_5000.csv"

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

print("\nDataset saved successfully!")

print(f"Total Samples : {len(df)}")

print(f"Saved As      : {OUTPUT_FILE}")

rows = []

for emotion, temp_list in templates.items():
    for _ in range(400):   # 200 × 5 = 1000 rows
        sentence = random.choice(temp_list).format(random.choice(subjects))
        rows.append([sentence, emotion])

random.shuffle(rows)

df = pd.DataFrame(rows, columns=["text", "emotion"])
df.to_csv("learning_emotions_part1.csv", index=False)

print("Generated", len(df), "rows.")