import os
import dotenv
import streamlit as st
import pandas as pd
from langchain_openai import OpenAI
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey

# Load environment variables from .env file
dotenv.load_dotenv()

# Retrieve API key from environment variables

st.title('SquidTank 🦑')
st.header('The AI data helper.')
st.subheader("Solution:")

# Définir une liste pour stocker les DataFrames chargés
loaded_dataframes = st.session_state.get('loaded_dataframes', {})
texte = st.text_area("Welcome! Squidtank is your personal data helper AI. He is able to analyze CSV, read PDF files, giving you SQL request based on your CSV etc.. Just ask him and he will answer you !", "")

llm = OpenAI(temperature = 0)

with st.sidebar:
    st.image('https://images.emojiterra.com/google/noto-emoji/unicode-15/animated/1f419.gif', width=48)
    st.title('Options')
    st.divider()
    user_csv = st.file_uploader("Upload :", type="csv", accept_multiple_files=True)  # Accepter plusieurs fichiers
    if user_csv is not None:
        for csv_file in user_csv:
            df_name = os.path.basename(csv_file.name).split('.')[0]
            df = pd.read_csv(csv_file, low_memory=False)
            if df_name not in loaded_dataframes:  # Vérifier si le nom du DataFrame n'est pas déjà utilisé
                loaded_dataframes[df_name] = df  # Ajouter le DataFrame à la liste
        # Mettre à jour la session avec les nouveaux DataFrames chargés
        st.session_state.loaded_dataframes = loaded_dataframes

    # Bouton pour afficher les DataFrames chargés
    if st.button("Afficher mes BDD"):
        if loaded_dataframes:
            for idx, (name, df) in enumerate(loaded_dataframes.items()):
                with st.expander(f"{name}:"):
                    st.write(df)
        else:
            st.write("Please first upload a csv file.")
    st.divider()
    st.write('Informations:')
    st.caption("Here you can find all the related information about the different options available.")
    with st.expander("CSV Reader :"):
        st.write('Txt')
    st.divider()
