
import unittest
from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "sms_spam_model.joblib"


class TestSMSSpamClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Trained model not found. Run main.py first."
            )
        cls.model = joblib.load(MODEL_PATH)

    def test_model_has_expected_pipeline_steps(self):
        self.assertEqual(
            list(self.model.named_steps.keys()),
            ["tfidf", "classifier"],
        )

    def test_prediction_labels_are_valid(self):
        messages = [
            "Congratulations! You have won a free prize. Claim it now!",
            "Hey, are we still meeting for lunch today?",
        ]
        predictions = self.model.predict(messages)

        self.assertEqual(len(predictions), 2)
        self.assertTrue(set(predictions).issubset({"ham", "spam"}))

    def test_obvious_spam_example(self):
        message = "Congratulations! You have won a free prize. Claim it now!"
        self.assertEqual(self.model.predict([message])[0], "spam")

    def test_normal_conversation_example(self):
        message = "Hey, are we still meeting for lunch today?"
        self.assertEqual(self.model.predict([message])[0], "ham")

    def test_empty_message_does_not_crash(self):
        # An empty string is not a valid real SMS, but the pipeline
        # should still return a valid class rather than raising an error.
        prediction = self.model.predict([""])
        self.assertIn(prediction[0], {"ham", "spam"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
