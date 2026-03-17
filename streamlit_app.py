import streamlit as st
import requests
import pandas as pd

st.title("Travel Analytics Dashboard")

# ---- Flight Price Prediction ----

st.header("Flight Price Prediction")

distance = st.number_input("Enter Flight Distance")
time = st.number_input("Enter Flight Time")

if st.button("Predict Price"):

    data = {
    "features": [distance, time]
    }

    response = requests.post("http://127.0.0.1:5000/predict", json=data)

    result = response.json()

    st.success(f"Predicted Flight Price: {result['price']}")

# ---- Hotel Insights ----

df = pd.read_csv("hotels.csv")

st.header("Hotel Data Insights")

st.subheader("Top Hotel Locations")
st.bar_chart(df["place"].value_counts())

st.subheader("Average Price by Location")
st.bar_chart(df.groupby("place")["price"].mean())

st.header("Hotel Recommendation")

places = df["place"].unique()

selected_place = st.selectbox("Select Location", places)

filtered_hotels = df[df["place"] == selected_place]

st.subheader("Recommended Hotels")

st.write(filtered_hotels[["name","price","days"]].head())