import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
 
st.title("Penguine Speicy Prediction ML app")
st.info("This is end-to-end Machine Learning App")
 
with st.expander("Data"):
  pass
 
with st.expander("Data Visualization"):
  pass
 
with st.expander("Input data"):
  pass
 
with st.expander("Data Preperation"):
  pass
 
with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)