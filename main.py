
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


# 1. Load the SMS dataset
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "SMSSpamCollection"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "sms_spam_model.joblib"

df = pd.read_csv(
    DATA_PATH,
    sep="\t",
    header=None,
    names=["label", "message"],
    encoding="utf-8",
)

# 2. Validate and clean the data
df = df.dropna(subset=["label", "message"])
df["label"] = df["label"].str.strip().str.lower()
df["message"] = df["message"].astype(str).str.strip()

df = df[
    df["label"].isin(["ham", "spam"]) & df["message"].ne("")
].drop_duplicates()

if df["label"].nunique() != 2:
    raise ValueError("Dataset must contain both ham and spam labels.")

X = df["message"]
y = df["label"]

# 3. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

# 4. Build the machine-learning pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB()),
])

# 5. Train the model
model.fit(X_train, y_train)

# 6. Evaluate on unseen test messages
y_pred = model.predict(X_test)

print("=" * 55)
print("SMS SPAM CLASSIFIER - MODEL EVALUATION")
print("=" * 55)
print(f"Total messages: {len(df)}")
print(f"Training messages: {len(X_train)}")
print(f"Testing messages: {len(X_test)}")
print(f"Spam messages: {(y == 'spam').sum()}")
print(f"Ham messages: {(y == 'ham').sum()}")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

print("\nClassification report:")
print(classification_report(
    y_test,
    y_pred,
    labels=["ham", "spam"],
    target_names=["Ham (Not Spam)", "Spam"],
    zero_division=0,
))

print("Confusion matrix (rows=true, columns=predicted):")
print(confusion_matrix(y_test, y_pred, labels=["ham", "spam"]))

# 7. Save the trained model
MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"\nSaved model to: {MODEL_PATH}")

# 8. Try example messages
examples = [
    "Congratulations! You have won a free prize. Claim it now!",
    "Hey, are we still meeting for lunch today?",
]

print("\nExample predictions:")
for message in examples:
    prediction = model.predict([message])[0]
    print(f"Prediction: {prediction.upper()} | Message: {message}")
