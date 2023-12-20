from flask import Flask, render_template, request, redirect
import keras
import tensorflow as tf
app = Flask(__name__)
import numpy as np
global model

model = tf.keras.models.load_model("best.h5")

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
        print(title)
        class_names = ["BCH", "HAMMING", "Convolutional", "Turbo"]

        with open(title, "r+") as f:
            result = f.readlines()

        val = []
        for i in result:
            val.append(i[:-1])

        t = ""
        for i in range(len(val)):
            if len(val[i])<774:
                t = val[i]
                for j in range(abs(774-len(val[i]))):
                    t+="0"
                val[i] = t
            if len(val[i])>774:
                val[i] = val[i][:774]


        x_pred = []
        for i in val:
            x_pred.append(list(i))

        final_data=[]
        for i in x_pred:
            final_data.append([[float(x)] for x in i])

        final_data = np.array(final_data)
        print(final_data.shape)
    
        pred = model.predict(final_data)
        print("*"*12)
        print(pred)
        predictions = [class_names[np.argmax(x)] for x in pred]
        val = "All derived classes: "
        with open("result.txt", "w+") as file:
            file.write(str(predictions))

        return render_template("process.html", value=str(predictions), value2=val)  
    return render_template("process.html")

@app.route('/result', methods=['GET','POST'])
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)