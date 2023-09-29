from flask import Flask, render_template, request, jsonify
import os
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
tf.config.experimental.set_visible_devices([], 'GPU')

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

classnames = [
    'Tomato___Bacterial_spot', 'Tomato___Early_blight','Tomato___Late_blight', 
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]

# Create the "uploads" directory if it doesn't exist
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

def predict_image_class(image_path):
    model = load_model(os.path.join("artifacts","training", "model.h5"))
    img = load_and_preprocess_image(image_path)
    predictions = model.predict(img)
    predicted_class_index = np.argmax(predictions, axis=1)
    print(predicted_class_index)
    predicted_class = classnames[predicted_class_index[0]]
    return predicted_class

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return "No image file provided."

    image_file = request.files["image"]
    if image_file.filename == "":
        return "No selected image file."

    if image_file:
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
        image_file.save(image_path)
        predicted_class = predict_image_class(image_path)
        os.remove(image_path)  # Remove the uploaded image
        return predicted_class

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081,debug=True)
