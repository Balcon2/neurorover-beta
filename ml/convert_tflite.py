"""
Convert Keras model to TensorFlow Lite.
Run: python ml/convert_tflite.py
"""
from pathlib import Path
import tensorflow as tf

MODEL_DIR = Path("models")
model = tf.keras.models.load_model(MODEL_DIR / "neurorover_model.keras")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()
(MODEL_DIR / "neurorover_model.tflite").write_bytes(tflite_model)
print("saved models/neurorover_model.tflite")
