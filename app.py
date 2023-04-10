import sys
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import cv2
from flask import Flask, render_template, request
import tensorflow as tf
import concurrent.futures
import reportMail
import pyttsx3

new_model = tf.keras.models.load_model('trained_model.hdf5')
app = Flask(__name__)
predictions = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

def typing(text):
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

def textToSpeech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 220)
    engine.say(text)
    engine.runAndWait()
    del engine

def parallel(text):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_tasks = {executor.submit(
            textToSpeech, text), executor.submit(typing, text)}
        for future in concurrent.futures.as_completed(future_tasks):
            try:
                data = future.result()
            except Exception as e:
                print(e)

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
    parallel(f"Your stage is {predicted_value}")
    reportMail.send(name,age,emailId,contact,symptoms,predicted_value)
    return render_template('index.html', name=name, emailId=emailId, predicted_value=predicted_value)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
