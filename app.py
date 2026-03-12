from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("crime_model.pkl","rb"))

# Load encoders
le_city = pickle.load(open("le_city.pkl","rb"))
le_time = pickle.load(open("le_time.pkl","rb"))
le_gender = pickle.load(open("le_gender.pkl","rb"))
le_weapon = pickle.load(open("le_weapon.pkl","rb"))
le_crime = pickle.load(open("le_crime.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        print("Incoming data:", data)

        # Safe transform function
        def safe_transform(encoder, value):
            if value in encoder.classes_:
                return encoder.transform([value])[0]
            else:
                return 0

        city = safe_transform(le_city, data["city"])
        time = safe_transform(le_time, data["time"])
        gender = safe_transform(le_gender, data["gender"])
        weapon = safe_transform(le_weapon, data["weapon"])

        age = int(data["age"])
        police = int(data["police"])

        features = np.array([[city, time, age, gender, weapon, police]])

        prediction = model.predict(features)[0]

        crime_name = le_crime.inverse_transform([prediction])[0]

        return jsonify({"crime": crime_name})

    except Exception as e:

        print("Prediction Error:", e)

        return jsonify({
            "crime": "Error in Prediction"
        })


if __name__ == "__main__":
    app.run(debug=True)