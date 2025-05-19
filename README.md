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
```
energy-prediction/
│
├── app.py # Flask API application
├── model/
│ └── appliances_energy_model.pkl # Trained ML model
├── train_model.py # Script to train & save the model
├── send_request.py # Sample script to test API
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```
## 🚀 Setup Instruction
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

```
energy-prediction/
│
├── app.py                  # Flask API application
├── model/
│   └── appliances_energy_model.pkl   # Trained ML model
├── train_model.py          # Script to train & save the model
├── send_request.py         # Sample script to test API
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/energy-prediction.git
cd energy-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model (if not already trained)

```bash
python train_model.py
```

This will save the trained model as `models/appliances_energy_model.pkl`.

### 5. Start the Flask API

```bash
python app.py
```

The API will run at:  
**http://127.0.0.1:5000**

---

## 📡 API Usage

### Endpoint: `POST /predict`

**Request Format (JSON):**

```json
{
  "lights": 10,
  "T1": 19.89,
  "RH_1": 47.6,
  "T2": 19.2,
  "RH_2": 44.79,
  "T3": 19.79,
  "RH_3": 44.73,
  "T4": 19.0,
  "RH_4": 45.56,
  "T5": 17.2,
  "RH_5": 55.2,
  "T6": 7.0,
  "RH_6": 35.0,
  "T7": 17.0,
  "RH_7": 50.0,
  "T8": 17.0,
  "RH_8": 45.0,
  "T9": 17.0,
  "RH_9": 49.0,
  "T_out": 6.6,
  "Press_mm_hg": 733.5,
  "RH_out": 92.0,
  "Windspeed": 7.0,
  "Visibility": 63.0,
  "Tdewpoint": 5.3,
  "rv1": 13.2754,
  "rv2": 13.2754,
  "hour": 10,
  "day": 15,
  "weekday": 2
}
```

✅ All 31 features must be provided in the request.

**Response Format:**

```json
{
  "predicted_energy_usage_Wh": 90.31
}
```

---

## 🧪 Test with Python (`requests`)

You can test the API using `send_request.py`:

```bash
python send_request.py
```

---

## 🛠 Tech Stack

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- UCI Appliances Energy dataset

---

## 📈 Model Info

- Model: `RandomForestRegressor`
- Metrics: MAE, MSE, RMSE, R²
- Input Features: 31
- Target: Energy consumed by appliances (in Wh)

