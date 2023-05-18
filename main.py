import streamlit as st
import plotly.express as px

st.title("In Search for Hapiness")
x_axis = st.selectbox("Select the data for the X-axis",
             ("GDP", "Hapiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-axis",
             ("GDP", "Hapiness", "Generosity"))
st.subheader(f"{x_axis} and {y_axis}")

figure = px.line(x=, y=, labels=)
st.plotly_chart(figure)

