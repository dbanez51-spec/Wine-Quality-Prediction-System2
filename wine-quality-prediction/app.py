# app.py - Wine Quality Prediction System (Section B)
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="wide"
)


@st.cache_resource
def load_model():
    # Load the trained model only once
    return joblib.load("wine_model.pkl")


model = load_model()
data = pd.read_csv("wine_quality.csv")

st.title("🍷 Wine Quality Prediction System")
st.caption("Section B classroom prototype for preliminary quality classification")

# Basic dataset information
c1, c2, c3 = st.columns(3)
c1.metric("Records", len(data))
c2.metric("Average quality score", round(data["quality"].mean(), 2))
c3.metric("Good-quality records", int((data["quality"] >= 6).sum()))

st.subheader("Dataset preview")
st.dataframe(data.head(10), use_container_width=True)

st.subheader("Predict uploaded wine samples")
st.write("Upload a CSV containing the same predictor columns as the training data.")

# Sample file the user can download and upload back
template = data.drop(columns=["quality"]).head(5)
st.download_button(
    "Download sample input CSV",
    template.to_csv(index=False),
    "sample_wine_input.csv",
    "text/csv"
)

uploaded = st.file_uploader("Choose wine sample CSV", type=["csv"])

if uploaded is not None:
    new_data = pd.read_csv(uploaded)

    # Columns the model was trained on
    required_columns = list(model.feature_names_in_)
    missing = [c for c in required_columns if c not in new_data.columns]

    if missing:
        st.error("Missing required columns: " + ", ".join(missing))
    else:
        predictions = model.predict(new_data[required_columns])

        results = new_data.copy()
        results["Prediction"] = [
            "GOOD QUALITY" if value == 1 else "NEEDS IMPROVEMENT"
            for value in predictions
        ]

        st.subheader("Prediction results")
        st.dataframe(results, use_container_width=True)
        st.metric("Predicted good-quality samples", int((predictions == 1).sum()))

        st.download_button(
            "Download prediction results",
            results.to_csv(index=False),
            "wine_quality_predictions.csv",
            "text/csv"
        )

st.info(
    "Responsible use: this is a classroom prototype. A prediction is not a "
    "substitute for laboratory testing, sensory evaluation, food-safety "
    "procedures, or professional quality-control decisions."
)
