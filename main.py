import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

columns = (df.columns[1], df.columns[2], df.columns[6])

st.title("In Search for Hapiness")
x_axis = st.selectbox("Select the data for the X-axis",
             (columns))
x_axis = x_axis
y_axis = st.selectbox("Select the data for the Y-axis",
             (columns))
y_axis =y_axis
st.subheader(f"{x_axis} and {y_axis}")

def get_data(data_x0, data_y0):
    data_x1 = df[f"{data_x0}"]
    data_y1 = df[f"{data_y0}"]
    return data_x1,data_y1

x, y = get_data(x_axis, y_axis)



figure = px.scatter(x=x, y=y, labels={"x": x_axis, "y":y_axis})
st.plotly_chart(figure)

