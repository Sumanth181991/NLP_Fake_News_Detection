import joblib

from preprocess import preprocess_text

model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_news(news):

    news = preprocess_text(news)

    vector = vectorizer.transform([news])

    prediction = model.predict(vector)[0]

    if prediction == 0:
        return "Fake News"

    return "Real News"


if __name__ == "__main__":

    news = input("Enter News : ")

    print(predict_news(news))