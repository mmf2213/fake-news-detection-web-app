from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model(df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['clean_text'])
    y = df['label']

    model = LogisticRegression()
    model.fit(X, y)

    return model, vectorizer

def predict(model, vectorizer, df):
    X = vectorizer.transform(df['clean_text'])
    df['prediction'] = model.predict(X)
    return df