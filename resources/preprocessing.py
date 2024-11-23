import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import joblib
import re

stemmer = PorterStemmer()

def stem_headline(headline):
  tokens = word_tokenize(headline)
  stemmed_tokens = [stemmer.stem(token) for token in tokens]
  return ' '.join(stemmed_tokens)

def preprocessing_dataset():
  df = pd.read_csv("resources/dataset.csv", index_col=False)
  df = pd.concat([df[df['clickbait'] == 1].sample(frac=0.5, random_state=42), df[df['clickbait'] == 0].sample(frac=0.5, random_state=42)]).sample(frac=1, random_state=42)
  if df.isnull().any().any():
    df = df.dropna()
  if df.duplicated().sum() > 0:
    df = df.drop_duplicates()
  df['headline'] = df['headline'].str.lower()
  df['headline'] = df['headline'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
  df['headline'] = df['headline'].str.replace(r'\d+', '', regex=True)
  df['headline'] = df['headline'].str.strip()
  df['headline'] = df['headline'].apply(stem_headline)
  vectorizer = TfidfVectorizer(stop_words='english')
  response = vectorizer.fit_transform(df['headline'])
  X = response.toarray()
  y = df['clickbait'].to_numpy()
  scaler = MinMaxScaler(feature_range=(0, 1))
  X = scaler.fit_transform(X)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  return X_train, X_test, y_train, y_test

def preprocessing_input(new_text):
  df = pd.read_csv("resources/dataset.csv", index_col=False)
  df = pd.concat([df[df['clickbait'] == 1].sample(frac=0.5, random_state=42), df[df['clickbait'] == 0].sample(frac=0.5, random_state=42)]).sample(frac=1, random_state=42)
  if df.isnull().any().any():
    df = df.dropna()
  if df.duplicated().sum() > 0:
    df = df.drop_duplicates()
  df['headline'] = df['headline'].str.lower()
  df['headline'] = df['headline'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
  df['headline'] = df['headline'].str.replace(r'\d+', '', regex=True)
  df['headline'] = df['headline'].str.strip()
  df['headline'] = df['headline'].apply(stem_headline)
  vectorizer = TfidfVectorizer(stop_words='english')
  response = vectorizer.fit_transform(df['headline'])
  text = new_text.lower()
  text = re.sub(r'[^\w\s]', '', text)
  text = re.sub(r'\d+', '', text)
  text = ' '.join(text.split())
  ps = PorterStemmer()
  words = word_tokenize(text)
  stemmed_words = [ps.stem(word) for word in words]
  text = " ".join(stemmed_words)
  text = vectorizer.transform([text])
  text = text.toarray()
  scaler = joblib.load("resources/minmax_scaler.save")
  text = scaler.transform(text)
  return text.reshape(1, -1)
