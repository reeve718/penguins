import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import io
import sys
 
st.title("Penguine Speicy Prediction ML app")
st.info("This is end-to-end Machine Learning App")

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
    return df

with st.expander("Data"):
  st.write("Raw data")
  df = load_data()
  df
  st.write("Input variables")
  X_raw = df.drop(columns=['species'])
  X_raw
  st.write("Target variable")
  y_raw = df['species']
  y_raw
  st.write("Descriptive statistics")
  st.write(df.describe())
  st.write("More information about data")
  #st.write(f"Data shape: {df.info()}")
  buffer = io.StringIO()
  df.info(buf=buffer)
  info_string = buffer.getvalue()
  st.text(info_string)

with st.expander("Data Visualization"):
  pass
 
with st.expander("Data Preperation"):
  pass
 
with st.sidebar:
    st.header("Input Variables")
    island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
    bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill Depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper Length (mm)', 172.0, 231.0, 190.0)
    body_mass_g = st.slider('Body Mass (g)', 2700.0, 6300.0, 4207.0)
    gender = st.selectbox('Gender',('male','female'))

    data = {'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm, 
            'body_mass_g': body_mass_g,
            'gender': gender}
    features = pd.DataFrame(data, index=[0])
    input_df = pd.concat([X_raw, features], axis=0)

with st.expander("Input data"):
    st.write("Input variables")
    features
    st.write("Target variable")
    input_df

encode = ["island", "sex"]
