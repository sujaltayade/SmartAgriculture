# 🌱 Smart Agriculture Using Machine Learning

## 📌 Project Overview

Smart Agriculture is a machine-learning-based web application that provides crop and fertilizer recommendations based on agricultural input data.

The project aims to help users make more informed farming decisions by using machine learning algorithms to analyze soil properties and environmental conditions.

## 🎯 Objectives

- Recommend suitable crops based on soil nutrients and environmental conditions.
- Recommend fertilizers based on soil properties, crop type, and nutrient levels.
- Compare multiple machine learning algorithms for crop prediction.
- Provide a simple, user-friendly web interface for recommendations.

## ✨ Features

### 🌾 Crop Recommendation
Predicts a suitable crop using:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

### 🧪 Fertilizer Recommendation
Predicts a fertilizer category using:
- Temperature
- Humidity
- Soil moisture
- Soil type
- Crop type
- Nitrogen
- Potassium
- Phosphorus

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS
- JavaScript

## 🤖 Machine Learning Algorithms

The crop recommendation training script compares these algorithms:

1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors (KNN)
4. Support Vector Machine (SVM)
5. Gaussian Naive Bayes

Random Forest is used for the crop recommendation model. The fertilizer recommendation system uses a machine-learning pipeline with preprocessing and a Random Forest classifier.

## 📂 Project Structure

```text
SmartAgriculture/
├── app.py
├── requirements.txt
├── train_model.py
├── train_fertilizer.py
├── data/
├── models/
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sujaltayade/SmartAgriculture.git
```

### 2. Open the project folder

```bash
cd SmartAgriculture
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Train the models if the saved model files are missing

```bash
python train_model.py
python train_fertilizer.py
```

### 7. Run the Flask application

```bash
python app.py
```

Open the local address displayed in the terminal, typically:

`http://127.0.0.1:5000`

## 🔬 Project Scope

This project demonstrates how machine learning can be integrated into a web application to support crop and fertilizer recommendations. It is intended for educational and demonstration purposes.

## ⚠️ Limitations

- Predictions depend on the quality and coverage of the training datasets.
- Model accuracy on a test dataset does not guarantee real-world performance.
- Recommendations should be verified with soil testing and qualified agricultural advice before practical use.

## 🚀 Future Enhancements

- Integrate live weather data.
- Add more regional crop and soil datasets.
- Improve model validation using larger datasets.
- Add user accounts and recommendation history.
- Develop a mobile-friendly interface.

## 👨‍💻 Author

**Sujal Tayade**

## 📄 Disclaimer

This application is an educational machine learning project. Its predictions should not be treated as definitive agricultural advice.
