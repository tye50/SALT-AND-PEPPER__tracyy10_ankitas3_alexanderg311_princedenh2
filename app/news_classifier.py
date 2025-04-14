import numpy as np 
import pandas as pd 
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.naive_bayes import GaussianNB
tfidf_vectorizer = TfidfVectorizer()
def get_model():
    fake = pd.read_csv(os.path.abspath('data/Fake (1).csv'))
    real = pd.read_csv(os.path.abspath('data/True (1).csv'))

    fake['true'] = 0
    real['true'] = 1
    news = pd.concat([fake, real], ignore_index = True)
    news.drop(['subject', 'date'], axis=1, inplace=True)

    print(news.head(10))
    print(news.columns)
    x = news[['title', 'text']]
    y = news['true']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    X_train_tfidf = tfidf_vectorizer.fit_transform(X_train["title"] + " " + X_train["text"])
    print(X_train_tfidf)
    X_test_tfidf = tfidf_vectorizer.transform(X_test["title"] + " " + X_test["text"])


    print(x)
    print(y)




    model = MultinomialNB()

    model.fit(X_train_tfidf, y_train)
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model.__class__.__name__}: {accuracy*100:.2f}")
    return model
def get_probability(model, text):
    text = str(text)
    prediction = model.predict_proba(tfidf_vectorizer.transform([text]))
    return prediction[0];
classifier = get_model()
n = get_probability(classifier, """trump""")
print(n)

