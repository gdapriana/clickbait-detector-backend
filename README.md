# Kelayakan Pinjaman
Menggunakan metode fuzzy tsukamoto.

| API | https://clickbait-detector-7e44ec055fea.herokuapp.com/                                                                                                                 |
|-----|------------------------------------------------------------------------------------------------------------------|
|Colab| <a href="https://colab.research.google.com/drive/1X-aTqftdPzJnKl499c5LlvG6U_C_M6vZ?usp=sharing">Google Colab</a> |

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
