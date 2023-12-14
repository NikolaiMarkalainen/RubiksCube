
UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

import os


from flask import render_template
from flask_cors import CORS
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

import numpy as np
import tensorflow as tf
import base64

from tensorflow.keras.preprocessing import image
from keras.models import load_model


app = Flask(__name__)
CORS(app)

#verifying data 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#loading ai model
def load_model_from_file():

    myModel = load_model('saved_model.h5')
    return (myModel)


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print("SHOULD BE HERE", request)
        # Request has files in it
        if 'file' not in request.json:
            print(request.json['file'])
            return jsonify({'message': 'Error: No file part'})
        file = request.json['file']
        # If filename is empty
        if 'fileName' not in request.json:
            return jsonify({'message': 'Error: No selected file'})
        filename = request.json['fileName']
        if not allowed_file(filename):
            return jsonify({'message': 'Error: Wrong file format'})
        if file and allowed_file(filename):
            print("should be here as everything matches")
            filename = secure_filename(filename)
            img_data = base64.b64decode(file)
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            with open(img_path, 'wb') as f:
                f.write(img_data)
            result = uploaded_file(filename)
        if result < 0.5:
            return jsonify({'message': 'Uploaded image is a rubiks cube'})
        else:
            return jsonify({'message': 'Not a cube'})
        
def uploaded_file(filename):
    test_image = image.load_img(UPLOAD_FOLDER + "/" + filename, target_size=(128, 128))
    test_image = image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)

    myModel = app.config['MODEL']
    result = myModel.predict(test_image)
    image_src = "./" + UPLOAD_FOLDER + "/" + filename
    return result

def main():
    (myModel) = load_model_from_file()
    
    app.config['SECRET_KEY'] = 'super_secret_key'
    app.config['MODEL'] = myModel
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.run(port=5001)

results = []




main()