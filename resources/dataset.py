import json

import pandas as pd


def get_dataset(num_row=5):
    dataset_title = "Clickbait Dataset"
    dataset_subtitle = (
        "Dataset of news articles for classification into clickbait and non-clickbait"
    )
    dataset_link = "https://www.kaggle.com/datasets/amananandrai/clickbait-dataset"
    dataset = pd.read_csv("resources/dataset.csv", index_col=False)
    balanced_df = pd.concat(
        [
            dataset[dataset["clickbait"] == 1].sample(frac=0.5, random_state=42),
            dataset[dataset["clickbait"] == 0].sample(frac=0.5, random_state=42),
        ]
    ).sample(frac=1, random_state=42)

    total_dataset_count = len(dataset)
    taken_dataset_coung = len(balanced_df)
    true_label = len(dataset[dataset["clickbait"] == 1])
    false_label = len(dataset[dataset["clickbait"] == 0])

    balanced_df = balanced_df.head(num_row)
    json_records = balanced_df.to_json(orient="records")
    df = json.loads(json_records)
    return (
        df,
        dataset_title,
        dataset_subtitle,
        dataset_link,
        total_dataset_count,
        taken_dataset_coung,
        true_label,
        false_label,
    )

