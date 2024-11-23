import tensorflow as tf
def get_model():
  model = tf.keras.models.load_model("resources/model.h5")
  return model
