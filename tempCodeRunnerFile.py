
# model = tf.keras.saving.load_model("best.h5")

# @app.route('/', methods=['GET'])
# def landing():
#     return render_template("/index.html")

# @app.route('/process', methods=['POST', 'GET'])
# def home():
#     if request.method == 'POST':
#         select_val = request.form.get("modulator_type")
#         print(select_val)
#         f = request.files['file']
#         title = f.filename
#         f.save(f.filename)
        

#     return render_template("landing.html")

# @app.route('/result', methods=['GET','POST'])
# def result():
#     return render_template('result.html')

# if __name__ == "__main__":
#     app.run(debug=True)