# ⚡ Energy Consumption Prediction

This project predicts appliance energy usage (in Wh) using a machine learning model trained on household environmental data. The model is exposed via a Flask-based REST API, enabling real-time energy usage predictions from JSON input.

---

## 📁 Dataset

We use the **Appliances Energy Prediction Data Set** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction).

- The dataset contains features such as:
  - Indoor and outdoor temperatures and humidity (`T1`, `RH_1`, …, `T9`, `RH_9`)
  - Weather conditions (`T_out`, `RH_out`, `Windspeed`, etc.)
  - Timestamp features (`hour`, `day`, `weekday`)
  - Target: `Appliances` energy use in Wh

---

## 📦 Project Structure

energy-prediction/
│
├── app.py # Flask API application
├── model/
│ └── appliances_energy_model.pkl # Trained ML model
├── train_model.py # Script to train & save the model
├── send_request.py # Sample script to test API
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/energy-prediction.git
cd energy-prediction
