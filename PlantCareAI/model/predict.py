import tensorflow as tf
import numpy as np
import cv2
import os

# Load trained model
model = tf.keras.models.load_model("../outputs/model.h5")

# IMPORTANT: same class order as training
dataset_path = "../dataset/PlantVillage"
class_names = sorted(os.listdir(dataset_path))

# Input image path
img_path = input("Enter image path: ")

# Read image
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Preprocess image
img = cv2.resize(img, (224, 224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# Predict
prediction = model.predict(img)
class_index = np.argmax(prediction)

print("\n✅ Prediction:", class_names[class_index])