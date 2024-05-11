import streamlit as st

from apikey import apikey
from controller import DataController
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import SmartDataframe
import matplotlib.pyplot as plt

import tempfile

def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=apikey)
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    plt.plot()
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(temp_file.name)
    plt.close()
    return result, temp_file.name

def extract_last_code_running(log_file):
    with open(log_file, 'r') as file:
        content = file.read()

    last_code_running_index = content.rfind("Code running:")

    if last_code_running_index != -1:
        start_index = content.find("```", last_code_running_index)
        end_index = content.find("```", start_index + 3)
        if start_index != -1 and end_index != -1:
            return content[start_index + 3:end_index].strip()

    return ""

log_file = "pandasai.log"
last_code_running = extract_last_code_running(log_file)
print(last_code_running)


def main():
    st.title('SquidTank 🦑')
    st.header('The AI data helper.')
    st.subheader("Solution:")

    controller = DataController()

    input_csvs = st.sidebar.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)
    st.write("Welcome! Squidtank is your personal data helper AI. He is able to analyze CSV, read PDF files, giving you SQL request based on your CSV etc.. Just ask him and he will answer you !")
    input_text = st.text_area("Enter the query")
    chat_button = st.button("Chat with csv")

    if input_csvs is not None:
        # Display uploaded files
        for csv_file in input_csvs:
            st.sidebar.write(f"{csv_file.name}")
            data = pd.read_csv(csv_file)
            with st.sidebar.expander(f"{csv_file.name}"):
                st.write(data)

            # Perform analysis
            if input_text and chat_button:
                st.info("Your Query: " + input_text)
                with st.spinner('Processing...'):
                    result, temp_file_path = chat_with_csv(data, input_text)
                    if plt.get_fignums():
                        st.image(temp_file_path)
                        log_file = "pandasai.log"
                        last_code_running = extract_last_code_running(log_file)
                        st.code(last_code_running)
                    else:
                        st.success(result)


if __name__ == "__main__":
    main()
