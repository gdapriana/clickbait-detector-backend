from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from resources.dataset import get_dataset
from resources.preprocessing import preprocessing_input, preprocessing_dataset
import pandas as pd
from sklearn.neural_network import MLPClassifier


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

dataset = []
model = MLPClassifier(
  hidden_layer_sizes=(64, 32),  # Two hidden layers with 64 and 32 neurons
  activation='relu',            # ReLU activation function
  solver='adam',                # Optimizer
  max_iter=10,                 # Maximum number of epochs (iterations)
  random_state=42               # Set a random state for reproducibility
)

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
  predicted = model.predict_proba(processed_text)
  return jsonify({"prediction": predicted[0][1]})

if __name__ == '__main__':
  dataset = pd.read_csv("dataset.csv", index_col=False)
  X_train, X_test, y_train, y_test = preprocessing_dataset(dataset)
  model.fit(X_train, y_train)
  app.run()