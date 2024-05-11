import streamlit as st

class DataViewer:
    @staticmethod
    def show_dataframes(loaded_dataframes):
        if loaded_dataframes:
            for name, df in loaded_dataframes.items():
                with st.expander(f"{name}:"):
                    st.write(df)
        else:
            st.write("Please first upload a csv file.")

