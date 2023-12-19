from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
    return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)