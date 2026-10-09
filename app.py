import streamlit as st
import pickle
import nltk
from text_cleaner import clean_messages

@st.cache_resource
def ensure_nltk_data():
    for resource in ("corpora/stopwords", "corpora/wordnet"):
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(resource.split("/")[-1], quiet=True)

ensure_nltk_data()

with open('sms_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

st.title("📩 SMS Spam Classifier") 
st.write("This is a simple SMS Spam Classifier app. Enter a message below and click 'Classify' to see if it's spam or not.")
message = st.text_input("Enter an SMS message:")
if st.button("Classify"):
    prediction = pipeline.predict([message])
    if prediction[0] == 1:
        st.error("🚨 This message is classified as spam.")
    else:
        st.success("✅ This message is not classified as spam.")