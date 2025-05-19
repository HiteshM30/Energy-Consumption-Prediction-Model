from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/appliances_energy_model.pkl")

# Define the features expected by the model
expected_features = [
    'lights', 'T1', 'RH_1', 'T2', 'RH_2', 'T3', 'RH_3',
    'T4', 'RH_4', 'T5', 'RH_5', 'T6', 'RH_6',
    'T7', 'RH_7', 'T8', 'RH_8', 'T9', 'RH_9',
    'T_out', 'Press_mm_hg', 'RH_out', 'Windspeed',
    'Visibility', 'Tdewpoint', 'rv1', 'rv2',
    'hour', 'day', 'weekday'
]

@app.route('/')
def home():
    return "🏠 Energy Consumption Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validate input
        missing = [f for f in expected_features if f not in data]
        if missing:
            return jsonify({'error': f'Missing fields: {missing}'}), 400

        # Convert input data into the right order
        input_values = [data[feature] for feature in expected_features]
        input_array = np.array([input_values])

        # Predict energy usage
        prediction = model.predict(input_array)[0]
        return jsonify({'predicted_energy_usage_Wh': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
