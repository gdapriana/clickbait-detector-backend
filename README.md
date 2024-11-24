# Clickbait Detector using ANN

| API | https://clickbait-detector-7e44ec055fea.herokuapp.com/                                                                                                                 |
|-----|------------------------------------------------------------------------------------------------------------------|
|Colab| |


## API Documentations
| <b>endpoint</b> | `API/predict`               |
|-----------------|-----------------------------|
| method          | `POST`                      |
| req body        | ```{"text": string}```      |
| res body        | ```{"prediction": float}``` |

| <b>endpoint</b> | `API/dataset`                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------|
| method          | `GET`                                                                                              |
| res body        | ```{"dataset": [], "dataset_title": string, "dataset_subtitle": string, "dataset_link": string}``` |
