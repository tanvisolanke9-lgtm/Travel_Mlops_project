from flask import Flask, request, jsonify
import joblib

# Flask app create
app = Flask(__name__)

# Load trained model
model = joblib.load("flight_price_model.pkl")

# Home route
@app.route("/")
def home():
    return "Flight Price Prediction API Running"

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.get_json()
    
    # Features from request
    features = data["features"]
    
    # Prediction
    prediction = model.predict([features])
    
    return jsonify({
        "prediction": prediction.tolist()
    })


# Run server
if __name__ == "__main__":
    app.run(debug=True)