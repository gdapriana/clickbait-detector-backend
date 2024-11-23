import json
from flask import jsonify
import pandas as pd

def get_dataset(num_row=5, dataset=None):
  dataset_title = "Clickbait Dataset"
  dataset_subtitle = "Dataset of news articles for classification into clickbait and non-clickbait"
  dataset_link = "https://www.kaggle.com/datasets/amananandrai/clickbait-dataset"
  df = pd.concat([dataset[dataset['clickbait'] == 1].sample(frac=0.5, random_state=42), dataset[dataset['clickbait'] == 0].sample(frac=0.5, random_state=42)]).sample(frac=1, random_state=42)
  df = df.head(num_row)
  df = df.to_json(orient="records")
  df = json.loads(df)
  return df, dataset_title, dataset_subtitle, dataset_link