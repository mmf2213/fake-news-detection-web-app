from flask import Flask, render_template, request
from src.preprocessing import clean_text, load_data, preprocess
from src.model import train_model
import pandas as pd

app = Flask(__name__)

df = load_data("data/news.csv")
df = preprocess(df)
model, vectorizer = train_model(df)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""

    if request.method == 'POST':
        news = request.form['news']
        clean = clean_text(news)

        X = vectorizer.transform([clean])
        result = model.predict(X)[0]

        prediction = result

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)