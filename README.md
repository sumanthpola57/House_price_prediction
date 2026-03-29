# 🏠 House Price Prediction App

An end-to-end Machine Learning project that predicts house prices using an XGBoost model, with a FastAPI backend and Streamlit frontend.

---

## 🚀 Features

* 📊 Machine Learning model (XGBoost)
* ⚡ FastAPI backend for predictions
* 🖥️ Streamlit interactive UI
* 🌐 Ready for deployment (Render + Streamlit Cloud)

---

## 🧠 Model Details

* Algorithm: XGBoost Regressor
* Features used:

  * grade
  * sqft_living
  * lat
  * view
  * waterfront
  * sqft_living15
  * long

---

## 📁 Project Structure

```
House_price_prediction/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── ui.py
│
├── model/
│   └── xgb.pkl
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/sumanthpola57/House_price_prediction.git
cd House_price_prediction
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run FastAPI backend

```
uvicorn backend.main:app --reload
```

---

### 4. Run Streamlit frontend

```
streamlit run frontend/ui.py
```

---

## 🔗 API Endpoint

* **POST /predict**
* Input: JSON data with features
* Output: Predicted house price

Example:

```
{
  "grade": 7,
  "sqft_living": 1500,
  "lat": 47.5,
  "view": 0,
  "waterfront": 0,
  "sqft_living15": 1500,
  "long": -122.2
}
```

---

## 🌐 Deployment

* Backend: Render
* Frontend: Streamlit Cloud

---

## 📌 Future Improvements

* Add better UI design
* Add feature importance visualization
* Add user authentication
* Deploy with Docker

---

## 👨‍💻 Author

Sumanth Pola

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
