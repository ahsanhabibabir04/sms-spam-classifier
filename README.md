# SMS Spam Classifier

A machine learning application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP), TF-IDF feature extraction, and a Multinomial Naive Bayes classifier.

## Project Overview

SMS Spam Classifier is a machine learning project designed to identify unwanted text messages. It processes SMS text, converts messages into numerical features using TF-IDF, and uses a trained Multinomial Naive Bayes model to predict whether a message is spam or legitimate.

The project includes a model training pipeline, performance evaluation, an interactive Streamlit web application, and automated unit tests.

## Features

- Classifies SMS messages as Spam or Ham
- Uses Natural Language Processing (NLP) techniques
- Extracts text features using TF-IDF
- Trains a Multinomial Naive Bayes classifier
- Splits data into training and testing sets using stratification
- Evaluates performance using accuracy, precision, recall, F1-score, and a confusion matrix
- Provides an interactive web interface built with Streamlit
- Saves the trained model using Joblib
- Includes automated unit tests
- Supports local execution on Windows

## Technologies Used

- **Python 3.11** — Programming language
- **Pandas** — Data loading and manipulation
- **Scikit-learn** — Feature extraction, model training, and evaluation
- **Streamlit** — Interactive web application
- **Matplotlib** — Data visualization
- **Joblib** — Model serialization
- **unittest** — Automated testing
- **Git and GitHub** — Version control and source code hosting

## Dataset

This project uses the **UCI SMS Spam Collection** dataset, which contains SMS messages labeled as spam or ham.

**Dataset Source:** [UCI Machine Learning Repository — SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

The dataset is used to train and evaluate the classification model.

## Requirements

- Python 3.11
- Git (optional, for cloning the repository)
- An internet connection for installing dependencies

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ahsanhabibabir04/sms-spam-classifier.git
```

### 2. Navigate to the Project Directory

```bash
cd sms-spam-classifier
```

### 3. Create a Virtual Environment

Make sure Python 3.11 is installed, then run:

```bash
py -3.11 -m venv .venv
```

### 4. Install Dependencies

On Windows, install the required packages using:

```bash
.venv\Scripts\python.exe -m pip install pandas scikit-learn streamlit matplotlib joblib
```

## Train and Evaluate the Model

Run the main Python script to train the classifier and evaluate its performance:

```bash
.venv\Scripts\python.exe main.py
```

The script trains the model, evaluates it on the held-out test dataset, and saves the trained model to:

```text
models/sms_spam_model.joblib
```

Make sure the required dataset is available in the `data/` directory.

## Run the Web Application

Start the Streamlit application with:

```bash
.venv\Scripts\python.exe -m streamlit run app.py
```

After the application starts, open the local URL displayed in the terminal.

Enter an SMS message into the interface to receive a spam or ham prediction.

## Run Automated Tests

Execute the unit tests using:

```bash
.venv\Scripts\python.exe -m unittest -v test_main.py
```

The tests help verify the behavior of the implemented functions and model pipeline.

## Model Evaluation

The model was evaluated on a held-out test set representing 20% of the dataset.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 95.06% |
| Spam Precision | 100% (rounded) |
| Spam Recall | 60.16% (rounded) |
| Spam Messages Missed | 51 out of 128 |

### Understanding the Results

- **Accuracy:** The model correctly classified approximately 95.06% of all messages in the test set.
- **Precision:** Spam precision rounded to 100% on this test split, indicating very few false-positive spam predictions.
- **Recall:** The model identified approximately 60.16% of the actual spam messages.
- **False Negatives:** The model failed to identify 51 spam messages in the test set, classifying them as non-spam.

Although the model achieved high overall accuracy and spam precision, its recall indicates that a substantial proportion of spam messages were missed.

These results demonstrate why accuracy alone is insufficient for evaluating a spam classification system.

**Note:** The reported metrics reflect the current test split and may vary if the dataset split, random seed, or model configuration changes. The model is intended for educational purposes and has not been established as production-ready.

## Project Structure

```text
sms-spam-classifier/
├── data/
│   └── SMSSpamCollection
├── models/
│   └── sms_spam_model.joblib
├── main.py
├── app.py
├── test_main.py
├── .gitignore
└── README.md
```

The trained model file is generated when the training script runs, so it may not exist in a fresh clone until the model has been trained.

## Limitations

- The model may incorrectly classify legitimate messages as spam or spam messages as legitimate.
- Spam recall is relatively low, meaning some spam messages may go undetected.
- Predictions depend on the quality and diversity of the training dataset.
- Unfamiliar wording, new spam patterns, and messages that differ from the training examples may reduce prediction reliability.
- The model has been evaluated on a held-out test split but has not been validated for production use.

## Future Improvements

Potential improvements include:

- Improving spam recall while maintaining acceptable precision
- Comparing Multinomial Naive Bayes with other classification algorithms
- Performing hyperparameter tuning and cross-validation
- Adding more diverse SMS examples to improve generalization
- Displaying prediction confidence or probability estimates
- Enhancing the Streamlit interface with additional evaluation visualizations
- Deploying the application to a public hosting platform

## Learning Outcomes

Through this project, I practiced:

- Applying NLP techniques to text classification
- Converting text into numerical features using TF-IDF
- Training a machine learning classifier with Scikit-learn
- Splitting datasets using stratified sampling
- Evaluating models using classification metrics
- Understanding precision, recall, and false negatives
- Saving and loading trained models with Joblib
- Building an interactive application with Streamlit
- Writing automated tests with Python's `unittest`
- Managing and documenting projects using Git and GitHub

## Author

**M.A. Ahsan Habib Abir**

Aspiring Computer Science and Artificial Intelligence student interested in machine learning, natural language processing, and software development.

## Repository

GitHub: [SMS Spam Classifier](https://github.com/ahsanhabibabir04/sms-spam-classifier)

---

If you find this project useful, consider giving the repository a star.
