import requests

# API endpoint
url = "http://127.0.0.1:5000/predict"

# Sample input data (make sure this matches the model's expected features)
data = {
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

# Send POST request
response = requests.post(url, json=data)

# Print response from the API
if response.status_code == 200:
    print("✅ Predicted Energy Usage (Wh):", response.json()['predicted_energy_usage_Wh'])
else:
    print("❌ Error:", response.status_code)
    print(response.json())
