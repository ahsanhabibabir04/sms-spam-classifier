\# SMS Spam Classifier



A machine learning project that classifies SMS messages as \*\*Spam\*\* or \*\*Ham (Not Spam)\*\* using TF-IDF text features and a Multinomial Naive Bayes classifier.



\## Features



\- SMS spam classification using NLP techniques

\- TF-IDF feature extraction

\- Training and testing split with stratification

\- Evaluation using accuracy, precision, recall, F1-score, and confusion matrix

\- Interactive Streamlit web application

\- Automated unit tests



\## Tech Stack



\- Python 3.11

\- Pandas

\- Scikit-learn

\- Streamlit

\- Matplotlib

\- Joblib



\## Dataset



This project uses the UCI SMS Spam Collection dataset.



Source: https://archive.ics.uci.edu/dataset/228/sms+spam+collection



\## Installation



Clone this repository, then create and activate a virtual environment.



```bash

py -3.11 -m venv .venv

```



Install the dependencies:



```bash

.venv\\Scripts\\python.exe -m pip install pandas scikit-learn streamlit matplotlib joblib

```



\## Train and Evaluate the Model



```bash

.venv\\Scripts\\python.exe main.py

```



The trained model is saved to `models/sms\_spam\_model.joblib`.



\## Run the Web App



```bash

.venv\\Scripts\\python.exe -m streamlit run app.py

```



Open the local URL shown in the terminal.



\## Run Tests



```bash

.venv\\Scripts\\python.exe -m unittest -v test\_main.py

```



\## Evaluation Results



On the current 20% held-out test split:



\- Accuracy: 95.06%

\- Spam precision: 100% (rounded)

\- Spam recall: 60.16% (rounded)



The model missed 51 of 128 spam messages in this test split. Accuracy alone does not fully describe performance, and the model should not be considered production-ready.



\## Project Structure



```text

SMS-Spam-Classifier/

├── data/

│   └── SMSSpamCollection

├── models/

│   └── sms\_spam\_model.joblib

├── main.py

├── app.py

├── test\_main.py

├── .gitignore

└── README.md

```



\## Limitations



This is an educational project. Predictions may be incorrect, particularly for spam messages that differ from the training examples.



\## Author



M.A. Ahsan Habib Abir

