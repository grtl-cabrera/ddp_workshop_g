import pandas as pd
import streamlit as st
print("Hello World")

st.write("This is our data app.")
st.title("My app")

df = pd.read_csv("Film_Locations_in_San_Francisco_20250423.csv")

st.dataframe(df)
