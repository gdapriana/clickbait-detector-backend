from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from resources.dataset import get_dataset
from resources.model import get_model
from resources.preprocessing import preprocessing_input
import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

dataset = []

@app.route('/')
@cross_origin()
def hello_world():
  return jsonify({"message": "news classification"})

@app.route('/dataset')
@cross_origin()
def end_dataset():
  df, dataset_title, dataset_subtitle, dataset_link = get_dataset(num_row=10, dataset=dataset)
  return jsonify({"dataset": df,
                  dataset_title: dataset_title,
                  dataset_subtitle: dataset_subtitle,
                  dataset_link: dataset_link
                  })

@app.route('/predict', methods=['POST'])
@cross_origin()
def end_predict():
  data = request.get_json()
  new_text = data['text']
  processed_text = preprocessing_input(new_text, df=dataset)
  model = get_model()
  prediction = model.predict(processed_text)[0][0]
  return jsonify({"prediction": prediction})

if __name__ == '__main__':
  dataset = pd.read_csv("resources/dataset.csv", index_col=False)
  app.run()