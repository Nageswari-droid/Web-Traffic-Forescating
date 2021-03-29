import streamlit as st
import pandas as pd
import os
import time

import warnings
warnings.filterwarnings('ignore')

import re # to separate pages based on language (regular expression)
import matplotlib.pyplot as plt # to visualize data
from statsmodels.tsa.arima_model import ARIMA


import numpy as np

image = '.\\undraw_fast_loading_0lbh.png'

st.title("Web Traffic Forecasting")
st.header("Problem Statement")
st.write("Web traffic congestion is a scenario faced by network appliction frequently.")
st.write("Web traffic congestion is a phenomenum where the number of requests to be fulfilled by the server increases beyond the resource allocation.")
st.image(image, caption=None, width=300, use_column_width=None)
st.header("Solution")
st.write("A prediction model which analyzes the web traffic pattern of the target server and thus the server resources are allocated in advance to handle the server load.")

st.sidebar.header("Visualisation Settings")
uploaded_file = st.sidebar.file_uploader(label="Upload your web traffic dataset(.csv)", type=['csv','xslx'])

st.sidebar.image("undraw_Data_trends_re_2cdy.png",caption=None, width=300, use_column_width=None)

global df
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file).fillna(0)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

try:
    st.write(df.head(10))
except Exception as e:
    st.info('Fetching dataset...')
    print(e)

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)
#
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)
#
# progress_bar.empty()
#
# st.button("Re-run")