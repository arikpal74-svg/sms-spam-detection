# SMS Spam Classifier

A machine learning app that classifies SMS messages as **spam** or **ham** (not spam). Enter a message in the app to see its prediction.

## How it works

The app cleans the message, converts its text into TF-IDF features, and passes those features to a trained machine learning model.

## Built with

- Python
- Scikit-learn
- NLTK
- Streamlit

## Try the app

**Live demo:** _Add your Streamlit app link here after deployment._

## Example

**Message:** “Congratulations! You have won a free prize. Click here to claim your reward.”

**Prediction:** Spam

## Project files

- `app.py` — interactive web app
- `text_cleaner.py` — text-cleaning functions
- `sms_pipeline.pkl` — trained classification pipeline
- `requirements.txt` — app dependencies

## Run locally

Install the dependencies and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## About

This project demonstrates an end-to-end text classification workflow, from cleaning SMS messages to serving model predictions in a web app.
