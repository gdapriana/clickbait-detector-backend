from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from resources.dataset import get_dataset
from resources.preprocessing import preprocessing_input, preprocessing_dataset
from sklearn.neural_network import MLPClassifier
import joblib


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# model = MLPClassifier(
#   hidden_layer_sizes=(64, 32),
#   activation='relu',
#   solver='adam',
#   max_iter=10,
#   random_state=42
# )

@app.route('/')
@cross_origin()
def hello_world():
  return jsonify({"message": "news classification"})

@app.route('/dataset')
@cross_origin()
def end_dataset():
  df, dataset_title, dataset_subtitle, dataset_link = get_dataset(num_row=10)
  return jsonify({"dataset": df,
                  "dataset_title": dataset_title,
                  "dataset_subtitle": dataset_subtitle,
                  "dataset_link": dataset_link
                  })

@app.route('/predict', methods=['POST'])
@cross_origin()
def end_predict():
  data = request.get_json()
  new_text = data['text']
  model = joblib.load(open("resources/model.sav", 'rb'))
  processed_text = preprocessing_input(new_text)
  predicted = model.predict_proba(processed_text)
  return jsonify({"prediction": predicted[0][1]})

if __name__ == '__main__':
  app.run()