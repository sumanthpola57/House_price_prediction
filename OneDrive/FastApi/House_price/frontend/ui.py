import streamlit as st
import requests
import pandas as pd

# -------------------------
# 1️⃣ App config
# -------------------------
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")
st.title("🏠 House Price Prediction App")
st.write("Enter the top 7 house features using sliders and click Predict.")

# -------------------------
# 2️⃣ Load median values for other features
# -------------------------
df = pd.read_csv(
    "https://raw.githubusercontent.com/Shreyas3108/house-price-prediction/master/kc_house_data.csv"
)
df.drop(['id', 'date', 'price'], axis=1, inplace=True)
median_values = df.median()

# -------------------------
# 3️⃣ User input (Top 7) in 2 columns
# -------------------------
with st.form("house_form"):
    col1, col2 = st.columns(2)

    with col1:
        grade = st.slider("Grade (1-13)", min_value=1, max_value=13, value=7)
        sqft_living = st.slider("Living Area (sqft)", min_value=300, max_value=10000, value=1800)
        lat = st.slider("Latitude", min_value=47.0, max_value=47.8, value=47.5)
        view = st.slider("View (0-4)", min_value=0, max_value=4, value=0)

    with col2:
        waterfront = st.select_slider("Waterfront", options=[0,1], value=0)
        sqft_living15 = st.slider("Living15 (sqft)", min_value=300, max_value=8000, value=1700)
        long = st.slider("Longitude", min_value=-122.5, max_value=-121.5, value=-122.2)

    submit = st.form_submit_button("Predict Price")

# -------------------------
# 4️⃣ Prediction logic
# -------------------------
if submit:
    st.info("Predicting price...")

    # Prepare input dictionary with top 7 from user
    data = {
        "grade": grade,
        "sqft_living": sqft_living,
        "lat": lat,
        "view": view,
        "waterfront": waterfront,
        "sqft_living15": sqft_living15,
        "long": long
    }

    # Fill remaining 11 features with median values
    for col in df.columns:
        if col not in data:
            data[col] = float(median_values[col])

    # Call FastAPI backend
    try:
        response = requests.post("https://house-price-prediction-1-ck7o.onrender.com/predict", json=data)
        result = response.json()
        st.success(f"💰 Predicted House Price: ${result['prediction']:.2f}")
    except Exception as e:
        st.error(f"Error calling API: {e}")

# -------------------------
# 5️⃣ Footer
# -------------------------
st.markdown("---")
st.write("Built by mawa 😎 | FastAPI + XGBoost + Streamlit")