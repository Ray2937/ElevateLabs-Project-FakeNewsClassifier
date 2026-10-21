# 📰 News Article Classification (Fake/Real)

An Machine Learning web application that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) and Logistic Regression.

## 📌 Features
- **Dataset:** ~45,000 labeled articles (Kaggle Fake/Real news dataset)
- **Preprocessing:** Lowercasing, punctuation removal, stop-word filtering, and Lemmatization via NLTK
- **Feature Extraction:** TF-IDF Vectorization (5,000 max features)
- **Model:** Logistic Regression achieving **~98.7% Accuracy**
- **User Interface:** Interactive Streamlit Web App

## 📁 Repository Structure
ElevateLabs-Project-FakeNewsClassifier/
├── data/
│   ├── True.csv
│   └── Fake.csv
├── notebooks/
│   └── news_classification.ipynb
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/ElevateLabs-Project-FakeNewsClassifier.git
   cd ElevateLabs-Project-FakeNewsClassifier
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit app:**
   ```bash
   python -m streamlit run app.py
   ```