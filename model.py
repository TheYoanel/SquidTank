from turtle import st

import pandas as pd
import streamlit as st
import os

class DataModel:
    def __init__(self):
        self.loaded_dataframes = {}

    def load_csv(self, csv_files):
        for csv_file in csv_files:
            df_name = os.path.basename(csv_file.name).split('.')[0]
            if df_name not in self.loaded_dataframes:  # Check if dataframe already loaded
                self.loaded_dataframes[df_name] = pd.read_csv(csv_file, low_memory=False)
            else:  # Update dataframe if already loaded
                self.loaded_dataframes[df_name] = pd.concat([self.loaded_dataframes[df_name], pd.read_csv(csv_file, low_memory=False)])

    def get_loaded_dataframes(self):
        return self.loaded_dataframes


    def load_pdf(self, pdf_files):
        pdf = st.file_uploader("Upload your PDF", type='pdf')
