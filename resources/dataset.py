import json
import pandas as pd

def get_dataset(num_row=5, dataset=None):
  dataset_title = "Clickbait Dataset"
  dataset_subtitle = "Dataset of news articles for classification into clickbait and non-clickbait"
  dataset_link = "https://www.kaggle.com/datasets/amananandrai/clickbait-dataset"
  if dataset is None or not isinstance(dataset, pd.DataFrame):
    raise ValueError("Please provide a valid Pandas DataFrame as the dataset.")
  balanced_df = pd.concat([
    dataset[dataset['clickbait'] == 1].sample(frac=0.5, random_state=42),
    dataset[dataset['clickbait'] == 0].sample(frac=0.5, random_state=42)
  ]).sample(frac=1, random_state=42)
  balanced_df = balanced_df.head(num_row)
  json_records = balanced_df.to_json(orient="records")  # JSON string
  df = json.loads(json_records)  # Convert to list of dictionaries
  return df, dataset_title, dataset_subtitle, dataset_link