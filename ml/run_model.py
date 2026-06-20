"""
Run trained model with camera and print predictions.
Run: python ml/run_model.py
"""
from pathlib import Path
import cv2
import numpy as np
import tensorflow as tf

MODEL_DIR = Path("models")
IMG_SIZE = (96, 96)

model = tf.keras.models.load_model(MODEL_DIR / "neurorover_model.keras")
classes = (MODEL_DIR / "classes.txt").read_text(encoding="utf-8").splitlines()

camera = cv2.VideoCapture(0)

while True:
    ok, frame = camera.read()
    if not ok:
        break

    img = cv2.resize(frame, IMG_SIZE)
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)[0]
    index = int(np.argmax(pred))
    print(classes[index], float(pred[index]))

    cv2.imshow("AI Prediction", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
