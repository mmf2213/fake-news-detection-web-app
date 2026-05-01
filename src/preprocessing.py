import pandas as pd
import re

def load_data(path):
    return pd.read_csv(path)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

def preprocess(df):
    df['clean_text'] = df['text'].apply(clean_text)
    return df