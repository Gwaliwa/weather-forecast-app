import streamlit as st

st.title("Weather Forecast App")
place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, help="Number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

