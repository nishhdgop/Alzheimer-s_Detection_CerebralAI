import matplotlib.pyplot as plt
import numpy as np
import cv2
from flask import Flask, render_template, request
import tensorflow as tf
import reportMail

new_model = tf.keras.models.load_model('trained_model.hdf5')
app = Flask(__name__)
predictions = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

def predict_new(path):
    img = cv2.imread(path)
    RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    RGBImg = cv2.resize(RGBImg, (180,180))
    plt.imshow(RGBImg)
    image = np.array(RGBImg) / 255.0
    predict = new_model.predict(np.array([image]))
    pred = np.argmax(predict, axis=1)
    a = predictions[pred[0]]
    return a

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    name = request.form['name']
    age = request.form['age1']
    emailId = request.form['emailId']
    contact = request.form['contact']
    symptoms=request.form['symptoms']
    imagefile = request.files['imagefile']
    image_path = "images/"+imagefile.filename
    imagefile.save(image_path)
    predicted_value = predict_new(image_path)
    print(name,age, emailId,contact,symptoms,predicted_value)
    reportMail.send(name,age,emailId,contact,symptoms,predicted_value)
    return render_template('index.html', name=name, emailId=emailId, predicted_value=predicted_value)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
