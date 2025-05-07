from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load only the Keras model
keras_model = load_model("calories_model.h5", compile=False)

# Encode gender
def encode_gender(gender_str):
    return 1 if gender_str.lower() == 'male' else 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        gender = request.form['Gender']
        age = float(request.form['Age'])
        height = float(request.form['Height'])
        weight = float(request.form['Weight'])
        duration = float(request.form['Duration'])
        heart_rate = float(request.form['Heart_Rate'])
        body_temp = float(request.form['Body_Temp'])

        encoded_gender = encode_gender(gender)

        # Prepare input
        user_input = np.array([[encoded_gender, age, height, weight, duration, heart_rate, body_temp]])

        # Keras prediction
        keras_prediction = round(keras_model.predict(user_input).flatten()[0], 2)

        # Determine calorie level
        if keras_prediction < 200:
            calorie_level = "Low"
            suggestions = "For low calorie needs, prioritize protein, fiber, and hydration. Avoid liquid calories."
        elif 200 <= keras_prediction <= 400:
            calorie_level = "Medium"
            suggestions = "For medium calorie needs, focus on balanced macronutrients, healthy fats, and regular activity."
        else:
            calorie_level = "High"
            suggestions = "For high calorie needs, increase caloric intake with nutrient-dense foods, include protein and healthy fats, and engage in strength training."

        return render_template('index.html',
                               keras_prediction=keras_prediction,
                               calorie_level=calorie_level,
                               suggestions=suggestions,
                               input_values={
                                   'Gender': gender,
                                   'Age': age,
                                   'Height': height,
                                   'Weight': weight,
                                   'Duration': duration,
                                   'Heart_Rate': heart_rate,
                                   'Body_Temp': body_temp
                               })
    except Exception as e:
        return f"An error occurred: {str(e)}"

app.run(host='0.0.0.0', port=4050, debug=True)