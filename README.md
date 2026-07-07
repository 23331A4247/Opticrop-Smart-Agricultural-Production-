# 🌱 OptiCrop — Smart Agricultural Production System

OptiCrop is a machine learning-based crop recommendation web application designed to help identify a suitable crop for cultivation based on soil nutrients and environmental conditions.

The system takes agricultural parameters such as nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall as input. A trained machine learning model analyzes these values and recommends a suitable crop.

## 📌 Project Overview

Agricultural productivity depends on several factors, including soil nutrients and climatic conditions. Choosing a suitable crop without considering these factors can reduce productivity and lead to inefficient use of agricultural resources.

OptiCrop provides a data-driven approach to crop selection. The application combines machine learning with a simple web interface so users can enter agricultural conditions and receive a crop recommendation.

## ✨ Features

* Machine learning-based crop recommendation
* Simple and user-friendly web interface
* Prediction based on seven agricultural parameters
* Fast crop prediction using a pre-trained model
* Separate pages for landing, home, and prediction input
* Integration of a trained ML model with a Flask web application

## 🌾 Input Parameters

The model uses the following seven parameters:

| Parameter   | Description                     |
| ----------- | ------------------------------- |
| N           | Nitrogen content in the soil    |
| P           | Phosphorus content in the soil  |
| K           | Potassium content in the soil   |
| Temperature | Environmental temperature in °C |
| Humidity    | Relative humidity in %          |
| pH          | pH value of the soil            |
| Rainfall    | Rainfall in mm                  |

## ⚙️ How It Works

1. The user opens the OptiCrop web application.
2. The user enters soil and environmental values.
3. The Flask backend collects the input data.
4. The values are converted into a format suitable for the trained model.
5. The machine learning model predicts the recommended crop.
6. The label encoder converts the encoded prediction into the crop name.
7. The recommended crop is displayed to the user.

## 🛠️ Technologies Used

### Programming and Machine Learning

* Python
* Pandas
* Scikit-learn
* Joblib
* Jupyter Notebook

### Web Development

* Flask
* HTML
* CSS

## 📂 Project Structure

```text
Smart-Agricultural-Production-/
│
├── README.md
│
└── Opticrop/
    ├── data/
    │   └── Crop_recommendation.csv
    │
    ├── static/
    │   └── [CSS and static assets]
    │
    ├── templates/
    │   ├── index.html
    │   ├── home.html
    │   └── inputs.html
    │
    ├── Opticrop.ipynb
    ├── app.py
    ├── crop_recommendation_model.pkl
    └── crop_recommendation_label_encoder.pkl
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/23331A4247/Opticrop-Smart-Agricultural-Production-.git
```

### 2. Open the project folder

```bash
cd Smart-Agricultural-Production-/Opticrop
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 5. Install the required libraries

```bash
pip install flask pandas scikit-learn joblib
```

### 6. Run the application

```bash
flask --app app run
```

### 7. Open the application

Open the local address shown in the terminal and navigate to:

```text
/opticrop
```

## 🧠 Machine Learning Workflow

The machine learning workflow is available in `Opticrop.ipynb`.

The general process includes:

1. Loading the crop recommendation dataset
2. Exploring and preparing the data
3. Separating input features and crop labels
4. Encoding crop labels
5. Training the machine learning model
6. Evaluating the model
7. Saving the trained model and label encoder
8. Integrating the saved model with the Flask application

## 📊 Dataset

The project uses `Crop_recommendation.csv`.

The dataset contains soil nutrient values and environmental conditions used to train the crop recommendation model.

### Input Features

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* pH
* Rainfall

### Target

* Recommended crop

## 🔮 Prediction Process

When a user submits the input form, the application:

1. Reads the seven input values.
2. Creates a Pandas DataFrame.
3. Sends the data to the trained machine learning model.
4. Generates an encoded prediction.
5. Uses the saved label encoder to recover the crop name.
6. Displays the predicted crop on the web page.

## 🎯 Objective

The objective of OptiCrop is to demonstrate how machine learning can support data-driven agricultural decisions by recommending crops based on soil and environmental conditions.

## 🔮 Future Improvements

Future versions of the project can include:

* Real-time weather API integration
* Soil sensor and IoT integration
* Fertilizer recommendations
* Crop disease detection
* Yield prediction
* Location-based recommendations
* Multilingual support for farmers
* Cloud deployment
* Improved mobile responsiveness

This project is developed for educational and academic purposes. Crop recommendations should not be treated as a replacement for professional agricultural advice or local soil testing.
