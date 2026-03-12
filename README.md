# 🚔 Crime Detection and Risk Analysis System

## 📌 Project Overview

The **Crime Detection and Risk Analysis System** is an AI-based web
application that predicts the type of crime based on various input
factors.\
The system analyzes crime-related attributes such as **city, time of
occurrence, victim details, weapon used, and police deployment** to
predict the possible crime type and assess the **risk level**.

This project integrates **Machine Learning with a web interface** to
provide an interactive platform for **crime prediction and risk
evaluation**.

------------------------------------------------------------------------

## 🎯 Objectives

-   Analyze crime-related data using **machine learning techniques**
-   Predict the **possible type of crime** based on input parameters
-   Calculate and display a **risk level** for the predicted crime
    scenario
-   Provide an **easy-to-use web interface** for crime prediction

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python**
-   **Flask**
-   **HTML**
-   **CSS**
-   **JavaScript**
-   **Machine Learning**
-   **Random Forest Algorithm**

------------------------------------------------------------------------

## 📚 Libraries Used

-   `pandas`
-   `numpy`
-   `scikit-learn`
-   `pickle`
-   `flask`

------------------------------------------------------------------------

## ⚙️ System Architecture

The system consists of **three main components**:

### 1️⃣ Data Processing

The dataset is cleaned and preprocessed using **pandas**.\
Categorical values are converted into numerical values using **Label
Encoding**.

### 2️⃣ Machine Learning Model

A **Random Forest Classifier** is trained using the processed dataset to
predict the **crime type**.

### 3️⃣ Web Application

A **Flask-based web application** collects user input and sends it to
the trained model.\
The predicted crime and risk level are then displayed on the interface.

------------------------------------------------------------------------

## 🧾 Input Features

The model takes the following features as input:

-   City
-   Time of Occurrence
-   Victim Age
-   Victim Gender
-   Weapon Used
-   Police Deployed

------------------------------------------------------------------------

## 🎯 Target Feature

-   **Crime Description (Predicted Crime Type)**

### Examples of Predicted Crimes

ARSON

ASSAULT

BURGLARY

COUNTERFEITING

CYBERCRIME

DOMESTIC VIOLENCE

DRUG OFFENSE

EXTORTION

FIREARM OFFENSE

FRAUD

HOMICIDE

IDENTITY THEFT

ILLEGAL POSSESSION

KIDNAPPING

PUBLIC INTOXICATION

ROBBERY

SEXUAL ASSAULT

SHOPLIFTING

TRAFFIC VIOLATION

VANDALISM

VEHICLE - STOLEN

------------------------------------------------------------------------

## 🤖 Algorithms Used

### 1️⃣ Random Forest Classifier

Used for **predicting the type of crime**.

### 2️⃣ Label Encoding

Used to convert **categorical data into numerical format** for model
training.

### 3️⃣ Train-Test Split

Used to divide the dataset into **training and testing sets** for model
evaluation.

------------------------------------------------------------------------

## 📂 Project Structure

    CrimeDetectionRiskAnalysis
    │
    ├── dataset
    │   └── crime_dataset_india.csv
    │
    ├── templates
    │   └── index.html
    │
    ├── train_model.py
    ├── app.py
    ├── crime_model.pkl
    └── README.md

------------------------------------------------------------------------

## ⚡ Installation and Setup

### 1️⃣ Install Python

Download and install Python from https://www.python.org/downloads/

### 2️⃣ Install Required Libraries

``` bash
pip install pandas numpy scikit-learn flask
```

### 3️⃣ Train the Model

``` bash
python train_model.py
```

### 4️⃣ Run the Flask Application

``` bash
python app.py
```

### 5️⃣ Open the Application in Browser

http://127.0.0.1:5000

------------------------------------------------------------------------

## ✨ Features

-   AI-based **crime prediction**
-   **Risk level analysis** (Low, Medium, High)
-   **User-friendly web interface**
-   **Machine learning integration**
-   **Real-time prediction**

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   Integration with **real-time crime datasets**
-   Advanced **deep learning models**
-   Interactive **dashboards and data visualization**
-   **Mobile application support**

