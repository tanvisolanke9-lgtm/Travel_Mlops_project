# Travel_Mlops_project
# ✈️ Flight Price Prediction using MLOps

## 📌 Project Overview

This project focuses on predicting flight ticket prices using machine learning while implementing an end-to-end MLOps pipeline. The system processes historical flight data, trains a regression model, and deploys it using modern tools for real-world usage.

It combines data preprocessing, model building, API deployment, containerization, and workflow automation into a single scalable solution.

---

## 🎯 Objectives

* Build a machine learning model to predict flight prices
* Automate the workflow using Airflow
* Deploy the model using a REST API
* Create an interactive dashboard for users
* Ensure scalability using Docker and Kubernetes

---

## 🚀 Features

* Accurate flight price prediction
* User-friendly Streamlit interface
* REST API for external access
* Automated pipeline using Airflow
* Containerized deployment
* Scalable infrastructure

---

## 📋 Tasks Performed

* Data collection and analysis
* Data cleaning and preprocessing
* Feature engineering
* Model training and evaluation
* API development using Flask
* Frontend development using Streamlit
* Docker containerization
* Kubernetes deployment
* Workflow scheduling using Airflow

---

## 📊 Dataset Information

The dataset contains flight-related details used for training the model.

**Key Features:**

* Source (`from`)
* Destination (`to`)
* Flight Type (`flightType`)
* Distance (`distance`)
* Time (`time`)
* Agency (`agency`)
* Date (`date`)
* Price (`price`) – Target variable

The dataset is preprocessed to remove unnecessary columns, handle missing values, and convert categorical data into numerical format.

---

## 🏗️ Project Structure


flight-price-mlops/
│
├── dags/                  # Airflow DAGs
├── src/                   # Training & preprocessing scripts
├── app/                   # Flask API
├── model/                 # Saved model (model.pkl)
├── requirements.txt
├── Dockerfile
/-ci/cd with jenkins
/-mlflow
└── README.md
```

---

## ⚙️ Workflow


Data → Preprocessing → Model Training → Flask API → Streamlit → Docker → Kubernetes → Airflow
```

---

## 🔄 Airflow DAG Explanation

Apache Airflow is used to automate and manage the machine learning pipeline.

The DAG (Directed Acyclic Graph) defines a sequence of tasks:

* Data loading
* Data preprocessing
* Model training
* Saving the model
* Running predictions

Each task is executed in a defined order, ensuring smooth workflow automation and scheduling.

---

## 🌐 REST API (Flask)

The trained model is deployed using Flask.

python app/app.py
```

Endpoints:

* `/` → API status
* `/predict` → Get predictions

---

## 🎨 Streamlit Dashboard

A user-friendly dashboard is created using Streamlit.


streamlit run app.py
```

Users can:

* Enter flight details
* Get instant price predictions
* Interact with the system easily

---

## 🐳 Docker Deployment

```bash id="k5p2jd"
docker build -t flight-api .
docker run -p 5000:5000 flight-api
```

---

## ☸️ Kubernetes Deployment


kubectl apply -f deployment.yml
kubectl apply -f service.yml
```

---

## 🎯 Conclusion

This project demonstrates how machine learning models can be effectively deployed using MLOps practices. It integrates multiple tools to automate workflows, improve scalability, and provide real-time predictions.

The combination of Airflow, Flask, Streamlit, Docker, and Kubernetes makes the system robust, efficient, and suitable for production environments.

---

