import os
import dotenv
import streamlit as st
from model import DataModel
from view import DataViewer
from langchain_openai import OpenAI
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
dotenv.load_dotenv()

class DataController:
    def __init__(self):
        self.model = DataModel()
        self.viewer = DataViewer()
        self.llm = OpenAI(temperature=0)

    def process_user_input(self, user_csv):
        if user_csv is not None:
            self.model.load_csv(user_csv)

    def display_dataframes(self):
        loaded_dataframes = self.model.get_loaded_dataframes()
        self.viewer.show_dataframes(loaded_dataframes)
