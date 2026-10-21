
from pathlib import Path

import joblib
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "sms_spam_model.joblib"


st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="📩",
    layout="centered",
)

st.title("📩 SMS Spam Classifier")
st.write(
    "Enter an SMS message below to check whether the model "
    "classifies it as spam or not spam."
)

st.caption("Machine learning demo • TF-IDF + Multinomial Naive Bayes")

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Trained model not found. Run main.py before starting the app."
        )
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except (FileNotFoundError, OSError) as error:
    st.error(str(error))
    st.stop()


message = st.text_area(
    "SMS message",
    placeholder="Example: Congratulations! You have won a free prize!",
    height=150,
    max_chars=5000,
)

if st.button("Check Message", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        prediction = model.predict([message])[0]
        probabilities = model.predict_proba([message])[0]
        classes = model.named_steps["classifier"].classes_
        scores = dict(zip(classes, probabilities))

        st.subheader("Prediction")

        if prediction == "spam":
            st.error("🚨 SPAM")
        else:
            st.success("✅ NOT SPAM (HAM)")

        st.write("Model probability estimates:")
        st.write(f"Spam: {scores.get('spam', 0.0):.1%}")
        st.progress(float(scores.get("spam", 0.0)))

        st.write(f"Not spam: {scores.get('ham', 0.0):.1%}")

        st.caption(
            "These are model probability estimates, not guarantees. "
            "A message may still be misclassified."
        )

st.divider()
st.caption(
    "Educational project using the UCI SMS Spam Collection dataset. "
    "Do not rely on this demo as your only spam protection."
)
