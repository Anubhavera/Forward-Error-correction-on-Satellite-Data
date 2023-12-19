from flask import Flask, render_template, request, redirect
import keras
import tensorflow as tf
app = Flask(__name__)
import numpy as np
global prediction

model = tf.keras.models.load_model("best.h5")
class_names = ["BCH", "HAMMING", "Convolutional", "Turbo"]

@app.route('/', methods=['GET'])
def landing():
    return render_template("/index.html")


@app.route('/process', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        select_val = request.form.get("modulator_type")
        print(select_val)
        f = request.files['file']
        title = f.filename
        f.save(f.filename)
        data = np.random.randint(0, 2, 856)
        data = np.array([[x] for x in data[:774]])
        data = np.expand_dims(data, axis=0)

        pred = model.predict(data)
        prediction = class_names[np.argmax(pred[0])]
        return render_template("landing.html", value=prediction)    
    return render_template("landing.html")

@app.route('/result', methods=['GET','POST'])
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)