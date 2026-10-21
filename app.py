import pickle
import streamlit as st

# Load the saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Fake News Classifier", page_icon="📰", layout="centered"
)

st.title("📰 Fake News Article Classification")
st.write(
    "Enter a news article text below to check whether it is predicted to be **Real** or **Fake**."
)

# Text area for user input
news_text = st.text_area(
    "Paste News Article Here:", height=200, placeholder="Type or paste text..."
)

if st.button("Predict"):
  if news_text.strip() == "":
    st.warning("Please enter some text before clicking predict.")
  else:
    # Vectorize the input text
    transform_text = vectorizer.transform([news_text])

    # Make prediction
    prediction = model.predict(transform_text)[0]
    probability = model.predict_proba(transform_text)

    # Display results
    st.subheader("Prediction Result:")
    if prediction == 1:
      st.success(
          f"✅ This article is predicted to be **Real News** (Confidence:"
          f" {probability[0][1]*100:.2f}%)"
      )
    else:
      st.error(
          f"🚨 This article is predicted to be **Fake News** (Confidence:"
          f" {probability[0][0]*100:.2f}%)"
      )