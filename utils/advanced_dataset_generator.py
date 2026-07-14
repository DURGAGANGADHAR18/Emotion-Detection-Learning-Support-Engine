import random
import pandas as pd
EMOTIONS = [
    "Confused",
    "Frustrated",
    "Curious",
    "Confident",
    "Bored"
]
SUBJECTS = [

"Python",
"Java",
"C",
"C++",
"JavaScript",
"HTML",
"CSS",
"React",
"Node.js",
"SQL",
"MySQL",
"MongoDB",
"DBMS",
"Operating Systems",
"Computer Networks",
"Data Structures",
"Algorithms",
"Machine Learning",
"Deep Learning",
"Artificial Intelligence",
"Data Science",
"Statistics",
"Mathematics",
"Calculus",
"Linear Algebra",
"Physics",
"Chemistry",
"Biology",
"Cloud Computing",
"AWS",
"Azure",
"Cyber Security",
"Ethical Hacking",
"Linux",
"Git",
"GitHub",
"Docker",
"Kubernetes",
"Android Development",
"Flutter",
"Software Engineering",
"Compiler Design",
"Computer Architecture",
"Discrete Mathematics",
"Digital Electronics",
"IoT",
"Blockchain",
"NLP",
"Computer Vision",
"Streamlit"

]
SITUATIONS = [

"while solving assignments",

"before exams",

"during lab sessions",

"while writing code",

"while debugging",

"during online classes",

"while preparing for interviews",

"while building projects",

"while practicing coding",

"while studying late at night",

"while attending lectures",

"while solving previous papers",

"while completing homework",

"while preparing notes",

"while reading textbooks"

]
# ---------------------------------------------------------
# ADVANCED SENTENCE TEMPLATES
# ---------------------------------------------------------

TEMPLATES = {

"Confused":[

"I don't understand {} {}.",
"I am confused about {} {}.",
"I keep forgetting the concepts of {} {}.",
"I cannot understand the logic behind {} {}.",
"I don't know how to solve {} {}.",
"I am unable to understand {} {}.",
"I don't know where I am making mistakes in {} {}.",
"I feel completely lost while studying {} {}.",
"I cannot differentiate the concepts in {} {}.",
"I keep getting confused whenever I study {} {}.",
"I don't know how to start learning {} {}.",
"I find {} extremely difficult {}.",
"I read the topic many times but still don't understand {} {}.",
"I cannot understand the examples of {} {}.",
"I always get confused between similar topics in {} {}.",
"I don't understand why my solution is wrong in {} {}.",
"I don't know which approach to use in {} {}.",
"I keep asking questions because {} confuses me {}.",
"I don't understand the syntax of {} {}.",
"I get confused every time I practice {} {}."

],

"Frustrated":[

"I am frustrated with {} {}.",
"I keep getting errors while learning {} {}.",
"I spent hours studying {} but still failed {}.",
"I feel like giving up on {} {}.",
"I am tired of debugging {} {}.",
"I keep making the same mistakes in {} {}.",
"I cannot complete my {} assignment {}.",
"I worked very hard but still don't understand {} {}.",
"I am stressed because of {} {}.",
"I don't know why {} is so difficult {}.",
"I feel overwhelmed while studying {} {}.",
"I cannot solve even simple problems in {} {}.",
"I hate working on {} {}.",
"I feel disappointed with my performance in {} {}.",
"I always fail in {} {}.",
"I am exhausted after practicing {} {}.",
"I feel mentally tired because of {} {}.",
"I cannot finish my project using {} {}.",
"I lose confidence every time I study {} {}.",
"I keep failing while practicing {} {}."

],

"Curious":[

"I want to know more about {} {}.",
"I enjoy learning {} {}.",
"I want to build projects using {} {}.",
"I am interested in advanced {} concepts {}.",
"I enjoy exploring new ideas in {} {}.",
"I want to become an expert in {} {}.",
"I love reading about {} {}.",
"I want to understand every concept of {} {}.",
"I want to learn real-world applications of {} {}.",
"I enjoy experimenting with {} {}.",
"I am excited to study {} {}.",
"I like discovering new topics in {} {}.",
"I want to explore research in {} {}.",
"I enjoy solving difficult problems in {} {}.",
"I want to learn beyond my syllabus in {} {}.",
"I want to participate in competitions related to {} {}.",
"I want to improve my knowledge in {} {}.",
"I enjoy asking questions about {} {}.",
"I want to build innovative solutions using {} {}.",
"I want to master {} {}."

],

"Confident":[

"I understand {} very well {}.",
"I solved all the problems in {} {}.",
"I completed my {} assignment successfully {}.",
"I am confident in {} {}.",
"I can teach {} to my friends {}.",
"I scored excellent marks in {} {}.",
"I can solve difficult {} questions {}.",
"I enjoy helping others understand {} {}.",
"I completed my project using {} successfully {}.",
"I can answer any question related to {} {}.",
"I practice {} every day {}.",
"I am improving continuously in {} {}.",
"I feel prepared for my {} exam {}.",
"I enjoy solving advanced {} problems {}.",
"I built a complete application using {} {}.",
"I can debug {} programs easily {}.",
"I feel comfortable learning {} {}.",
"I can complete {} tasks without help {}.",
"I solved all coding challenges in {} {}.",
"I believe I have mastered {} {}."

],

"Bored":[

"I feel bored while studying {} {}.",
"I lose interest in {} {}.",
"I cannot stay focused during {} {}.",
"I find {} repetitive {}.",
"I don't enjoy learning {} anymore {}.",
"I feel sleepy while studying {} {}.",
"I keep getting distracted during {} {}.",
"I don't feel motivated to study {} {}.",
"I am not interested in {} anymore {}.",
"I cannot concentrate while learning {} {}.",
"I feel exhausted attending {} lectures {}.",
"I get bored reading {} books {}.",
"I don't like solving {} problems anymore {}.",
"I lose my attention quickly in {} {}.",
"I don't feel excited about {} {}.",
"I wish {} was more interesting {}.",
"I don't enjoy practicing {} {}.",
"I cannot stay engaged while learning {} {}.",
"I feel lazy whenever I open {} {}.",
"I postpone studying {} because it feels boring {}."

]

}
# ---------------------------------------------------------
# MIXED EMOTION COMBINATIONS
# ---------------------------------------------------------

MIXED_EMOTIONS = [

("Confused","Frustrated"),

("Confused","Curious"),

("Curious","Confident"),

("Frustrated","Confident"),

("Bored","Frustrated"),

("Bored","Confused"),

("Curious","Bored"),

("Confident","Curious"),

("Confident","Frustrated"),

("Curious","Confused")

]

# ---------------------------------------------------------
# MIXED SENTENCE CONNECTORS
# ---------------------------------------------------------

CONNECTORS = [

"because",

"and",

"but",

"although",

"even though",

"while",

"yet",

"however",

"at the same time"

]

# ---------------------------------------------------------
# CREATE SINGLE EMOTION SENTENCE
# ---------------------------------------------------------

def generate_single():

    emotion = random.choice(list(TEMPLATES.keys()))

    template = random.choice(TEMPLATES[emotion])

    subject = random.choice(SUBJECTS)

    situation = random.choice(SITUATIONS)

    sentence = template.format(subject, situation)

    return {
        "text": sentence,
        "primary_emotion": emotion,
        "secondary_emotion": ""
    }


# ---------------------------------------------------------
# CREATE MIXED EMOTION SENTENCE
# ---------------------------------------------------------

def generate_mixed():

    primary, secondary = random.choice(MIXED_EMOTIONS)

    first = random.choice(TEMPLATES[primary])

    second = random.choice(TEMPLATES[secondary])

    subject = random.choice(SUBJECTS)

    situation = random.choice(SITUATIONS)

    connector = random.choice(CONNECTORS)

    part1 = first.format(subject, situation).rstrip(".")

    part2 = second.format(subject, situation).lower()

    sentence = f"{part1} {connector} {part2}"

    return {
        "text": sentence,
        "primary_emotion": primary,
        "secondary_emotion": secondary
    }
    # ---------------------------------------------------------
# GENERATE DATASET
# ---------------------------------------------------------

dataset = []

TOTAL_SAMPLES = 10000

# 70% Single Emotion
single_samples = int(TOTAL_SAMPLES * 0.70)

# 30% Mixed Emotion
mixed_samples = TOTAL_SAMPLES - single_samples

print("Generating single emotion samples...")

for _ in range(single_samples):
    dataset.append(generate_single())

print("Generating mixed emotion samples...")

for _ in range(mixed_samples):
    dataset.append(generate_mixed())

# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(dataset)

# Remove duplicate sentences
df.drop_duplicates(subset=["text"], inplace=True)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# ---------------------------------------------------------
# SAVE DATASET
# ---------------------------------------------------------

OUTPUT_FILE = "datasets/emotions_advanced.csv"

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

# ---------------------------------------------------------
# DISPLAY STATISTICS
# ---------------------------------------------------------

print("\n===================================")
print("Dataset Generated Successfully!")
print("===================================\n")

print(f"Total Samples : {len(df)}")

print("\nPrimary Emotion Distribution:\n")
print(df["primary_emotion"].value_counts())

print("\nSecondary Emotion Distribution:\n")
print(df["secondary_emotion"].value_counts())

print(f"\nDataset saved to: {OUTPUT_FILE}")