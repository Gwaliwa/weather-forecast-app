#import libraries
import streamlit as st
import plotly.express as px
from backend import get_data

#the interface widgets
st.title("Weather Forecast App")
place = st.text_input("Place")
days = st.slider("Forecast Days", 1, 5, help="Number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

kind = get_data(place, days, option)

#import graps functions
figure = px.line(x=dates, y=kind, labels={'x':'Date', 'y':'Temperature'})
st.plotly_chart(figure)
