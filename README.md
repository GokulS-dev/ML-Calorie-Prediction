#  ML Calorie Prediction

This project is a machine learning web application built using Python and Flask that predicts the number of calories burned during physical activity. It uses a trained machine learning model (`random_forest_model.pkl`) and includes a simple HTML UI for users to input physical metrics and view calorie predictions.

---

##  Project Overview

- `app.py` – Flask backend server handling requests and predictions.
- `calories_model.h5` – Saved deep learning model (optional model variant).
- `random_forest_model.pkl` – Trained Random Forest model used for predictions.
- `feature_columns.pkl` – Saved feature structure for consistent preprocessing.
- `templates/index.html` – Frontend form for input and result display.

---

##  Features

- Predict calories burned based on:
  - Gender
  - Age
  - Height
  - Weight
  - Duration
  - Heart rate
  - Body temperature
- Built with Flask for backend logic.
- Clean and user-friendly HTML frontend.
- ML models trained and serialized for fast prediction.

---

##  How to Use

To run this project:
1. Clone the repository and open the folder.
2. Ensure all required files (`app.py`, models, templates) are present.
3. Install Flask and required dependencies.
4. Run `app.py` to start the local server.
5. Open your browser and navigate to `http://127.0.0.1:5000` to access the app.
6. Enter your details and get instant calorie predictions.

---

##  Author

- [GokuLS-dev](https://github.com/GokuLS-dev)
