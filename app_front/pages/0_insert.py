import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ROOT_URL =  f"http://{os.getenv('API_BASE_URL')}:{os.getenv('FAST_API_PORT', '8000')}"
API_URL =  API_ROOT_URL + "/insert"

st.title("Insertion")

with st.form("insert_form"):
    new_word = st.text_area("Inserez un mot")
    submitted = st.form_submit_button("Ajouter à la base de données")
    if submitted :
        data = {"word":new_word}
        st.info("envoi à l'API")
        try : 
            response = requests.post(API_URL, json=data)

            if response.status_code == 200:
                result = response.json()
                st.success(f"mot ajouté avec succès ! ID: {result['id']}")
                st.balloons()
            else:
                st.error(f"Erreur de l'API avec le code {response.status_code}")


        except requests.exceptions.ConnectionError:
            st.error(f"ERREUR : Impossible de se connecter à l'API à {API_URL}")
            st.warning("Veuillez vous assurer que le serveur Uvicorn est bien lancé en arrière-plan.")

