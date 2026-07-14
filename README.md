# 📰 Fake News Detection using NLP and Machine Learning

## 📌 Project Overview

Fake news spreads rapidly across digital platforms, making it difficult to distinguish genuine information from misinformation.

This project builds an end-to-end **Natural Language Processing (NLP)** pipeline that classifies a news article as **Fake** or **Real** using classical NLP techniques and Machine Learning.

The application is deployed as a REST API using **FastAPI** and containerized with **Docker**.

---

# 🚀 Features

- End-to-End NLP Pipeline
- Text Cleaning & Preprocessing
- Tokenization
- Stop Word Removal
- Lemmatization
- Bag of Words (BoW)
- TF-IDF Vectorization
- Multiple Machine Learning Models
- Model Comparison
- FastAPI REST API
- Docker Support
- GitHub Actions CI

---

# 📂 Dataset

Dataset: ISOT Fake News Dataset

Contents:

- Fake.csv
- True.csv

Total Records:

| Dataset | Records |
|----------|---------|
| Fake News | 23,481 |
| Real News | 21,417 |
| Total | 44,898 |

Columns:

- title
- text
- subject
- date

---

# 🛠 Technologies Used

## Programming Language

- Python 3.10

## NLP

- NLTK

## Machine Learning

- Scikit-Learn

## API

- FastAPI

## Deployment

- Docker
- Docker Compose

## Model Serialization

- Joblib

---

# 📁 Project Structure

```text
Fake-News-Detection/
│
├── app/
│   └── main.py
│
├── data/
│   ├── Fake.csv
│   └── True.csv
│
├── models/
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── preprocess.py
│   └── predict.py
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 NLP Pipeline

```
Raw News
      │
      ▼
Text Cleaning
      │
      ▼
Lowercase Conversion
      │
      ▼
URL Removal
      │
      ▼
HTML Removal
      │
      ▼
Punctuation Removal
      │
      ▼
Number Removal
      │
      ▼
Tokenization
      │
      ▼
Stop Word Removal
      │
      ▼
Lemmatization
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Linear SVM
      │
      ▼
Prediction
```

---

# 🤖 Machine Learning Models

The following models were trained and compared.

| Model | Feature Extraction | Accuracy |
|--------|--------------------|----------|
| Multinomial Naive Bayes | Bag of Words | **95.59%** |
| Multinomial Naive Bayes | TF-IDF | **94.04%** |
| Logistic Regression | TF-IDF | **98.72%** |
| **Linear SVM** | **TF-IDF** | **99.55%** ✅ |

Best Model:

- Linear Support Vector Machine
- TF-IDF Vectorizer

---

# 📊 Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 🌐 REST API

## Home

```
GET /
```

Response

```json
{
    "message": "Fake News Detection API is running!"
}
```

---

## Prediction

```
POST /predict
```

Request

```json
{
    "news": "The government announced a new education policy today."
}
```

Response

```json
{
    "prediction": "Fake News"
}
```

---

# ▶️ Run Locally

## Clone Repository

```bash
git clone <repository-url>
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker compose up --build
```

Swagger

```
http://localhost:8000/docs
```

---

# 📈 Future Improvements

- Word2Vec
- GloVe Embeddings
- FastText
- BERT
- RoBERTa
- Transformer Models
- Explainable AI (LIME/SHAP)
- CI/CD Deployment to Azure

---

# 💡 Key NLP Concepts Demonstrated

- Text Preprocessing
- Tokenization
- Stop Words
- Lemmatization
- Bag of Words
- TF-IDF
- Feature Engineering
- Text Classification

---

# 📚 Interview Highlights

This project demonstrates:

- End-to-End NLP Pipeline
- Classical NLP Techniques
- Feature Engineering
- Model Comparison
- Machine Learning Model Selection
- REST API Development
- Docker Containerization
- GitHub CI/CD
- Production-ready Project Structure

---

# 👨‍💻 Author

**Sumanth Ashwath**

Senior Infrastructure Engineer | AI & ML Enthusiast

GitHub:
https://github.com/Sumanth181991