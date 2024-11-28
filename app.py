from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from resources.dataset import get_dataset
from resources.preprocessing import preprocessing_input
from resources.member import member
from resources.evaluate import evaluate
from resources.model import model_info
import joblib
import json

from resources.tech import get_tech

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
  return jsonify({"message": "news classification"})

@app.route('/dataset')
@cross_origin()
def end_dataset():
  row = request.args.get('row')

  try:
    if row is None:
      row = 10
    row = int(row)
  except ValueError:
    return jsonify({"message": "wrong input"})

  (df,
   dataset_title,
   dataset_subtitle,
   dataset_link,
   total_dataset_count,
   taken_dataset_count,
   true_label,
   false_label) = get_dataset(num_row=row)
  return jsonify({"dataset": df,
                  "dataset_title": dataset_title,
                  "dataset_subtitle": dataset_subtitle,
                  "dataset_link": dataset_link,
                  "total_dataset": total_dataset_count,
                  "taken_dataset": taken_dataset_count,
                  "true_label": true_label,
                  "false_label": false_label
                  })

@app.route('/model')
@cross_origin()
def end_model():
  model_config, model_compile_config = model_info()
  con_matrix, accuracy, precision, recall = evaluate()
  lib_info = {
    "name": "tensorflow",
    "source": "https://www.tensorflow.org/",
    "description": "TensorFlow makes it easy to create ML models that can run in any environment. Learn how to use the intuitive APIs through interactive code samples",
    "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/google-tensorflow-icon.png"
  }
  return jsonify({ "model_config": model_config,
                   "model_compile": model_compile_config,
                   "evaluate": {
                     "con_matrix": con_matrix,
                     "accuracy": accuracy,
                     "precision": precision,
                     "recall": recall
                   },
                   "lib_info": lib_info
                   })


@app.route('/member')
@cross_origin()
def end_member():
  all_member = json.loads(json.dumps(member()))
  return jsonify({"all_member": all_member})

@app.route('/tech')
@cross_origin()
def end_tech():
  frontend, api, backend = get_tech()
  frontend = json.loads(json.dumps(frontend))
  api = json.loads(json.dumps(api))
  backend = json.loads(json.dumps(backend))
  return jsonify({"frontend": frontend, "api": api, "backend": backend})

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
