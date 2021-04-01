import streamlit as st
import pandas as pd
import datetime
import numpy as np
import re # to separate pages based on language (regular expression)
import matplotlib.pyplot as plt # to visualize data
from pandas.plotting import autocorrelation_plot # to visualize and configure the parameters of ARIMA model
from statsmodels.tsa.arima_model import ARIMA
import os
import time

import warnings
warnings.filterwarnings('ignore')

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

        list_of_column_names = list(df.columns)
        list_of_column_names.remove('Page')

        j = 0

        for i in range(1,len(list_of_column_names)):
            if i % 100 == 0:
                list_of_column_names[j] = list_of_column_names[i]
                j = j + 1


        x = [datetime.date(2015, 7, 1)] * 550

        def find_language(url):
            res = re.search('[a-z][a-z].wikipedia.org', url)
            if res:
                return res[0][0:2]
            return 'na'

        df['lang'] = df.Page.map(find_language)

        lang_sets = {}
        lang_sets['en'] = df[df.lang == 'en'].iloc[:, 0:-1]
        lang_sets['ja'] = df[df.lang == 'ja'].iloc[:, 0:-1]
        lang_sets['de'] = df[df.lang == 'de'].iloc[:, 0:-1]
        lang_sets['na'] = df[df.lang == 'na'].iloc[:, 0:-1]
        lang_sets['fr'] = df[df.lang == 'fr'].iloc[:, 0:-1]
        lang_sets['zh'] = df[df.lang == 'zh'].iloc[:, 0:-1]
        lang_sets['ru'] = df[df.lang == 'ru'].iloc[:, 0:-1]
        lang_sets['es'] = df[df.lang == 'es'].iloc[:, 0:-1]

        sums = {}
        for key in lang_sets:
            sums[key] = lang_sets[key].iloc[:, 1:].sum(axis=0) / lang_sets[key].shape[0]

        days = [r for r in range(sums['en'].shape[0])]

        for i in range(len(days) - 400):
            print(days[i])

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


        fig = plt.figure(1, figsize=[10, 10])
        fig, ax = plt.subplots()
        plt.ylabel('Views per Page')
        plt.xlabel('Day')
        plt.title('Pages in Different Languages')
        labels = {'en': 'English', 'ja': 'Japanese', 'de': 'German',
                  'na': 'Media', 'fr': 'French', 'zh': 'Chinese',
                  'ru': 'Russian', 'es': 'Spanish'
                  }


        # ax.plot_date(x, y, markerfacecolor='CornflowerBlue', markeredgecolor='white')

        for key in sums:
            plt.plot(days, sums[key], label=labels[key])
            # ax.plot_date(x, sums[key])

        # fig.autofmt_xdate()
        # ax.set_xlim([datetime.date(2015, 7, 1), datetime.date(2016, 12, 31)])
        # ax.set_ylim([2000,8000])
        plt.legend()
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

try:
    st.write(df.head(10))
except Exception as e:
    st.info('Fetching dataset...')
    print(e)

