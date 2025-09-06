import requests
import json

url = "http://127.0.0.1:5002/invocations"
headers = {"Content-Type": "application/json"}

data = {
    "dataframe_records": [
        {
            "mean radius": 17.99,
            "mean texture": 10.38,
            "mean perimeter": 122.8,
            "mean area": 1001.0,
            "mean smoothness": 0.1184,
            "mean compactness": 0.2776,
            "mean concavity": 0.3001,
            "mean concave points": 0.1471,
            "mean symmetry": 0.2419,
            "mean fractal dimension": 0.0787,
            "radius error": 1.095,
            "texture error": 0.9053,
            "perimeter error": 8.589,
            "area error": 153.4,
            "smoothness error": 0.0064,
            "compactness error": 0.049,
            "concavity error": 0.0537,
            "concave points error": 0.0159,
            "symmetry error": 0.03003,
            "fractal dimension error": 0.0062,
            "worst radius": 25.38,
            "worst texture": 17.33,
            "worst perimeter": 184.6,
            "worst area": 2019.0,
            "worst smoothness": 0.1622,
            "worst compactness": 0.6656,
            "worst concavity": 0.7119,
            "worst concave points": 0.2654,
            "worst symmetry": 0.4601,
            "worst fractal dimension": 0.1189
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Prediction result:", response.json())
