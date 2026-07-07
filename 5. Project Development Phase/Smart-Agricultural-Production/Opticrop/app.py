from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("crop_recommendation_model.pkl")
label_encoder = joblib.load("crop_recommendation_label_encoder.pkl")

@app.route('/opticrop')
def index():
    return render_template('index.html')

@app.route('/opticrop-home')
def home():
    return render_template('home.html')

@app.route('/opticrop-inputs')
def inputs():
    return render_template('inputs.html')

@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    input_data = pd.DataFrame([{
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])

    prediction = model.predict(input_data)

    crop = label_encoder.inverse_transform(prediction)[0]

    return render_template("inputs.html", crop=crop)


