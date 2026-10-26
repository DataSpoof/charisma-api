import tensorflow as tf
import joblib

# load model
model = tf.keras.models.load_model("model/model.h5")

# load scaler
scaler = joblib.load("model/scaler.pkl")